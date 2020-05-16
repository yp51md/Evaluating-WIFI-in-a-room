import wall

myfWall = wall.Wall('./51.jpg')
a = myfWall.getValue()
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 0.6:
            print('[',i,j,']')
