#Josh Flores
#05/26/2022
#assign2-4

import sys
import math

far = int(sys.argv[1])

f = (far - 32) * 5 / 9

print('The',far,'degree Fahrenheit is equal to', round(f, 2), 'degree Celsius.')