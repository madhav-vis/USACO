"""
ID: madhav52
LANG: PYTHON3
TASK: beads
"""

fin = open('C:/Users/Vish/PycharmProjects/USACO/beads.in', 'r')
fout = open('C:/Users/Vish/PycharmProjects/USACO/beads.out', 'w')

arr = []

for line in fin:
    arr.append(line)

arr1 = arr[0].split("/n")
numOfBeads = int(arr1[0])

word = arr[1]
beads1 = list(word)


def Redmax(beads):
    i = 0
    j= 0
    red = 0
    red1 = 0
    while(i < numOfBeads):
        if(beads[i] == "w"):
           beads[i] = "r"
        i = i +1
    print(beads)
    while (j < numOfBeads):
        if(j + 1 > numOfBeads):
            if (beads[j+1] != "b"):
                red = red + 1
                red1 = red
        else:
            if(red1 > red ):
                red = 0
            elif(red1 < red):
                red1 = red
        j = j + 1
    return red1


print(Redmax(beads1))
