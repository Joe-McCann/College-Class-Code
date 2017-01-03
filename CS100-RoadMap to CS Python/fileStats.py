def fileStats(filename):
    file = open(filename, 'r')
    wordFreq = {}
    lines = file.read().split("\n")
    for i in range(len(lines)):
        words = lines[i].split()
        freq = {}
        wordFreq[i+1] = []
        for j in set(words):
            if words.count(j) in freq:
                freq[words.count(j)].append(j)
            else:
                freq[words.count(j)] = [j]
        wordFreq[i+1] = freq[max(freq)]
    file.close()
    return wordFreq

f = open('stuff.txt', 'r')
print(f.readline())

    
    
