import serial
import time
import json
from servos import Servos

ser = serial.Serial('COM3', baudrate=19200, timeout=0.1)
time.sleep(3)  # delay required before sending and receiving

values = {
    "pos1": 90,
    "pos2": 90,
    "pos3": 90,
    "pos4": 90,
    "pos5": 90,
    "pos6": 90,
    "counter": 0,
}

def set_angles(angles):
    for i, p in enumerate(values):
        if not None in angles and "pos" in p:
            if (i+1)%2 ==0:
                values[p] = 180 - angles[i]
            else:
                values[p] = angles[i]


def setValues(ang):
    set_angles(ang)
    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y

servos = Servos()
setValues([0, 0, 0, 0, 0, 0])


def test(delay=0):
    stuff = (5, 5, 5, 10, 10, 10)
    for i, m in enumerate(stuff):
        arr = [0, 0, 0, 0, 0, 0]
        arr[i] = m
        ang = servos.get_servo_angles(*arr)
        setValues(ang)
        time.sleep(delay)
        arr[i] = -2*m
        ang = servos.get_servo_angles(*arr)
        setValues(ang)
        time.sleep(delay)
        arr[i] = m
        ang = servos.get_servo_angles(*arr)
        setValues(ang)
        time.sleep(delay)

while True:
    roll, pitch, yaw = 0, 0, 0
    x, y, z = 0, 0, 0
    ang = []
    try:
        print("Enter: roll, pitch, and yaw")
        inp = input().split()

        if 2<len(inp):
            roll, pitch, yaw = [int(x) for x in inp]
            ang = servos.get_servo_angles(roll, pitch, yaw, x, y, z)

            print(ang)
            receivedValues = setValues(ang)
            print(receivedValues)

        elif "e" == inp[0]:
            break
        elif "test" == inp[0]:
            test()

    except:
        print("WRONG!!")
        continue
