#Imports as they are in original code
import math
import os
import random
import re
import sys

#Test Values
meal_cost = 10.25
tip_percent = 17
tax_percent = 5

#Methode itself
def solve(meal_cost, tip_percent, tax_percent):
#Calculation, itself it will not work without proper rouding
    final_price = meal_cost + (meal_cost * (tip_percent/100)) + (meal_cost * (tax_percent/100))
#round() is not rounding as you are used to from school, so some extra effort is needed for rounding.
    if (float(final_price ) % 1) >= 0.5:
        receipt_price = math.ceil(final_price)
    else:
        receipt_price = round(final_price)
    print (int(receipt_price))

#It is working?
solve(meal_cost, tip_percent, tax_percent)

input()
