import numpy as np
import light_new
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

norm = np.linalg.norm


def getStrength(iLight, distance):
    return iLight.strength / (distance / 1.0) ** 2


lights = light_new.lights
field = light_new.field


def getLightStrength(iLight, point):
    start = np.array(iLight.start)
    l1 = point - start
    distance = iLight.distance * np.array(iLight.direction)
    if norm(distance) == 0:
        d = norm(l1)
        if d < 10:
            return iLight.strength
        else:
            return 0
    else:
        d = abs(float(np.cross(l1, distance)) / iLight.distance)
        l = np.dot(l1, distance) / iLight.distance
        if d < 10 and l > 0:
            return getStrength(iLight, l)
        else:
            return 0


x = range(len(field))
y = range(len(field[0]))
value = np.zeros((len(field), len(field[0])))
for i in x:
    print(i)
    for j in y:
        if field[i][j] != 0:
            value[i][j] = 0
        else:
            for light in lights:
                value[i][j] = value[i][j] + getLightStrength(light, np.array([i, j]))
            if value[i][j] < 1:
                value[i][j] = 0
            else:
                value[i][j] = np.log(value[i][j])

np.save('values1.npy',value)
X, Y = np.meshgrid(y, x)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
surf = ax.plot_surface(X, Y, value, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
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
