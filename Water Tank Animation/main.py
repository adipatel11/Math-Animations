import turtle
t = turtle.Turtle()
t.ht()
t.up()
t.clear()
screen = turtle.Screen()
turtle.tracer(0,0)
screen.title('Water Tank System')
screen.setup(width=600,height=600)
t.color('black')
def chx(a):
    t.goto(t.xcor()+a,t.ycor())

t.goto(-300,230)   #first pipe
t.down()
t.pensize(2)
t.seth(90)
chx(150)
t.back(70)
t.up()
chx(-30)
gutx = t.xcor()
guty = t.ycor()
t.goto(-300,200)
t.down()
chx(120)
t.back(40)
pipe1x = t.xcor()
pipe1y = t.ycor()

t.up()              #creating the box 
t.goto(-300,230)
chx(75)
t.down()
t.back(30)
chx(-30)
t.forward(30)
t.seth((360+270)/2)
t.forward(30*(2**0.5))
t.seth(90)
t.forward(30)
t.seth((180+270)/2)
t.forward(30*(2**0.5))

t.up()                  
t.goto(-300,230)          #make coral button
t.seth(90)
chx(60)
t.down()
t.forward(20)
t.color('coral')
chx(20)
chx(-40)
temphead = 89
t.begin_fill()
for i in range(62):
    temphead = temphead - 2.8
    t.seth(temphead)
    t.forward(1)

t.end_fill()
t.color('black')


t.up()              #make first box
t.goto(gutx,guty)
t.seth(90)
t.back(150)
chx(15)
t.down()
chx(60)
chx(-120)
t.forward(80)
t.back(80)
chx(120)
t.forward(25)
t.up()
t.forward(30)
t.down()
t.forward(25)

 
t.up()           #second pipe
tempx = t.xcor()
tempy = t.ycor()
t.back(25)
t.down()
chx(100)
t.up()
t.back(30)
t.down()
chx(-100)

chx(35)      #second box and button
chx(30)
t.forward(30)
chx(-30)
t.back(30)
t.seth(45)
t.forward(30*(2**0.5))
chx(-30)
t.seth((360+270)/2)
t.forward(30*(2**0.5))
chx(-65)
t.seth(90)
t.up()
t.forward(30)
t.down()
chx(50)
t.forward(20)
t.color('coral')
chx(-20)
temphead = 89
t.begin_fill()
for i in range(63):
    temphead = temphead - 2.8
    t.seth(temphead)
    t.forward(1)

t.end_fill()
t.color('black')


t.seth(90)         #finish second pipe
t.up()
t.goto(tempx,tempy)
t.down()
t.back(25)
chx(150)
chx(-150)
t.up()
t.back(30)
t.down()
chx(120)
t.back(30)
pipe2x = t.xcor()
pipe2y = t.ycor()
t.up()
t.goto(tempx,tempy)
t.back(25)
chx(150)
t.down()
t.back(60)



t.up()     #last box
chx(-30)
gut2x = t.xcor()
gut2y = t.ycor()
chx(15)
t.back(150)
t.down()
chx(-60)
t.forward(80)
t.back(80)
chx(120)
t.forward(80)











                    
                    
turtle.update()
clickcount = 0
d = turtle.Turtle()
d.ht()
d.clear()
d.pensize(2)
d.seth(90)


v = turtle.Turtle()
v.ht()
v.clear()
v.seth(90)
v.pensize(2)

e = input('Click enter for first pipe. ')
print()
del e
d.up()
d.goto(pipe1x,pipe1y)
d.color('teal')
d.down()
while d.ycor() != (pipe1y - 150): #first stream
    d.begin_fill()
    d.goto(d.xcor()+30,d.ycor())
    d.back(1)
    d.goto(d.xcor()-30,d.ycor())
    d.forward(1)
    d.end_fill()
    d.back(1)
    turtle.update()

v.up()
v.goto(d.xcor(),d.ycor())
v.color('teal')
v.down()
while v.ycor() != pipe1y: #copy stream
    v.begin_fill()
    v.goto(v.xcor()+30,v.ycor())
    v.forward(1)
    v.goto(v.xcor()-30,v.ycor())
    v.back(1)
    v.end_fill()
    v.forward(1)

h = turtle.Turtle()
h.ht()
h.clear()
h.pensize(2)
h.color('teal')   
h.up()              
h.goto(gutx,guty)
h.seth(90)
h.back(150)
h.goto(h.xcor()+15,h.ycor())
h.goto(h.xcor()-59,h.ycor())
for i in range(60):   #box fills with water
    h.down()
    h.begin_fill()
    h.forward(1)
    h.goto(h.xcor()+118,h.ycor())
    h.back(1)
    h.end_fill()
    h.forward(1)
    h.goto(h.xcor()-118,h.ycor())
    if i > 37:
        d.clear()
        for i in range(60):
            v.undo()        #delete copy stream for effect
    turtle.update()



turtle.update()


e = input('Click enter for the second pipe. ')  #SECOND BOX AND PIPE
del e
v.clear()
d.up()
d.goto(pipe2x,pipe2y)
d.color('teal')
d.down()
while d.ycor() != (pipe2y - 150): #first stream
    d.begin_fill()
    d.goto(d.xcor()+30,d.ycor())
    d.back(1)
    d.goto(d.xcor()-30,d.ycor())
    d.forward(1)
    d.end_fill()
    d.back(1)
    turtle.update()
    for a in range(2):
        h.undo()

v.up()
v.goto(d.xcor(),d.ycor())
v.color('teal')
v.down()
while v.ycor() != pipe2y: #copy stream
    v.begin_fill()
    v.goto(v.xcor()+30,v.ycor())
    v.forward(1)
    v.goto(v.xcor()-30,v.ycor())
    v.back(1)
    v.end_fill()
    v.forward(1)
        
t.color('teal')   
t.up()              
t.goto(gut2x,gut2y)
t.seth(90)
t.back(150)
chx(15)
chx(-59)
for i in range(60):      #box fills with water
    for a in range(2):
        h.undo()
    t.down()
    t.begin_fill()
    t.forward(1)
    chx(118)
    t.back(1)
    t.end_fill()
    t.forward(1)
    chx(-118)
    if i > 37:
        d.clear()
        for i in range(60):
            v.undo()        #delete copy stream for effect
    turtle.update()




turtle.update()
    




        
