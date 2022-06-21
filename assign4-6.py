#Josh Flores
#06/16/2022
#assign4-6

import sys
import math

shape = sys.argv[1]
area = int(sys.argv[2])

def shapes(shape, area):
    shape = None
    
    if shape == "square":
        formula = areaSquare
        print('The square are is' , areaSquare(area)
    else:
        formula = areaCircle
        print('The circle area is',areaCircle(area)

        
def areaSquare(area):
    square = area **2

def areaCircle(area):
    circle = math.pi * area **2
    
shapes(shape, area)