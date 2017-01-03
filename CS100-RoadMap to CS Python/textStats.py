def textStats(text):
    lines = text.split("\n")
    count = []
    for i in lines:
        words = i.split()
        hold = []
        for j in words:
            if (j not in hold):
                hold.append(j)
        count.append(len(hold))
    return count

print(textStats("a a a b b b c c c d d d \n a a a b b b"))
        
