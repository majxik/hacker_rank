import math
import os
import random
import re
import sys

#read input comment for testing
#n = int(input().strip())

test_arr = [[1,"Weird"],[2,"Not Weird"],[3,"Weird"],[4,"Not Weird"],[5,"Weird"],[6,"Weird"],[20,"Weird"],[22,"Not Weird"]]

def decide(n):
    if n % 2 == 1:
        print("Weird")
        return("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
            return("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
            return("Weird")
        elif n > 20:
            print("Not Weird")
            return("Not Weird")

#Automated test for test_arr collection
for test in test_arr:
    n = test[0]
    print(decide(n) == test[1])


input()
