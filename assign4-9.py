#Josh Flores
#06/19/2022
#assign4-9

import sys
import math

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    e = int(sys.argv[5])

except:
    print('Error, all grades must be numeric.')
    quit()

def calcavg(a,b,c,d,e):
    avg = (a+b+c+d+e)/5
    return avg
avg = calcavg(a,b,c,d,e)

def getletter(avg):
    if(avg>=90):
        return "A"
    elif(avg>=80):
        return "B"
    elif(avg>=70):
        return "C"
    elif(avg>=60):
        return "D"
    elif(avg<60):
        return "F"
grade = getletter(avg)
def printresults(avg, grade):
    print('Average:',avg)
    print('Letter grade:',grade)
    avg = getletter(avg)
    
printresults(avg, grade)
