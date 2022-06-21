#Josh Flores
#05/26/2022
#assign2-8

import sys 
import math

rad = int(sys.argv[1])

total = math.pi * (rad ** 2)

print('The area of a circle with',rad,'inches radious is', round(total, 2))