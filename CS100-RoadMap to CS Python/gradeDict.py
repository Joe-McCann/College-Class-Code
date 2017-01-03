grades = [95, 96, 97, 99, 100, 99, 95, 95]
gdic = {}

for i in grades:
    if i in gdic:
        gdic[i] += 1
    else:
        gdic[i] = 1

print(gdic)
