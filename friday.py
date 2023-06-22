"""
ID: madhav52
LANG: PYTHON3
TASK: friday

"""
import math

fin = open('C:/Users/Vish/PycharmProjects/USACO/friday.in', 'r')
fout = open('C:/Users/Vish/PycharmProjects/USACO/friday.out', 'w')

for line in fin:
    n = line

n = int(n) + 1900

def makeYear(year):
   rv = [31,28,31,30,31,30,31,31,30,31,30,31]
   if year % 100 == 0:
       if year % 400 == 0:
           rv[1] = 29
   elif year % 4 == 0:
       rv[1] = 29
   return rv

days = [1,2,3,4,5,6,7]  #where the int represents day of the week strating with monday

frv = []

frv.append((days * (int)(31 / 7) + days[0:(int)(31 % 7)]))

def daysInMonth(year):
    daysPerMonth = makeYear(year)
    i = ((year - 1900) * 12)
    j = 0
    if(year == 1900):
        i = 1
        j = 1

    while j < len(daysPerMonth):
      frv.append(days[frv[i-1][len(frv[i-1]) - 1] : 7] + days * (int)((daysPerMonth[i % 12] / 7) - 1) + days[0 : daysPerMonth[i % 12] - 21 - len(days[frv[i-1][len(frv[i-1]) -1] : 7]) ])
      if(len(frv[len(frv)-1]) < daysPerMonth[i % 12]):
          frv[len(frv) - 1] += days[0:daysPerMonth[i % 12] - len(frv[len(frv)-1])]
      j = j + 1
      i = i + 1


j = 1900

ctrSat= 0
ctrSun = 0
ctrMon = 0
ctrTue= 0
ctrWed =0
ctrThr =0
ctrFri = 0


while(j < n):
    daysInMonth(j)
    j = j +1


for month in frv:
    if month[12] == 1:
        ctrMon += 1
    elif month[12] == 2:
        ctrTue += 1
    elif month[12] == 3:
        ctrWed += 1
    elif month[12] == 4:
        ctrThr += 1
    elif month[12] == 5:
        ctrFri += 1
    elif month[12] == 6:
        ctrSat += 1
    elif month[12] == 7:
        ctrSun += 1

print(frv[276:288])

fout.write(str(ctrSat) + " ")
fout.write(str(ctrSun)+ " ")
fout.write(str(ctrMon)+ " ")
fout.write(str(ctrTue)+ " ")
fout.write(str(ctrWed)+ " ")
fout.write(str(ctrThr)+ " ")
fout.write(str(ctrFri) + "\n")
fout.close()
