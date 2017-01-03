def wordStats(name1, name2, freqRange):
    rfile = open(name1, 'r')
    wfile = open(name2, 'w')
    fileCont = rfile.read()
    words = set(fileCont.split())
    lines = fileCont.split("\n")
    for word in words:
        for freq in range(freqRange):
            lnlst = []
            count = 0
            for line in lines:
                print(line)
                if line.count(word) == freq:
                    lnlst.append(count)
                count+=1
            wfile.write(word + " " + str(freq) + " " + str(lnlst) + "\n")
    rfile.close()
    wfile.close()

wordStats("text.txt", "wat.txt", 3)
