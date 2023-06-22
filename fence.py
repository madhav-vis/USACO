import sys
a = []
for line in sys.stdin.readlines():
    a.append(line.split("\n")[0])

a[0] = int(a[0])


def deter(string):
    n =0
    s = 0
    w = 0
    e = 0
    word = []
    for i in range(0, len(string)):
        word.append(string[i])
    for j in range(0, int(len(word)) ):
        if(word[j] == "N"):
            n += 1
        elif(word[j] == "E"):
            e += 1
        elif (word[j] == "S"):
            s += 1
        elif (word[j] == "W"):
            w += 1
        if (e > w and n > s):
            return "CW"
        elif (e > w and n < s):
            return "CCW"
        elif (w > e and n > s):
            return "CW"
        elif (w > e and n < s):
            return "CCW"

for i in range(0, a[0]):
    print(deter(a[i+1]))