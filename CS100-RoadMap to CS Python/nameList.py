def initials(nameList):
    string = ""
    for i in nameList:
        string += i[0]
    return string

print(initials(["John", 'Steve', 'Kelly']))
