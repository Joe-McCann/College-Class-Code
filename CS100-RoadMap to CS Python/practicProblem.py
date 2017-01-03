import turtle

def square(t, s):
    for i in range(4):
        t.fd(s)
        t.right(90)

def multSquares(pen, initLength, incr, num, angle):
    pen.down()
    for i in range(num):
        square(pen, initLength+i*incr)
        pen.right(angle)

myT = turtle.Turtle()
screen = turtle.Screen()
myT.speed(0)
myT.up()
myT.goto(80,120)
myT.setheading(-45)
multSquares(myT, 50, 20, 40, 15)
screen.exitonclick()

#Stop creeping on me priya 
