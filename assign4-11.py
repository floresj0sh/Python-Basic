#Josh Flores
#06/19/2022
#assign4-11

import sys
import math

#variables
principle = int(sys.argv[1])
rate = float(sys.argv[2])
number_payments = int(sys.argv[3])
years = int(sys.argv[4])



def calcinterest(principle, rate, number_payments, years):
    interest = principle * (1 + rate / (100*number_payments))**(number_payments*years)

    total = interest - principle
    
    return total
interest = round(calcinterest(principle, rate, number_payments, years), 1)

print('Interest Paid:', "$"+str(interest))