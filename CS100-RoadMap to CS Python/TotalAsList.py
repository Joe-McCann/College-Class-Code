def totalAs(scorelist):
    As = []
    for i in scorelist:
        if i >= 90:
            As.append(i)

    return As

print(totalAs([10, 20, 90, 99, 45, 96, 93]))
            
