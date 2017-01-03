import turtle
from random import randint

def heart(t, size, x, y):
    t.up()
    t.goto(x,y)
    t.down()
    t.color("pink")
    t.begin_fill()
    t.setheading(45)
    t.circle(size, 180)
    t.right(90)
    t.circle(size,180)
    t.forward(size*2)
    t.left(90)
    t.forward(size*2)
    t.end_fill()
    t.up()
    t.goto(x - size * .707, y)
    t.down()
    t.color("black")
    t.write("I love Piya bae", align = 'right')

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
screen.bgcolor("black")

for i in range(200):
    heart(t, randint(10, 100), randint(0,1400) - 700, randint(0, 1400)-700)

screen.exitonclick()
