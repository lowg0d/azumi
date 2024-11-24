import math
import time
from math import asin, atan2, cos, degrees, exp, pi, radians, sin, sqrt

import numpy as np

from ..managers import Mission
from ..managers.gnc import PIDController

TIME_STEP = 0.01
KERBIN_RADIUS = 600000  # Kerbin radius in meters
# test what pitch, yaw, roll etc. do


class DebugMission(Mission):
    def __init__(self, data) -> None:
        super().__init__(data)

        self.estimate_lat = 0
        self.estimate_lon = 0
        self.out_pitch = 0

        self.landing_target = self.data.get("landing_target", [-1, -2])

        self.kp = 10.7
        self.ki = 0.0
        self.kd = 0.0

        self.kp_roll = 0.010000
        self.ki_roll = 0.000001
        self.kd_roll = 0.000001

        self.landing_target_lat = self.landing_target[0]
        self.landing_target_lon = self.landing_target[1]

    def execute(self):

        self.vessel.tlm.register("estimated_lat", self._get_estimated_lat)
        self.vessel.tlm.register("estimated_lon", self._get_estimated_lon)
        self.vessel.tlm.register("out_pitch", self._get_out_pitch)

        """
        while True:
            # lat, lon = self.predict_impact_kerbin()

            self.estimate_lat = lat
            self.estimate_lon = lon

            time.sleep(0.01)
        """

    def _get_estimated_lat(self):
        return self.estimate_lat

    def _get_estimated_lon(self):
        return self.estimate_lon

    def _get_out_pitch(self):
        return self.out_pitch
