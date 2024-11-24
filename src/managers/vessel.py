import logging
from dataclasses import dataclass
from math import degrees
from re import S
from typing import Any, Callable, Dict, Optional, Union


class VesselModel:
    def __init__(self, active_vessel) -> None:

        self.active = active_vessel
        self.name = active_vessel.name
        self.orbit = active_vessel.orbit
        self.flight = active_vessel.flight()
        self.control = active_vessel.control
        self.comms = active_vessel.comms
        self.auto_pilot = active_vessel.auto_pilot

        self.tlm = Telemetry(active_vessel)

        self.log = logging.getLogger(f"azumi.{self.name}")

        self.sas_dict = {
            "stability_assist": self.auto_pilot.sas_mode.stability_assist,
            "maneuver": self.auto_pilot.sas_mode.maneuver,
            "prograde": self.auto_pilot.sas_mode.prograde,
            "retrograde": self.auto_pilot.sas_mode.retrograde,
            "normal": self.auto_pilot.sas_mode.normal,
            "anti_normal": self.auto_pilot.sas_mode.anti_normal,
            "radial": self.auto_pilot.sas_mode.radial,
            "anti_radial": self.auto_pilot.sas_mode.anti_radial,
            "target": self.auto_pilot.sas_mode.target,
            "anti_target": self.auto_pilot.sas_mode.anti_target,
        }

        # refframe = vessel.orbit.body.reference_frame
        # vessel.auto_pilot.target_direction = target_direction
        # vessel.auto_pilot.reference_frame = ref_frame
        # vessel.auto_pilot.engage()
        # vessel.auto_pilot.wait()

    def throttle(self, input_: float):
        """
        set throttle level

        args:
            input_ (int): 0.0% - 100.0% -> will be setted to throtlle
        """
        t = round(float(input_) / 100.0, 1)
        self.control.throttle = t

        # self.log.info(f"throttle state updated: {t}%")

    def autopilot(self, toggle: bool):
        """
        toggles autopilot

        args:
            toggle: state the ap will be set to
        """
        self.auto_pilot.disengage()
        if toggle == True:
            self.auto_pilot.engage()
        elif toggle == False:
            self.auto_pilot.disengage()

        self.log.info(f"ap state updated: {toggle}")

    def sas(self, mode: Union[str, bool]):
        """
        Toggle Sas or Sas Mode

        args:
            mode (str || bool): if bool, turn sas on or off, if str, activate sas and set sas mode to the one defined in the str, format: 'anti_normal'

            more modes at https://krpc.github.io/krpc/python/api/space-center/control.html#SpaceCenter.SASMode
        """
        mode_type = type(mode).__name__
        if mode_type == "str":
            self.auto_pilot.sas = True

            if mode not in self.sas_dict:
                self.log.error(
                    f"'{mode}' not valid sas mode, visit https://krpc.github.io/krpc/python/api/space-center/control.html#SpaceCenter.SASMode"
                )
                return

            change_to = self.sas_dict[mode]
            self.auto_pilot.sas_mode = change_to
            self.log.info(f"sas state updated: {mode}")

        elif mode_type == "bool":
            mode = bool(mode)
            self.auto_pilot.sas = mode
            self.log.info(f"sas state updated: {mode}")

        else:
            self.log.error(
                f"'{mode_type}' not valid sas mode or toggle, visit https://krpc.github.io/krpc/python/api/space-center/control.html#SpaceCenter.SASMode"
            )

    def rcs(self, toggle: bool):
        """
        toggles rcs

        args:
            toggle: state the rcs will be set to
        """
        self.control.rcs = toggle
        self.log.info(f"rcs state updated: {toggle}")

    def stage(self):
        """
        Simply Fire Next Stage
        """
        self.control.activate_next_stage()
        self.log.info("nex stage fired")

    def action_group(self, index: int):
        """
        Activate an action group

        args:
            index (int): the index of the action group u desire to fire
        """
        self.control.toggle_action_group(index)
        self.log.info(f"ag fired: {index}")


def normalize_angle(angle: float) -> float:
    """Normalizes an angle to the range [0°, 360°].

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The normalized angle in the range [0°, 360°].
    """
    return angle % 360 if angle >= 0 else (angle % 360 + 360)


@dataclass
class TelemetryData:
    """Data structure for vessel telemetry values"""

    altitude: float = 0.0
    apoapsis: float = 0.0
    periapsis: float = 0.0
    velocity = [0.0, 0.0]
    speed: float = 0.0
    vertical_speed: float = 0.0
    horizontal_speed: float = 0.0
    pitch: float = 0.0
    yaw: float = 0.0
    heading: float = 0.0
    roll: float = 0.0
    time_to_apoapsis: float = 0.0
    time_to_periapsis: float = 0.0
    orbital_speed: float = 0.0
    surface_gravity: float = 0.0
    q: float = 0.0  # Dynamic pressure
    g_force: float = 0.0
    mean_altitude: float = 0.0
    biome: str = ""
    situation: str = ""
    latitude: float = 0.0  # New field for latitude
    longitude: float = 0.0  # New field for longitude
    drag = 0.0


