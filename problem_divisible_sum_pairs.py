import math
import os
import random
import re
import sys

n = 6
k = 3
ar = [1,3,2,6,1,2]
exp_res = 5


# Method, which will compare each pair from the list and check, if they are divisble by k.
def divisibleSumPairs(n, k, ar):
    index1 = 0
    counter = 0
# Loop which will sum each possible pair in the list
    while index1 != n-1:
        index2 = index1 + 1
        while index2 != n:
            sum = ar[index1] + ar[index2]
# Only divisble pairs are counted
            if sum % k == 0:
                counter += 1
            index2 += 1
        index1 += 1
    return counter

#Control print
print(divisibleSumPairs(n, k, ar))

#Test of result
if divisibleSumPairs(n, k, ar) == exp_res:
    print("expected result match",divisibleSumPairs(n, k, ar), " = ", exp_res)
else:
    print("expected result doesn't match")

input()
