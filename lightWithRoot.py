import numpy as np
import wall

min = 0.00000000001  # 最小条件
max = 20000000  # 光源
myfWall = wall.Wall('./room.jpg')
field = myfWall.getValue()
setstep = 5
N = 400


class Lights:
    def __init__(self, root):
        self.root = root
        self.lights = []

    def getValue(self):
        if isWall(self.root):
            return
        for i in range(N):
            angle = 2 * np.pi / N * i
            direction = [np.cos(angle), np.sin(angle)]
            light = Light(self.root, direction, max, angle)
            self.lights.append(light)

        i = 0
        while i < len(self.lights):
            self.grow(self.lights[i], setstep)
            i = i + 1
            if i == 10000:
                break

    def grow(self,iLight, step):
        while (True):
            distance = float(iLight.distance + step)
            location = np.array(iLight.start) + distance * np.array(iLight.direction)
            if getStrength(iLight, distance) < min:
                return

            if isWall(location) == -1:
                return
            if isWall(location):
                if distance == step:
                    return
                flag = getWallDirection(location)
                if flag == 2:
                    rAngle = - iLight.angle
                    rDirection = [iLight.direction[0], -iLight.direction[1]]
                elif flag == 1:
                    rAngle = np.pi - iLight.angle
                    rDirection = [-iLight.direction[0], iLight.direction[1]]
                else:
                    rDirection = [-iLight.direction[0], -iLight.direction[1]]
                    rAngle = np.pi + iLight.angle
                rate = getRate(location)
                if rate == 1:
                    rLight = Light(location, rDirection, rate * getStrength(iLight, distance), rAngle)
                    self.lights.append(rLight)

                    return

                else:
                    rLight = Light(location, rDirection, rate * getStrength(iLight, distance), rAngle)
                    tLightLocation = getTLightLocation(location, iLight.direction, 1)
                    tLight = Light(tLightLocation, iLight.direction, (1 - rate) * getStrength(iLight, distance),
                                   iLight.angle)
                    self.lights.append(rLight)
                    self.lights.append(tLight)
                    return
            iLight.distance = distance


class Light:
    def __init__(self, location, direc, strength, ang):
        self.start = location
        self.direction = direc
        self.strength = strength
        self.distance = 0.
        self.angle = ang





def trans(lightLocation):
    y = int(lightLocation[0] / 10.0)
    x = int(lightLocation[1] / 10.0)
    return [x, y]


def getRate(lightLocation):
    fieldLocation = trans(lightLocation)
    if fieldLocation[0] > 91 or fieldLocation[1] > 84:
        return 1
    return field[fieldLocation[0]][fieldLocation[1]]


def getWallDirection(lightLocation):
    fieldLocation = trans(lightLocation)
    flag = 0
    if fieldLocation[0] > 91 or fieldLocation[1] > 84:
        return flag
    if field[fieldLocation[0] - 1][fieldLocation[1]] == field[fieldLocation[0]][fieldLocation[1]]:
        flag = flag + 1  # x
    elif field[fieldLocation[0]][fieldLocation[1] - 1] == field[fieldLocation[0]][fieldLocation[1]]:
        flag = flag + 2  # y
    return flag


def getStrength(iLight, distance):
    return iLight.strength / (distance / 1.0) ** 2


def isWall(lightLocation):
    fieldLocation = trans(lightLocation)
    # if fieldLocation[0] == 0 or fieldLocation[1] == 0 or fieldLocation[0] == len(field) or fieldLocation[1] == len(
    #         field[0]):
    #     return -1  # boundary
    if fieldLocation[0] >= 92 or fieldLocation[1] >= 85:
        return -1
    if field[fieldLocation[0]][fieldLocation[1]] != 0:
        return True  #
    return False  # False


def getTLightLocation(lightLocation, direc, step):
    result = np.array(lightLocation)
    while True:
        if isWall(result) != True:
            return result
        result = np.array(result) + step * np.array(direc)


lights = Lights([500, 430])
lights.getValue()
