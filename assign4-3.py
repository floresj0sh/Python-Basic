#Josh Flores
#06/15/2022
#assign4-3

import random
import math

def powRand():
    base = random.randint(1,10)
    exponent = random.randint(1,10)
    return str(base)+" power "+str(exponent)+" is "+str(int(math.pow(base, exponent)))
print(powRand())