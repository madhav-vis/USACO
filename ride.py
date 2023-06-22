"""
ID: madhav52
LANG: PYTHON3
TASK: ride
"""
inputnum = []
filein = open ('ride.in', 'r')
fileout = open ('ride.out', 'w')
with filein:
    for count, line in enumerate(filein):
        inputnum.append(line)
ar1 = str(inputnum[0])
ar2 = str(inputnum[1])
def alphaNum(ar):
    output = []
    for character in ar:
        num = ord(character) - 64
        output.append(num)
    return output
def calc(ar):
    total = ar[0]
    for x in range(1,len(ar)):
        total = total * ar[x]
    return total%47
ar1 = calc(alphaNum(ar1))
ar2 = calc(alphaNum(ar2))
if ar1 == ar2:
    fileout.write("GO" + "\n")
else:
    fileout.write("STAY" + "\n")
fileout.close()