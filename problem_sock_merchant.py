import math
import os
import random
import re
import sys

# Entry values
n = 9
ar = [10,20,20,10,10,30,50,10,20]
exp_res = 3

# Methode, which will count number of whole pairs of numbers
def sockMerchant(n, ar):
    counter = 0
    #extract unique values from list
    ar_unique = list(set(ar))
    #sorting mechanismus
    for sock in ar_unique:
        #if there is /2 of numbers, it count it as 1 pair
        if ar.count(sock) % 2 == 0:
            counter += int(ar.count(sock) / 2)
        #if there is odd number, it removes one, and count rest pairs
        else:
            counter += int((ar.count(sock) - 1) / 2)
    return counter

#Test of result
if sockMerchant(n, ar) == exp_res:
    print("expected result match",sockMerchant(n, ar), " = ", exp_res)
else:
    print("expected result doesn't match")

input()
