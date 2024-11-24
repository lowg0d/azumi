import importlib
import inspect
import json
import logging
import os
import sys
import traceback
from typing import Any, Dict, List, Tuple

from PySide6.QtCore import QObject, QThread, Signal

from ..managers import Mission

MISSIONS_PATH = "./missions"
PROFILES_PATH = "src.profiles"


class MissionControlManager(QObject):
    populate_folder = Signal(list)
    populate_missions = Signal(list)
    write = Signal(str)
    state = Signal(str, str)
    status = Signal(str)

    exit_signal = Signal()
    come_back_to_selector = Signal()
    start_visualization_thread = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.log = logging.getLogger(f"azumi.msn_control")
        self.lastest_msn_path = ""
        self.msn = None
        # check if the mission path exists
        self._check_path()

    def execute(self, parameters):

        with open(self.lastest_msn_path, "r") as f:
            data = json.loads(f.read())

        msn_name = data.get("name", None)
        if msn_name == None:
            self.log.error("Invalid mission format")
            sys.exit(1)

        profile = data["profile"]
        self.log.info(f"Mission Name: {msn_name}")
        self.log.info(f"Mission Profile: {profile}")

        success = self._start_msn(profile, parameters)
        return success

    def get_tlm(self, value):
        if self.msn:
            return self.msn.vessel.tlm.get(value)

        else:
            self.log.warning("Missions instance not found !")

    def get_mission_data(self, mission_path: str) -> dict[str, Any]:
        """
        Reads a .json file containing mission data and returns its content as a dictionary.

        Args:
            folder (str): The folder containing the mission files.
            mission (str): The name of the mission file (without the .json extension).

        Returns:
            dict[str, Any]: The content of the mission file as a dictionary.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the file is not a valid JSON format.
            OSError: For any other I/O related issues.
        """
        # Construct the path to the .json file
        mission_path = f"{mission_path}.json"
        path = os.path.join(MISSIONS_PATH, mission_path)
        self.lastest_msn_path = path

        try:
            # Open and read the JSON file
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The file at {path} was not found.") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"The file at {path} is not valid JSON.") from e
        except OSError as e:
            raise OSError(
                f"An error occurred while accessing the file at {path}."
            ) from e

        return data

    def get_folders(self) -> List[str]:
        """
        Retrieves a list of folders from the specified path.

        Returns:
            List[str]: A list of folder names within the specified directory.
        """
        folders = []
        for folder in os.listdir(MISSIONS_PATH):
            folder_path = os.path.join(MISSIONS_PATH, folder)
            if os.path.isdir(folder_path):
                folders.append(folder)
                self.log.debug(f"Found mission subfolder '{folder}' !")
        return folders

    def get_missions(self, folder_path: str) -> List[str]:
        """
        Retrieves mission names from a specified folder by looking for `.json` files.

        Args:
            folder_path (str): Path to the folder containing `.json` mission files.

        Returns:
            List[str]: A list of mission names (derived from `.json` file names).
        """
        missions = []
        folder = os.path.join(MISSIONS_PATH, folder_path)

        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            if os.path.isfile(item_path) and item.endswith(".json"):
                mission_name = os.path.splitext(item)[0]
                missions.append(mission_name)
                self.log.debug(f"Mission found '{mission_name}' at '{folder}'!")

        return missions

    def _start_msn(self, profile_name: str, data: Dict):
        try:
            # Attempt to import the module
            module = importlib.import_module(f"{PROFILES_PATH}.{profile_name}")
            self.log.debug("Module found!")

            # Loop through members and look for a valid Mission subclass
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Mission) and obj != Mission:
                    self.log.debug(f"Mission class found: {name}")
                    try:
                        # Instantiate the mission class and set up connections
                        self.msn = obj(data)
                        self.msn.write.connect(self.write.emit)
                        self.msn.state.connect(self.state.emit)
                        self.msn.status.connect(self.status.emit)
                        self.msn.connected.connect(self.start_visualization_thread)
                        self.exit_signal.connect(self.msn.terminate)
                        self.msn.finished.connect(self.come_back_to_selector.emit)
                        self.msn.start()
                        return True
                    except Exception as exc:
                        self.log.error(f"Exception during mission execution: {exc}")
                        traceback.print_exc()
                        return False

            # No valid mission class found
            self.log.error(
                f"No valid subclass of Mission found in module {profile_name}"
            )
            return False

        except Exception as e:
            self.log.error(f"Failed to load or instantiate mission class: {e}")
            return False

        return False

    def _check_path(self) -> None:
        if not os.path.exists(MISSIONS_PATH):
            self.log.warning(
                f"Mission path ({MISSIONS_PATH}) does not exist, CREATING..."
            )
            os.mkdir(MISSIONS_PATH)

        return
