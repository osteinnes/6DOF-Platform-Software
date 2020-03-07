import numpy as np
from math import cos, sin, pi

# Manipulates points by roll, pitch, yaw
def rotate(pos, roll=0, pitch=0, yaw=0, rad=False):
    if not rad:                 # Converts to radians
        roll *= pi/180.0
        pitch *= pi/180.0
        yaw *= pi/180.0

    pos = np.array(pos)         # Create numpy array

                                # Transformation matrix
    r_mat = np.array([
    [cos(yaw)*cos(pitch), cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll), cos(yaw)*sin(pitch)*sin(roll)+sin(yaw)*cos(roll)],
    [cos(yaw)*cos(pitch), cos(yaw)*sin(pitch)*sin(roll)+sin(yaw)*cos(roll), cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll)],
    [-sin(pitch), cos(pitch)*sin(roll), cos(pitch)*cos(roll)]])

    result = np.dot(pos, r_mat).tolist()
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
    pos = (0, 0, 1)
    ang = 90
    tra = (2, 2, 2.1)

    print(pos)
    print(rotate(pos, roll=ang, pitch=ang, yaw=ang, rad=False))
    print(translate(pos, *tra))
