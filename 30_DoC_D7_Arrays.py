import math
import os
import random
import re
import sys

#we dont need first input from automat
input()
#reading list of numbers to insert them to list named array
array = [int(x) for x in input().split()]

#methode for reversing list and print it delimited by space
def arrayBackwards(array):
    reverse_array = list(reversed(array))
    print (" ".join(str(y) for y in reverse_array))

arrayBackwards(array)

input()
