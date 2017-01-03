def totalAs(scoreList):
    amtA = 0
    for i in scoreList:
        if i >= 90:
            amtA += 1

    return amtA

scores = [90, 89, 91, 79]
print(totalAs(scores))
