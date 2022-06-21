#Josh Flores
#05/26/2022
#assign3-2

import sys
import math

try:
    hours = int(sys.argv[1])
    rate = int(sys.argv[2])
except:
    print('Error, please enter numeric input')
    quit()
    
if hours <= 40:
    reg = hours * rate
    print('Your gross pay is', reg)
if hours > 40:
    #OT calculator
    OT = (40 * rate) + (((hours - 40) * rate) * 1.75)
    print('Your gross pay is', OT)
    
