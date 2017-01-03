import turtle
from random import randint

def randPoly(iterations, pen):
    print("Hello World")
    pen.down()
    angle = randint(10,170)
    for i in range(iterations):
        col = (randint(0,128),randint(0,128),randint(0,128))
        pen.pencolor(col)
        fd((iterations // 100)*100 + 100)
        left(angle)

pen = turtle.Turtle()
screen = turtle.Screen()
#screen.bgcolor("black")

randPoly(1000, pen)
