import numpy as np

people1 = np.array([5, 5])
people2 = np.array([10, 0])
people3 = np.array([0, 0])


def isOneSide(l1, l2, temp):
    print(np.cross(l1, temp))
    print(np.cross(l2, temp))
    return np.cross(l1, temp) * np.cross(l2, temp) < 0


def isInTriangle(root):
    temp = np.array(root)
    return isOneSide(people3 - people1, people2 - people1, temp - people1) and isOneSide(people2 - people3,
                                                                                         people1 - people3,
                                                                                         temp - people3) and isOneSide(
        people1 - people2, people3 - people2, temp - people2)


print(isInTriangle([10, 1]))
