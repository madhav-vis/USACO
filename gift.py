"""
ID: madhav52
LANG: PYTHON3
TASK: gift1

"""
import math

giftin = open('gift1.in', 'r')
giftout2 = open('gift1.out', 'w')

NP = 0

input = []
people = {}

for line in giftin:
    input.append(line)

NP = int(input[0])

def names(arr):
    i = 0
    while(i < NP):
        ev = arr[i+1].split("\n")
        people[ev[0]] = 0
        i = i +1

def amountSplit(num1):
    rv = []
    rv = num1.split("\n")
    rv1 = rv[0].split(" ")
    rv2 = [(int)(rv1[0]), (int)(rv1[1])]
    if rv2[1] == 0:
      rv3 = [0,0,0,0]
    else:
     rv3 = [int(rv2[0] / rv2[1]), rv2[0] - int(int(rv2[0] / rv2[1]) * rv2[1]), (int)(rv1[0]),(int)(rv1[1]) ] # amount that goes to each person, left over for giver, original amount, num of people to split
    return rv3

def update(arr):
    name15 = arr[0].split("\n")
    name1 = name15[0]
    rv = amountSplit(arr[1])
    nump = rv[3]
    if name1 in people:
        people[name1] = people[name1] + rv[1] - rv[2]
    j = 0
    while(j < nump):
         name25 = arr[j+2].split("\n")
         name2 = name25[0]
         people[name2] = people[name2] + rv[0]
         j = j + 1


i = NP + 1

arrt = input
names(input)
while( i < len(input)):
    num7 = amountSplit(input[i+1])
    arrt = input[i:i+num7[3]+2]
    update(arrt)
    i = i + num7[3] + 2

print(people)

e = 0

while(e < len(people)) :
    res = list(people.keys())[e]
    giftout2.write(str(res) + " " + str(people[str(res)]) + "\n")
    e = e + 1

giftout2.close()



