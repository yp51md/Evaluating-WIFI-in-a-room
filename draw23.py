import numpy as np
import lightWithRoot
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
field = lightWithRoot.field
x = range(len(field))
y = range(len(field[0]))
values = np.load('values.npy')
np.save('values.npy',values)
X, Y = np.meshgrid(y, x)
fig = plt.figure()
ax = fig.add_subplot(111)
surf = plt.contourf(X, Y, values, 30, alpha=.9, cmap=plt.get_cmap('rainbow'))
xLabel = ax.set_xlabel('x', fontsize='20')
yLabel = ax.set_ylabel('y', fontsize='20')

plt.clabel(surf,inline=True,fmt='%1.1f',fontsize=10)
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
plt.show()
