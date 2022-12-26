import turtle
import random
from math import *
erase = turtle.Turtle()
erase.up()
erase.pencolor('black')
erase.width(5)
erase.ht()
draw = turtle.Turtle()
draw.up()
draw.width(3)
draw.pencolor('white')
draw.ht()
turtle.colormode(255)

n = 10 #number of sides
trailSize = 5 #how long the tail is

screen = turtle.Screen()
screen.screensize(2000,1500)
screen.bgcolor('black')
screen.tracer(0,0)

iterator = 1 #how far turtle moves each time


allPoints = [[random.randint(-750,750),random.randint(-400,400)] for i in range(n)]
# allPoints = [[400,400],[400,-400],[-400,-400],[-400,400]] - square
newPoints = []

theta = 0 #changes rgb functions color

def r(x):
    return int(255/2*(sin(x/255)+1))
def g(x):
    return int(255/2*(sin((x/255)+(2/3*pi))+1))
def b(x):
    return int(255/2*(sin((x/255)+(pi*4/3))+1))

bigCount = 0
smallCount = 0
erasePoints = allPoints[:]
p = (int(1/iterator)+1)*trailSize*5*2
while True:

    for i in range(len(allPoints)):
        if bigCount > p:
            erase.up()
            erase.setpos(tuple(erasePoints[smallCount]))
            targetPointe = erasePoints[smallCount+1]

            erase.seth(erase.towards(tuple(targetPointe)))
            erase.down()
            erase.forward(iterator)
            smallCount += 1

        if i == len(allPoints)-1:
            targetPoint = allPoints[0]
        else:
            targetPoint = allPoints[i+1]
        draw.up()
        draw.setpos(tuple(allPoints[i]))
        draw.seth(draw.towards(tuple(targetPoint))) #look towards target point
        draw.down()
        draw.pencolor((r(theta),g(theta),b(theta)))
        draw.forward(iterator)
        newPoints.append(list(draw.pos()))
        turtle.update()

    theta += 3*iterator
    if bigCount > 0:
        erasePoints.extend(allPoints)
    bigCount += 1
    allPoints = newPoints[:]
    newPoints = []
