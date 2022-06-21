#Josh Flores
#06/2/2022
#assign3.3

import sys
import math

grade = float(sys.argv[1])
if grade < 0 or grade > 1:
    print("Error")
    
else:
    if grade >= .9:
        print('The letter grade is A')
    elif grade >= .8 < .89:
        final = 'B'

    elif grade >= .7 < .79:
        final = 'C'
        
    elif grade >= .6 < .69:    
        final = 'D'

    elif grade < .6:
        final = 'F'
    print('The letter grade is', final)