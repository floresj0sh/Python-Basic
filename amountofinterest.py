#Josh Flores
#05/24/2022
#assign1-4

import sys
import math

#variables
loan = float(sys.argv[1])
rate = float(sys.argv[2])
number_payments = float(sys.argv[3])
years = float(sys.argv[4])



#formula for interest calculation
A = loan * (1 + rate / (100 * number_payments)) ** (number_payments * years)

total = A - loan

print('Interest paid:', round(total, 1))
