from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import json as js

x, y, z= [], [], []
# Reads json configuration file and creates servo objects
with open('src/kinematics/servos.json', "r") as f:
    servos = js.load(f)
    for servo in servos[0]:
        x.append(servos[0][servo]["pos"][0])
        x.append(servos[0][servo]["cp"][0])
        y.append(servos[0][servo]["pos"][1])
        y.append(servos[0][servo]["cp"][1])
        z.append(servos[0][servo]["pos"][2])
        z.append(servos[0][servo]["cp"][2])



fig = pyplot.figure()
ax = Axes3D(fig)

ax.scatter(x, y, z)
pyplot.show()