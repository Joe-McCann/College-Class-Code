import turtle
'''
def equalSign(t, length):
    t.down()
    x = t.xcor()
    y = t.ycor()
    theta = t.heading()
    t.fd(length)
    t.goto(x, y)
    t.setheading(theta)
    t.up()
    t.right(90)
    t.fd(length/2)
    t.pd()
    t.left(90)
    t.fd(length)
    t.up()
    t.goto(x, y)
    t.setheading(theta)

def equalSigns(t, size, spacing, num):
    for i in range(num):
        equalSign(t, size)
        t.fd(size+spacing)

t = turtle.Turtle()
s = turtle.Screen()
t.left(43)
equalSigns(t, 30, 15, 6)
    '''
#############

def vowelCount(word):
    lword = word.lower()
    vowels = lword.count("a")+lword.count("e")+lword.count("i")+lword.count("o")+lword.count("u")
    return vowels

s = "I am the Walrus"
v = vowelCount(s)
print(v)


##############

def getInitials(remark):
    first = input("What is your first name? ")
    last = input("What is your last name? ")
    print(remark, first, last)
    return (first[0]) + last[0]

ini = getInitials("yo wazzup")
print(ini)

