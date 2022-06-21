#Josh Flores
#05/26/2022
#assign2-3

import sys
import math

number1 = int(sys.argv[1])
number2 = float(sys.argv[2])

print('Number1 is', number1)
print()
print('Number2 is', number2)
print()

value1 = number1 / 2
value2 = number1 / number2
value3 = number1 * number2
value4 = 3 ** number2

print(str(number1) + '//2','=', round(value1, ), type(number1))
print()
print(str(number1) + '/', number2, '=', round(value2, 11), type(value2))
print()
print(str(number1) + '*', number2, '=', round(value3, 0), type(value3) )
print()
print("3**"+str(number2), '=', round(value4, 1), type(value4))