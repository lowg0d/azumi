import os
import subprocess
from functools import partial

from kore import Interface  # type:ignore
from PySide6.QtCore import QPropertyAnimation, SignalInstance
from PySide6.QtWidgets import QFrame, QGraphicsOpacityEffect, QLayout, QWidget

from .components import ParameterWidget
from .gui.views import Ui_MainWindow
from .managers import MissionControlManager, TerminalModel, VisualizationModel


class MainWindow(Interface):

    def __init__(self, app_data) -> None:
        super().__init__(app_data)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_msn_parameters = {}

        self.terminal = TerminalModel(self.ui.terminal)

        # start mission control, will check for mission folder, and populate comboboxes with data.
        self.msn_control = MissionControlManager()
        self.visualization = VisualizationModel(
            self.msn_control,
            self.ui.graph_container,
            self.ui.primaryLabelsLayout,
            self.ui.secondaryLabelsLayout,
        )
        self.msn_control.write.connect(self.terminal.write)
        self.msn_control.status.connect(self.status_update)
        self.msn_control.start_visualization_thread.connect(
            self.visualization.update_thread.start
        )
        self.ui.msn_exit_btn.clicked.connect(self.msn_control.exit_signal.emit)
        self.msn_control.come_back_to_selector.connect(
            self.come_back_to_mission_selector
        )
        # get a list of missions and subfolders where they are, then add them to the combo boxes.
        folder_list = self.msn_control.get_folders()
        self.ui.msn_folder_comboBox.addItems(folder_list)
        self.update_mission_combobox()

        self.ui.edit_btn.clicked.connect(self.open_mission_file)
        self.ui.execute_btn.clicked.connect(self.start_mission)

        # when subfolder is changed, then switch missions, to the ones inside that subfolder
        self.ui.msn_folder_comboBox.currentTextChanged.connect(
            self.update_mission_combobox
        )
        # when a mission is changed, the change the information dispalayed on the right panel.
        self.ui.msn_combobox.currentTextChanged.connect(self.update_mission_data)
        self.update_mission_data()

        self.ui.centralStackedWidget.setCurrentWidget(self.ui.msnSelectPage)

        self.ui.kp.valueChanged.connect(self.update_kp)
        self.ui.kd.valueChanged.connect(self.update_kd)
        self.ui.ki.valueChanged.connect(self.update_ki)

        # set the status bar label that shows the version, to the current version and show the app
        self.ui.version_label.setText(f"v{self.version}")
        self.show()
        # apply theme after showing, to bypass a bug, that will not set it if done before
        self.apply_theme("dark")
        self.fade_animation(self.ui.msnSelectPage, 100)

        self.start_mission()

    def update_kp(self, value):
        if self.msn_control.msn:
            self.msn_control.msn.kp = value  # type:ignore

    def update_kd(self, value):
        if self.msn_control.msn:
            self.msn_control.msn.kd = value  # type:ignore

    def update_ki(self, value):
        if self.msn_control.msn:
            self.msn_control.msn.ki = value  # type:ignore

    def fade_animation(
        self,
        container: QWidget,
        duration: int = 200,
        start_value: float = 0.0,
        end_value: float = 1.0,
    ) -> SignalInstance:
        """Applies a fade-in animation to the given container widget.

        Args:
            container (QWidget): The QWidget to apply the fade-in effect.
            duration (int, optional): The duration of the fade-in animation in milliseconds. Defaults to 200.
        """

        # Make the container visible initially.
        container.setVisible(True)

        # Create an opacity effect for the container.
        opacity_effect = QGraphicsOpacityEffect(container)

        # Create an animation for the container's opacity effect.
        animation = QPropertyAnimation(opacity_effect, b"opacity", parent=container)

        # Apply the opacity effect to the container.
        container.setGraphicsEffect(opacity_effect)

        def cleanup():
            container.removeEventFilter(self)
            container.setGraphicsEffect(None)  # type: ignore
            try:
                opacity_effect.deleteLater()
                animation.deleteLater()
            except:
                pass

        # Configure and start the opacity animation.
        animation.setStartValue(start_value)
        animation.setEndValue(end_value)
        animation.setDuration(duration)
        animation.finished.connect(cleanup)
        animation.start()

        return animation.finished

    def come_back_to_mission_selector(self):
        self.ui.centralStackedWidget.setCurrentWidget(self.ui.msnSelectPage)
        self.fade_animation(self.ui.msnSelectPage, 100)
        self.visualization.update_thread.terminate()
        self.visualization.clear()
        self.terminal.clear()

    def start_mission(self):
        success = self.msn_control.execute(self.current_msn_parameters)
        if success:
            self.visualization.setup_dashborad(self.current_msn_visualization_data)
            self.ui.centralStackedWidget.setCurrentWidget(self.ui.dashPage)
            self.fade_animation(self.ui.dashPage, 50)

    def open_mission_file(self):
        current_mission = f"{self.ui.msn_combobox.currentText()}.json"
        current_folder = self.ui.msn_folder_comboBox.currentText()

        if not current_mission or not current_folder:
            return

        file_path = os.path.join("./missions", current_folder, current_mission)

        if os.path.exists(file_path) and file_path.endswith(".json"):
            try:
                # On Windows, 'start' opens the file with the default associated application
                subprocess.run(["start", file_path], shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error opening file: {e}")
        else:
            print("The file does not exist or is not a .json file.")

    def update_mission_data(self) -> None:
        current_mission = self.ui.msn_combobox.currentText()
        current_folder = self.ui.msn_folder_comboBox.currentText()

        # reject initial update
        if not current_mission or not current_folder:
            return

        mission_path = os.path.join(current_folder, current_mission)
        msn_data = self.msn_control.get_mission_data(mission_path)

        self.ui.msn_indicator_dash.setText(f"{current_folder}/{current_mission}")

        title = msn_data.get("name", "INVALID DATA")
        description = msn_data.get("description", "INVALID DATA")
        profile = msn_data.get("profile", "INVALID DATA")
        visualization = msn_data.get("visualization", {})
        parameters = msn_data.get("parameters", {"invalida_data": "invalid_data"})
        self.current_msn_parameters = parameters
        self.current_msn_visualization_data = parameters
        self.current_msn_visualization_data = visualization

        # update the parameters
        self.update_parameters(parameters)

        # update labels
        self.ui.msn_title_label.setText(title)
        self.ui.msn_description_label.setText(f"<b>{profile}</b> | {description}")

        self.log.debug(f"data update for '{title}'")

    def update_parameters(
        self,
        parameters,
    ):
        self.clear_layout(self.ui.mission_parameters_layout)

        parameter_items = parameters.items()
        for key, current_value in parameter_items:
            widget = ParameterWidget(current_value)

            widget.ui.name_label.setText(key)
            widget.update_value.connect(partial(self.update_value, key))
            widget.check_if_it_is_dict()

            line = QFrame(self)
            line.setFrameShape(QFrame.HLine)  # type:ignore
            line.setFrameShadow(QFrame.Sunken)  # type:ignore
            line.setFixedHeight(1)
            line.setStyleSheet("background-color: #383838;")  # Set the background color

            # Add the line to the layout
            self.ui.mission_parameters_layout.addWidget(widget)
            self.ui.mission_parameters_layout.addWidget(line)

    def update_value(self, key, value):
        self.current_msn_parameters[key] = value

    def clear_layout(self, layout: QLayout) -> None:
        """
        Clears all items from the given layout and deletes the widgets.

        Args:
            layout (QLayout): The layout to be cleared.

        Raises:
            ValueError: If the layout is not valid (None or empty).
        """
        if layout is None:
            raise ValueError("The layout cannot be None")

        # Iterate through all items in the layout
        while layout.count():
            item = layout.takeAt(0)  # Remove the item from the layout
            if item is not None:
                widget = item.widget()  # Get the widget inside the item
                if widget is not None:
                    widget.deleteLater()  # Safely delete the widget

    def update_mission_combobox(self) -> None:
        self.ui.msn_combobox.clear()
        current_folder = self.ui.msn_folder_comboBox.currentText()
        mission_list = self.msn_control.get_missions(current_folder)
        self.ui.msn_combobox.addItems(mission_list)
        self.log.debug("mission combo box updated !")

    def status_update(self, str):
        self.ui.status_label.setText(str)

    def apply_theme(self, name: str):
        with open(f"./src/gui/assets/themes/{name}.qss", "r") as f:
            theme_data = f.read()
            self.apply_style(theme_data)
