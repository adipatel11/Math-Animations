import turtle
from math import *
turtle.tracer(0,0)

def f(t):
    return -7*cos(3*t)


def g(t):
    return 6*sin(2*t)

#setup

d = turtle.Turtle() #draw tool
d.speed(0)
d.hideturtle()
screen = turtle.Screen()
screen.screensize(2000,1500)
screen.bgcolor('Black')

d.color('antique white') #axis
d.forward(1000)
d.backward(2000)
d.forward(1000)
d.seth(90)
d.forward(750)
d.backward(1500)
d.seth(0)
d.up()


###
iterator = (10**-3)

num = -10
scale = 20
d.goto(scale*f(0),scale*g(0))
d.color('red')
d.down()

while(num<10):  # draw function
    num += iterator
    d.goto(scale*(f(num)),scale*(g(num)))
    turtle.update()
print('Done')

while(True):
    turtle.exitonclick()
    





