file = open("firstWrite.txt", "w")
for i in range(1, 101):
    file.write(str(i) + "\n")
file.close()
