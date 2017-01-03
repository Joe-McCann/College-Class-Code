scores = open("scoresFile.txt", "r")
'''for i in scores:
    text = i.split()
    print(text[1])
'''
#s = scores.read()
#print(s)
#print(len(s.split()))
lst = scores.readlines()
print(lst)
scores.close()
