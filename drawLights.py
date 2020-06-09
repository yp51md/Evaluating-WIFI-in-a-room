import turtle
import numpy as np
import light

lights = light.lights

lightMax = light.max
lightMin = light.min


def getStrength(light, distance):
    return np.log(light.strength / (distance / 1.0) ** 2)


def getColor(x):
    cmap = [[255, 0, 0], [255, 5, 0], [255, 10, 0], [255, 15, 0], [255, 20, 0], [255, 25, 0], [255, 30, 0],
            [255, 35, 0], [255, 40, 0], [255, 45, 0], [255, 50, 0],
            [255, 55, 0], [255, 60, 0], [255, 65, 0], [255, 70, 0],
            [255, 75, 0], [255, 80, 0], [255, 85, 0], [255, 90, 0],
            [255, 95, 0], [255, 100, 0], [255, 105, 0], [255, 110, 0],
            [255, 115, 0], [255, 120, 0], [255, 125, 0], [255, 130, 0], [255, 135, 0],
            [255, 140, 0], [255, 145, 0], [255, 150, 0], [255, 155, 0],
            [255, 160, 0], [255, 165, 0], [255, 170, 0], [255, 175, 0], [255, 180, 0],
            [255, 185, 0], [255, 190, 0], [255, 195, 0], [255, 200, 0],
            [255, 205, 0], [255, 210, 0], [255, 215, 0], [255, 220, 0],
            [255, 225, 0], [255, 230, 0], [255, 235, 0], [255, 240, 0],
            [255, 245, 0], [255, 250, 0], [255, 255, 0], [255, 0, 0],
            [255, 130, 0], [255, 255, 0]]
    inter = (np.log(lightMax) - np.log(lightMin)) / 51

    i = int(51 - (x - np.log(lightMin)) / inter)
    if i <= 0:
        return cmap[0]
    elif i >= 51:
        return cmap[51]
    else:
        return cmap[i]


step = 2
turtle.screensize(1800, 1600, )
turtle.tracer(0)
ninja = turtle.Turtle()
ninja.speed(20000)
ninja.pensize(1)
turtle.colormode(255)
for i in range(len(lights)):
    length = 0
    x = lights[i].start[0]
    y = lights[i].start[1]
    ninja.penup()
    ninja.setposition(x, y)
    angle = lights[i].angle / np.pi * 180
    ninja.setheading(angle)
    ninja.pendown()
    while length < lights[i].distance:
        length = length + step
        strength = getStrength(lights[i], length)
        ninja.pencolor(getColor(strength))
        ninja.forward(step)
turtle.update()
turtle.done()
