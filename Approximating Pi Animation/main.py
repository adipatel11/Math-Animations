import math
import time
import turtle
from datetime import datetime


def shapeCirc(sides):
  y = (180*(sides-2))/(2*sides)
  circ = 0.5*(math.cos(math.radians(y)))
  circ = 2*circ*sides
  print(circ)


def infPi(num):   #These aren't important
  denom = 1        
  pi = 0
  for i in range(num):
    if i/2 == int(i/2):
      pi += (1/denom)
    else:
      pi += (1/(0-denom))
    denom += 2
  print(pi*4)

def infPi2(num): #They aren't related to the turtle drawing
  pi = 0
  fakepi = 0
  start = time.time()
  fakepi += (1/(2*(1+1)-1)**2)
  length = (time.time()-start)*num
  print('The estimated time is ' + str(length/120) + ' minutes')
  print()
  time.sleep(2)
  start = time.time()
  starttime = datetime.now()
  print('Start time: ' + str(starttime))
  print()

  for i in range(num):
    pi += (1/(2*(i+1)-1)**2)
  print((pi*8)**0.5)
  length = (time.time()-start)
  print()
  print('It took ' + str(length/120) + ' minutes')
  print()
  print('End time: ' + str(datetime.now()))
  print()


def chx(a): #change x by amount
  t.goto(t.xcor()+a,t.ycor())

def yhx(a): #change y by amount
  t.goto(t.xcor(),t.ycor()+a)

t = turtle.Turtle()  #setting everything up
t.ht()
t.clear()
t.up()
t.pensize(2)

screen = turtle.Screen()      #setting up screen 
screen.title('Approximating Pi') 
screen.setup(width=800,height=800)
turtle.tracer(0,0)    #making no delay

radius = 150

sides = 2
while True:
  time.sleep(1.5)
  t.up()
  t.goto(0,0)
  yhx(0-radius)
  sides += 1
  t.clear()
  t.down()
  t.seth(0)
  t.color('black')
  t.circle(radius)
  t.up()
  t.goto(0,0)
  yhx(0-radius)
  angle = (180*(sides-2))/(2*sides)
  side_length = ((2*radius)/(math.tan(math.radians(angle))))
  t.down()
  t.color('blue')
  chx(side_length/2)
  chx(0-side_length)
  chx(side_length)
  heading = abs(180-(angle*2))
  t.seth(0)
  for i in range(sides):
    t.left(heading)
    t.forward(side_length)
      
  pi1 = sides*side_length


  t.color('red')
  side_length = ((2*radius)*(math.cos(math.radians(angle))))
  t.up()
  t.goto(0,0)
  t.seth(90)
  t.right((180/sides)*(sides-1))
  t.forward(radius)
  t.seth(0)
  t.down()
  for i in range(sides):
    t.left(heading)
    t.forward(side_length)

  pi4 = ''
  pi2 = sides*side_length
  pi3 = (pi2+pi1)/(radius*4)
  for i in range(8):
    pi4 = pi4 + str(str(pi3)[i])
  t.up()
  t.goto(0,0)
  yhx(0-(radius*2))
  t.down()
  t.color('black')
  t.write('π = ' + str(pi4), move = False, align='center',font=('Arial',40,'normal'))
  turtle.update()
  





