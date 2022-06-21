#Josh Flores
#06/15/2022
#assign4-2

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

def isDivisible(x, y):
    if x % y == 0:
        print(x, 'is divisible by', str(y)+".")
    else:
        print(x, 'is not divisile by', str(y)+".")
isDivisible(x, y)