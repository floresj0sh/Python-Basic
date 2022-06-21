#Josh Flores
#06/19/2022
#assign4-12

import sys

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
number3 = int(sys.argv[3])
number4 = int(sys.argv[4])
number5 = int(sys.argv[5])


def calstats(number1,number2,number3,number4,number5):

    if number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5:
        highest = number1
    
    elif number2 > number1 and number2 > number3 and number1 > number4 and number1 > number5:
        highest = number2
    
    elif number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
        highest = number3
        
    elif number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5:
        highest = number3
    elif number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5:
        highest = number3
    else:
        highest = number5


    if number1<number2 and number1<number3 and number1 < number4 and number1 < number5:
        lowest=number1 
    
    elif number2 < number1 and number2 < number3 and number1 < number4 and number1 < number5:
        lowest = number2
        
    elif number3 < number1 and number3 < number2 and number3 < number4 and number3 < number5:
        lowest = number3
    elif number4 < number1 and number4 < number2 and number4 < number3 and number4 < number5:
        lowest = number4
    else:
        lowest = number5
    
    range1 = highest - lowest
    average = (number1 + number2 + number3 + number4 + number5)/5
    print('Min:', lowest)
    print('Max:', highest)
    print('Range:', range1)
    print('Average:', average)

calstats(number1,number2,number3,number4,number5)