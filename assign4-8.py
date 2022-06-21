#Josh Flores
#06/16/2022
#assign4-8


def calcavg(g1,g2,g3,g4,g5):

  try:

    return (g1+g2+g3+g4+g5)/5

  except ValueError:

    return -1

def getletter(avg):

  if avg>=90:

    return "A"

  if avg>=80:

    return "B"

  if avg>=70:

    return "C"

  if avg>=60:

    return "D"

  return "F"

def printresults(avg,grade):

  print("Averagae: ",avg)

  print("Letter grade: ",grade)

avg=calcavg(56 ,70 ,80 ,99 ,66)

if(avg==-1):

  print("Error, all grades must be numeric.")

else:

  g=getletter(avg)

  printresults(avg,g)