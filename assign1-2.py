#Josh Flores
#05/23/2022
#assign2

import sys

#variables
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
number3 = int(sys.argv[3])

multi = number1 * number2

multi =  float(multi)
print(number1, '*', number2, '=', multi)

power = number2 ** number3

print(number2, 'power', number3, '=', float(power))