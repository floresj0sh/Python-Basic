#Josh Flores
#06/15/2022
#assign4-1

import sys
import math

hours = int(sys.argv[1])
rate = int(sys.argv[2])

def computepay(hours, rate):
    reg = 0
    if hours <= 40:
        reg = hours * rate

    else:
       
        reg = (40 * rate) + (((hours - 40) * rate) * 1.75)
    return reg
print('Your gross pay is', '$'+str(computepay(hours,rate)))

