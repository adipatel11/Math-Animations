#dragon fractal

#imports

import turtle
from math import *

#setup drawer

turtle.tracer(0,0)
d = turtle.Turtle()
d.ht()
d.pensize(3)
d.color('red')


#setup screen

screen = turtle.Screen()
screen.bgcolor('black')
screen.screensize(2000,1500)


starting_fractal_string = "100"
fractal_string = ""
iterations = 0

def complement(string):

    resultList = ['1']*len(string)
    for i in range(len(string)):
        if string[i] == "1":
            resultList[i] = '0'
    
    resultString = "".join(resultList)
    return resultString
    
def genStr(fs):
    global iterations
    global fractal_string

    iterations += 1


    fractal_string = complement(fs[::-1]) + "0" + fs
    if iterations == 20:
        return
    genStr(fractal_string)

genStr(starting_fractal_string)
print('done')
# "fractal_string" variable stores the generating sequence

d.up()
d.goto(0,0)
d.down()
d.seth(45)
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
    d.color()
    if i == "1":
        d.right(90)
    else:
        d.left(90)
    for color_change in range(5):
        d.forward(1)
    d.color(r(x),g(x),b(x))
    x += 1
    turtle.update()


print('done')
while(True):
    turtle.exitonclick()















