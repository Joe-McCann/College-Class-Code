def stringStats(fileName):
    rfile = open(fileName, 'r')
    retList = []
    hold = []
    lines = rfile.read().lower().split("\n")
    for line in lines:
        count = 0
        for word in set(line.split()):
            if line.split().count(word) > 1:
                count += 1
        hold.append(count)
    for i in range(len(hold)):
        if hold[i] == max(hold):
            retList.append(lines[i])
    rfile.close()
    return retList

print(stringStats("text.txt"))
