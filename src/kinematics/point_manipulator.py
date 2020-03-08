import numpy as np
from math import cos, sin, pi
import time as t

# Manipulates points by roll, pitch, yaw
def rotate(pos, roll=0, pitch=0, yaw=0, rad=False):
    if not rad:                 # Converts to radians
        roll *= pi/180
        pitch *= pi/180
        yaw *= pi/180

    pos = np.array(pos)         # Create numpy array

                                # Transformation matrix
    yaw_mat = np.array([
        [cos(yaw), -sin(yaw), 0],
        [sin(yaw), cos(yaw), 0],
        [0, 0, 1]
    ])

    pitch_mat = np.array([
        [cos(pitch), 0, sin(pitch)],
        [0, 1, 0],
        [-sin(pitch), 0, cos(pitch)]
    ])

    roll_mat = np.array([
        [1, 0, 0],
        [0, cos(roll), -sin(roll)],
        [0, sin(roll), cos(roll)]
    ])

    result = yaw_mat.dot(pitch_mat).dot(roll_mat).dot(pos).tolist()
    result = [round(e, 2) for e in result]

                                # Return result as tuple
    return tuple(result)

# Manipulates point in x,y,z direction
def translate(pos, x=0, y=0, z=0):
    pos = np.array(pos)         # Create numpy array
    pos = np.append(pos, 1)

    t_mat = np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

    result = np.dot(t_mat, pos)
    result = [round(e, 2) for e in result]

    return tuple(np.delete(result, -1))
    

if __name__ == "__main__":
    pos = (2, 0, 0)
    ang = 90
    tra = (2, 2, 2.1)
    
    print(pos)
    new_pos = rotate(pos, pitch=ang)
    print(new_pos)
    new_pos = translate(new_pos, *tra)
    print(new_pos)