class Telemetry:
    """Handles vessel telemetry data collection and access"""

    def __init__(self, vessel) -> None:
        self.vessel = vessel

        refframe = vessel.orbit.body.reference_frame

        self.log = logging.getLogger("azumi.telemetry")
        self._cached_data: Optional[TelemetryData] = None
        self._telemetry_map: Dict[str, Any] = {
            # Flight data
            "altitude": lambda: self.vessel.flight().surface_altitude,
            "mean_altitude": lambda: self.vessel.flight().mean_altitude,
            "speed": lambda: self.vessel.flight(refframe).speed,
            "velocity": lambda: self.vessel.flight(refframe).velocity,
            "vertical_speed": lambda: self.vessel.flight(refframe).vertical_speed,
            "horizontal_speed": lambda: self.vessel.flight(refframe).horizontal_speed,
            "pitch": lambda: normalize_angle(self.vessel.flight().pitch + 90),
            "heading": lambda: self.vessel.flight().heading,
            "roll": lambda: normalize_angle(self.vessel.flight().roll + 180),
            "q": lambda: self.vessel.flight().dynamic_pressure,
            "g_force": lambda: self.vessel.flight().g_force,
            "biome": lambda: self.vessel.flight().biome,
            "situation": lambda: str(self.vessel.situation),
            # Orbital data
            "apoapsis": lambda: self.vessel.orbit.apoapsis_altitude,
            "periapsis": lambda: self.vessel.orbit.periapsis_altitude,
            "time_to_apoapsis": lambda: self.vessel.orbit.time_to_apoapsis,
            "time_to_periapsis": lambda: self.vessel.orbit.time_to_periapsis,
            "orbital_speed": lambda: self.vessel.orbit.orbital_speed,
            # Body data
            "surface_gravity": lambda: self.vessel.orbit.body.surface_gravity,
            "latitude": lambda: degrees(self.vessel.flight().latitude),
            "longitude": lambda: degrees(self.vessel.flight().longitude),
            "drag": lambda: degrees(self.vessel.flight(refframe).drag),
            "lift": lambda: degrees(self.vessel.flight(refframe).lift),
            "drag_coefficient": lambda: degrees(
                self.vessel.flight(refframe).drag_coefficient
            ),
            "lift_coefficient": lambda: degrees(
                self.vessel.flight(refframe).lift_coefficient
            ),
            "ballistic_coefficient": lambda: degrees(
                self.vessel.flight(refframe).ballistic_coefficient
            ),
            "terminal_velocity": lambda: degrees(
                self.vessel.flight(refframe).terminal_velocity
            ),
        }

    def register(self, name: str, return_function: Callable[[], Any]) -> None:
        """Register a new telemetry key with its corresponding getter function."""
        if name in self._telemetry_map:
            self.log.warning(f"Telemetry key '{name}' already exists.")
        else:
            self._telemetry_map[name] = return_function
            self.log.info(f"Telemetry key '{name}' registered successfully.")

    def get(self, key: str) -> Any:
        """Get a specific telemetry value"""
        try:
            if key in self._telemetry_map:
                return self._telemetry_map[key]()
            else:
                self.log.warning(f"Unknown telemetry key: {key}")
                return 0.0
        except Exception as e:
            self.log.error(f"Error getting telemetry for {key}: {str(e)}")
            return 0.0

    def get_all(self) -> TelemetryData:
        """Get all telemetry data at once"""
        try:
            return TelemetryData(
                altitude=self.get("altitude"),
                mean_altitude=self.get("mean_altitude"),
                apoapsis=self.get("apoapsis"),
                periapsis=self.get("periapsis"),
                vertical_speed=self.get("vertical_speed"),
                horizontal_speed=self.get("horizontal_speed"),
                pitch=self.get("pitch"),
                heading=self.get("heading"),
                roll=self.get("roll"),
                time_to_apoapsis=self.get("time_to_apoapsis"),
                time_to_periapsis=self.get("time_to_periapsis"),
                orbital_speed=self.get("orbital_speed"),
                surface_gravity=self.get("surface_gravity"),
                q=self.get("q"),
                g_force=self.get("g_force"),
                biome=self.get("biome"),
                situation=self.get("situation"),
                latitude=self.get("latitude"),
                longitude=self.get("longitude"),
            )
        except Exception as e:
            self.log.error(f"Error getting all telemetry: {str(e)}")
            return TelemetryData()
