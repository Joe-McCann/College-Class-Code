import turtle

def tri(t, sidelen):
    t.down()
    for i in range(3):
        t.fd(sidelen)
        t.left(120)

def tris(t, initial, incr, num, angle):
    for i in range(num):
        tri(t, initial + incr * i)
        t.left(angle)

def wordsByLine(inFile, outFile):
    rfile = open(inFile, 'r')
    wfile = open(outFile, 'w')
    lines = rfile.read().split("\n")
    for line in lines:
        words = line.split()
        for word in set(words):
            wfile.write(word + ":" + str(words.count(word)) + " ")
        wfile.write("\n")
    wfile.close()
    rfile.close()

def lineIndex(fname):
    rfile = open(fname, 'r')
    lines = rfile.read().split("\n")
    output = {}
    for line in lines:
        words = line.split()
        for word in set(words):
            if word in output:
                output[word].append(lines.index(line))
            else:
                output[word] = [lines.index(line)]
    return output

print(lineIndex("fish.txt"))
        
            
