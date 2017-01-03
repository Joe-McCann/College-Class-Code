import turtle
import math

def drawAxis(t):
    t.width(3)
    t.speed(0)
    t.goto(1000, 0)
    t.goto(-1000, 0)
    t.up()
    t.goto(0, 1000)
    t.down()
    t.goto(0, -1000)
    t.width(1)
    
def graph(stepsize, rang, t, function):
    t.up()
    t.goto(rang[0], f(rang[0]))
    t.down()
    for i in range(rang[0], rang[1], stepsize):
        t.goto(i, function(i))

def f(x):
    return 100*math.cos(x/50)
def f2(x):
    return 100*math.sin(x/50)
def f3(x):
    return 100*math.tan(x/50)
def f4(x):
    return (x/40)**2
def f5(x):
    return (400*math.exp(-1*(x/400)**2))

t = turtle.Turtle()
s = turtle.Screen()

drawAxis(t)
graph(1, [-960, 960], t, f4)
t.color("red")
graph(1, [-960, 960], t, f5)

