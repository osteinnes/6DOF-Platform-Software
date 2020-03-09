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


def setValues():
    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y

servos = Servos()
setValues()

while True:

    
    roll, pitch, yaw = 0, 0, 0
    try:
        print("Enter three angles: roll, pitch, and yaw")
        inp = input().split()

        if 2<len(inp):
            roll, pitch, yaw = [int(x) for x in inp]
        elif "e" == inp[0]:
            break
    except:
        print("WRONG!!")
        continue

    angles = servos.get_servo_angles(roll = roll, pitch = pitch, yaw = yaw)

    for i, p in enumerate(values):
        if not None in angles and "pos" in p:
            if (i+1)%2 ==0:
                values[p] = 180 - angles[i]
            else:
                values[p] = angles[i]

    print(angles)
    receivedValues = setValues()
    print(receivedValues)
