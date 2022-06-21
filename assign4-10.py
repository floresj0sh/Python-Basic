#Josh Flores
#06/19/2022
#assign4-10

import math
import sys

try:
    height = int(sys.argv[1])
    weight = int(sys.argv[2])

except:
    print('This program only takes numeric input. Program terminated.')
    quit()

def calcbmi(height, weight):
    bmi = round((weight / (height * height)) * 703, 2) 
    return bmi
bmi = calcbmi(height, weight)

def getcategory(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25 :
        return "normal"
    elif bmi < 30:
        return "obese"
category = getcategory(bmi)
print('BMI:', str(bmi)+',','and the category is', str(category)+'.' )