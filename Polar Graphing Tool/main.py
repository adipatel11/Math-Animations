import turtle
from math import *
turtle.tracer(0,0)
def r(theta):
    t = radians(theta)
    return cos(4*t)

#setup
screen = turtle.Screen()
screen.title('Polar Graphing Tool')
d = turtle.Turtle() #draw tool
d.speed(0)
d.hideturtle()
screen = turtle.Screen()
screen.screensize(2000,1500)
screen.bgcolor('Black')

d.color('antique white') #axis
d.up()
d.goto(-350, 200)
d.down()
d.write('r = cos(4θ)', False, align='left', font = ('arial',28, 'bold'))
d.up()
d.home()
d.down()
d.forward(1000)
d.backward(2000)
d.forward(1000)
d.seth(90)
d.forward(750)
d.backward(1500)
d.seth(0)
d.home()
d.color('green')

###
iterator = 10**-1

theta = 0
scale = 120
x = 0

while(theta<360):  # draw graph
    d.up()
    d.goto(scale*r(theta)*cos(radians(theta)),scale*r(theta)*sin(radians(theta)))
    d.down()
    d.dot(3)
    theta += iterator
    turtle.update()

print('Done')
d.up()
while(True):
    try:
        turtle.exitonclick()
    except:
        break
    





