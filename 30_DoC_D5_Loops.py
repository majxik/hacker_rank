import math
import os
import random
import re
import sys


#Get input from user
n = int(input())

#Methode, which will compute and print multiplication of entered number * [1..10] = result
def smallMultiples(n):
    index = 1
    while index < 11:
        result = n * index
        print(n,"x",index,"=",result)
        index += 1

#Lets run methode
smallMultiples(n)

#Soft pause
input()
