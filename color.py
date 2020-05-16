import numpy as np

cmap = np.ones([52, 3])
for i in np.arange(0, 52):  # 函数
    for j in np.arange(0, 3):
        if j == 0:
            cmap[i][j] = 255
        elif j == 2:
            cmap[i][j] = 0
        elif j == 1:
            cmap[i][j] = 5 * i

# total list
for i in np.arange(0, 52):
    print(cmap[i])

# examples
print(cmap[0])
print(cmap[26])
print(cmap[51])
