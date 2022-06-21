#Josh Flores
#06/15/2022
#assign4-4

import sys
import math

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

def calc(num1, num2, num3):
    formula = math.sqrt((num1 + num2 ** 2 + num3 ** 3))
    return round(formula, 2)

print(calc(num1, num2, num3))