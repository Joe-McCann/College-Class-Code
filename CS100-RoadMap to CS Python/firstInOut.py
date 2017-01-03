def writeData(readfile, writefile):
    rfile = open(readfile, 'r')
    wfile = open(writefile, 'w')
    for lines in rfile:
        words = lines.split()
        for j in set(words):
            wfile.write(j + " ")
        wfile.write("\n")
    rfile.close()
    wfile.close()

writeData("in.txt", "out.txt")
