import sys


input = []

for line in sys.stdin:
    input.append(line)

N1 = input[0].split("\n")
N = int(N1[0])

farm = [[0] * 1000] * 1000


def getcows(N):
    rv = []
    i = 0
    while(i < N):
        cow1 = input[i+1].split(" ")
        coor = cow1[2].split("\n")
        cow1[2] = int(coor[0])
        cow1[1] = int(cow1[1])
        rv.append(cow1)
        i = i +1

    return rv

def addCow(cows):
            if(cows[0][0] == 'E'):
                if(farm[(cows[0][1]) + 1][(cows[0][2])] == 2):
                 cows[0][1] = cows[0][1] + 1
            elif(cows[0][0] == 'N'):
                if(farm[(cows[0][1])][(cows[0][2])+ 1] == 2):
                    cows[0][2] = cows[0][2] + 1


cows1 = getcows(N)
k = 0

while(k < 100):
    addCow(cows1)
    k = k + 1

for cow in cows1:
    if(cow[1] > 100 or cow[2] > 100):
        print("Infinity")
    else:
        print(cow[2])