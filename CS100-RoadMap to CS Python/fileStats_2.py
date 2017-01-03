def fileStats(inFile, outFile):
    rfile = open(inFile, "r")
    wfile = open(outFile, 'w')
    lines = rfile.read().split('\n')
    output = {}
    for line in range(len(lines)):
        words = lines[line].split()
        for j in set(words):
            if j in output:
                output[j].append(line+1)
            else:
                output[j] = [line+1]
    for key in output:
        wfile.write(key + ": " + ",".join(str(i) for i in output[key]) + '\n')
    wfile.close()
    rfile.close()


fileStats("infileStats_2.txt", "outfileStats_2.txt")
    
