import turtle
import random
import time

t = turtle.Turtle()
names = ["Joe", "Granny", "Susan", "Frankie", "Patrick", "Karen", "Reagan", "Lindsey", "Katie",
         "Kathy", "Emily", "Holly", "Annie", "Sarah", "Andrew", "Patty", "Mary", "Carmen",
         "Johnny", "Kelly", "Cody", "Ron", "Rob", "Bill", "Jackie"]
file = open("grabBag2016.txt", 'w')

def writeName(x,y):
    t.clear()
    t.color("white")
    for i in range(50):
        t.clear()
        y = random.randint(0, len(names)-1)
        t.write(names[y], align = "center", font = ("Arial", 150, "normal"))
        time.sleep(.0001*(i**2))
    t.color("red")   
    t.clear()
    x = random.randint(0, len(names)-1)
    t.write(names[x], align = "center", font = ("Arial", 150, "normal"))
    print(names[x])
    names.remove(names[x])



s = turtle.Screen()
t.ht()
s.bgcolor("black")
s.onclick(writeName)
s.listen()

