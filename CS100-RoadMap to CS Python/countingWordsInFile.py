def wordStats(infile, outfile):
    rfile = open(infile, 'r')
    wfile = open(outfile, 'w')
    text = rfile.read().lower().split()
    for i in set(text):
        wfile.write(i+" "+str(text.count(i)) +'\n')
    rfile.close()
    wfile.close()

wordStats("input.txt", "output.txt")
    
