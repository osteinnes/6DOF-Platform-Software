from point_manipulator import rotate, translate
from servo import Servo
from matplotlib import pyplot as plt
from math import sin, cos, pi
import json as js

class Servos:
  servos = []

  # Set platform connection points
  def __init__(self):
    self.set_servos()

  # Rotates the points and returns servo angles
  def get_servo_angles(self, roll=0, pitch=0, yaw=0, x=0, y=0, z=0):
    result = []
    old_points = []
    for servo in self.servos:
      old_points.append(servo.get_platform_point())
      point = servo.get_platform_point()
      new_point = rotate(point, roll, pitch, yaw)
      new_point = translate(new_point, x, y, z)
      servo.set_platform_point(new_point)
      angle = servo.get_servo_angle()
      result.append(angle)

    if None in result:
      for i, servo in enumerate(self.servos):
        servo.set_platform_point(old_points[i])

    return result

  # Reads json configuration file and creates servo objects
  def set_servos(self, path='src/kinematics/servos.json'):
    with open(path, "r") as f:
      servos = js.load(f)
      for servo in servos[0]:
        s = servos[0][servo]
        self.servos.append(Servo(s["pos"], s["ang"], s["cp"]))

if __name__ == "__main__":
  sp = Servos()

  while True:
    try:
      roll, pitch, yaw = input().split()
      roll = int(roll)
      pitch = int(pitch)
      yaw = int(yaw)
    except ValueError:
      print("Moron!! That's not three numbers seperated by spaces!")
      continue

    new_point = sp.get_servo_angles(roll, pitch, yaw)
    print(new_point)
