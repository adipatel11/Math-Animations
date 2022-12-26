#hilbert curve

#imports

import turtle
from math import *

#setup drawer

turtle.tracer(0,0)
d = turtle.Turtle()
d.ht()
d.pensize(0.5)
d.color('red')


#setup screen

screen = turtle.Screen()
screen.bgcolor('black')
screen.screensize(2000,1500)


# starting_fractal_string
starting_fractal_string = "11"

fractal_string = ""

def complement(x):
    new = ""
    for i in x:
        if i == "1":
            new += "0"
        elif i == "0":
            new += "1"
        else:
            new += "3"
    return new
    
def genStr(fs):
    frac = fs
    for iterations in range(2,10):
        if iterations%2 == 0:
            frac = complement(frac) + "13" + frac + "00" + frac + "31" + complement(frac)
        else:
            frac = complement(frac) + "31" + frac + "33" + frac + "13" + complement(frac)

    return frac


fractal_string = genStr(starting_fractal_string)

# "fractal_string" variable stores the generating sequence

d.up()
d.goto(-200,-360)
d.down()
d.seth(90)
d.forward(5)


def r(x):
    return int(255/2*(sin(x/255)+1))
def g(x):
    return int(255/2*(sin((x/255)+(2/3*pi))+1))
def b(x):
    return int(255/2*(sin((x/255)+(pi*4/3))+1))

x = 0
screen.colormode(255)

for i in fractal_string:
    if i == "1":
        d.right(90)
    if i == "0":
        d.left(90)
    for color_change in range(5):
        d.forward(1)
    d.color(r(x),g(x),b(x))
    x += 1
    turtle.update()


print('done')
while(True):
    turtle.exitonclick()















