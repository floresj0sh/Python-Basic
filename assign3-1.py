#Josh Flores
#05/26/2022
#assign3-1

import sys
import math

hours = int(sys.argv[1])
rate = int(sys.argv[2])

if hours <= 40:
    reg = hours * rate
    print('Your gross pay is', reg)
if hours > 40:
    OT = (40 * rate) + (((hours - 40) * rate) * 1.75)
    print('Your gross pay is', OT)