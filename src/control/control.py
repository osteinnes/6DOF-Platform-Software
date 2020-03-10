# Main file for 6DOF control system.
import numpy as np

K1, K2 = 0.1429, -0.2857

mat = np.array([
    [0, 1],
    [-7*K1, -7*K2]
])

def get_res(pos, speed):
    x = np.array([pos, speed])
    return mat.dot(x)

print(mat)

if __name__ == "__main__":
    pos = 30
    speed = 10 

    print(get_res(pos, speed))