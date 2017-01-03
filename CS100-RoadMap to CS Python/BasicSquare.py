import turtle
'''Block comment?
'''

def drawPoly(n, length, pens):
    theta = 360/n
    pens.down()
    for i in range(n):
        pens.fd(length)
        pens.left(theta)

def drawLayers(side, t, num):
    for i in range(num):
        drawPoly(4, side, t)
        t.fd(side)

def drawPyramid(layers, t, side):
    x = t.xcor()
    y = t.ycor()
    for i in range(layers):
        drawLayers(side, t, layers - i)
        pen.up()
        pen.goto(x + side/2, y + side)
        x = t.xcor()
        y = t.ycor()
        pen.down()
    
pen = turtle.Turtle()
pen.width(1)
pen.speed(0)
pen.color("white")
screen = turtle.Screen()
screen.bgcolor("black")
pen.up()
pen.goto(-200,-200)
pen.down


'''pen.left(90)
drawLayers(50, pen, 5)

pen.up()
pen.goto(150, 0)
pen.setheading(0)
pen.left(60)
pen.down()

drawLayers(40, pen, 6)
'''

drawPyramid(6, pen, 100)
screen.exitonclick()
