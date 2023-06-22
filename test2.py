import sys
a = []
with open("beads.in", "r") as fp:
    for line in fp:
        a.append(line.split("\n")[0])


years = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]



def oneLine(a1, ):
    a2 = a1.split(" ")
    name1 = a2[0]
    name2 = a2[-1]
    for i in range(len(years)):
        if(years[i] == a2[4]):
            if(a2[3] == "previous"):
                return 12 - i
            elif(a2[3] == "next"):
                return i

print(oneLine(a[1]))

for i in range(a[0]):
