#Josh Flores
#06/16/2022
#assign4-5

import sys

inches = int(sys.argv[1])

def inch2cm(inches):
    cm = inches * 2.54
    return cm
    
print(inches, 'inches =',inch2cm(inches), 'centimeter' )