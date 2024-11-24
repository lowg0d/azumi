import time


class PIDController:
    def __init__(
        self, kp, ki, kd, setpoint, output_limits=(None, None), sample_time=0.01
    ):
        """
        Initialize the PID controller.

        :param kp: Proportional gain.
        :param ki: Integral gain.
        :param kd: Derivative gain.
        :param output_limits: Tuple (min, max) for output limits.
        :param sample_time: Time interval for updates in seconds.
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.min_output, self.max_output = output_limits
        self.sample_time = sample_time

        self.setpoint = setpoint
        self.last_error = 0
        self.integral = 0
        self.last_time = None

    def update(self, current_value):
        """
        Update the PID control output based on the current value.

        :param current_value: The current process variable.
        :return: Control output.
        """
        current_time = time.time()
        if self.last_time is None:
            self.last_time = current_time
            return 0

        dt = current_time - self.last_time
        if dt < self.sample_time:
            return 0

        error = self.setpoint - current_value
        self.integral += error * dt
        derivative = (error - self.last_error) / dt if dt > 0 else 0

        # Anti-windup: Clamp the integral
        if self.ki > 0.0:
            if self.max_output is not None and self.min_output is not None:
                self.integral = max(
                    min(self.integral, self.max_output / self.ki),
                    self.min_output / self.ki,
                )

        # PID Output
        output = self.kp * error + self.ki * self.integral + self.kd * derivative

        # Apply output limits
        if self.max_output is not None:
            output = min(output, self.max_output)
        if self.min_output is not None:
            output = max(output, self.min_output)

        # Update for next iteration
        self.last_error = error
        self.last_time = current_time

        return output

    def set_tunings(self, kp, ki, kd):
        """
        Adjust PID coefficients.

        :param kp: Proportional gain.
        :param ki: Integral gain.
        :param kd: Derivative gain.
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def set_setpoint(self, setpoint):
        """
        Set the desired target value.

        :param setpoint: The new setpoint.
        """
        self.setpoint = setpoint

    def reset(self):
        """Reset the PID controller."""
        self.last_error = 0
        self.integral = 0
        self.last_time = None
