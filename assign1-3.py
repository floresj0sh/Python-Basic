#Josh Flores   
#05/24/2022
#assign1-3

import math
import sys

#variavles
name = sys.argv[1]
height = int(sys.argv[2])
weight = int(sys.argv[3])

#formula
first = height * height

second = weight / first

third = second * 703


print(name,'\'s','BMI is',round(third, 2)) 


