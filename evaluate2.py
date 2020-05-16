import numpy as np
import lightWithRoot
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

norm = np.linalg.norm

people1 = np.array([60, 35])
people2 = np.array([10, 34])
people3 = np.array([15, 50])


def getStrength(iLight, distance):
    return iLight.strength / (distance / 1.0) ** 2


field = lightWithRoot.field


def getLightStrength(iLight, point):
    start = np.array(iLight.start)
    l1 = point - start
    distance = iLight.distance * np.array(iLight.direction)
    if norm(distance) == 0:
        d = norm(l1)
        if d < 1:
            return iLight.strength
        else:
            return 0
    else:
        d = abs(float(np.cross(l1, distance)) / iLight.distance)
        l = np.dot(l1, distance) / iLight.distance
        if d < 1 and l > 0:
            return getStrength(iLight, l)
        else:
            return 0


def getValue(lights, people):
    result = 0
    for light in lights.lights:
        result += getLightStrength(light, np.array(people))
    return result


def isOneSide(l1, l2, temp):
    return np.cross(l1, temp) * np.cross(l2, temp) < 0


def isInTriangle(root):
    temp = np.array(root)
    return isOneSide(people3 - people1, people2 - people1, temp - people1) and isOneSide(people2 - people3,
                                                                                         people1 - people3,
                                                                                         temp - people3) and isOneSide(
        people1 - people2, people3 - people2, temp - people2)


x = range(len(field))
y = range(len(field[0]))

values = np.zeros((len(field), len(field[0])), dtype=float)

for i in x:
    for j in y:
        root = [i * 10, j * 10]
        if isInTriangle([i,j]):
            print(i,j)
            iLights = lightWithRoot.Lights(root)
            iLights.getValue()
            values[i][j] = getValue(iLights, people1)
            values[i][j] += getValue(iLights, people2)
            values[i][j] += getValue(iLights, people3)
    # draw
np.save('values.npy',values)
X, Y = np.meshgrid(y, x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = plt.contourf(X, Y, values, 30, alpha=.9, cmap=plt.get_cmap('rainbow'))
xLabel = ax.set_xlabel('x', fontsize='20')
yLabel = ax.set_ylabel('y', fontsize='20')
zLabel = ax.set_zlabel('I', fontsize='20')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

params = {
    'font.size': '20',
    'axes.labelsize': '18',
    'xtick.labelsize': '12',
    'ytick.labelsize': '14',
    'lines.linewidth': '2',
    'legend.fontsize': '14',
    'font.sans-serif': 'SimHei',
    'figure.figsize': '60,48',  # set figure size
    'lines.markersize': '4',
    'figure.dpi': '300'
}
plt.rcParams.update(params)
plt.title('123')

plt.show()
