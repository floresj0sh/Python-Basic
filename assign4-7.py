#Josh Flores
#06/16/2022
#assign4-7


import sys

number = int(sys.argv[1])

def isOdd(number):
   if number%2!=0:
       print(number, 'is an odd number'.format(number))
   else:
       print(number,'is not an odd number'.format(number))
       
isOdd(number)
