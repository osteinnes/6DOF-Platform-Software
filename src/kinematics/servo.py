import numpy as np
from math import sin, cos, tan, acos, atan, sqrt, pi

class Servo:
    # Variables used by inverse kinematics of arm
    s, s1 = 0, 0
    A = None                        # Center of servo
    a = 0                           # Length of servo arm
    angle = None                    # Mounting angle of servo
    p = (0, 0, 0)                   # Platform connection point

    # Set classes points
    def __init__(self, servo_center, angle, platform_point, rod_length=290, arm_length=45):
        self.s = rod_length
        self.A = np.array(servo_center)
        self.a = arm_length
        self.angle = angle*pi/180
        self.p = np.array(platform_point)

    # Update platform connection point
    def set_platform_point(self, point):
        self.p = np.array(point)

    # Returns platform point
    def get_platform_point(self):
        return self.p

    # Insert platform connection point and get servo angle
    def get_servo_angle(self):
        s1 = self.p - self.A        # From servo to platform
        s1 = s1.dot(s1)             # Length

        M = self.s**2 - self.a**2 - s1
        K = 2*(self.A[2] - self.p[2])*self.a
        L = 2*(self.A[0] - self.p[0])*self.a*cos(self.angle) + 2*(self.A[1] - self.p[1])*self.a*sin(self.angle)

        try:
            angle = pi - (acos(M/sqrt(K**2 + L**2)) + atan(L/K))
            return round(angle*180/pi + 50)
        except ValueError:
            print("No cos angle exists exists")
            return None


if __name__ == "__main__":
    servo1 = Servo((7, -16, -25), angle=60, platform_point=(0, -17.5, 0))
    print(servo1.get_servo_angle())