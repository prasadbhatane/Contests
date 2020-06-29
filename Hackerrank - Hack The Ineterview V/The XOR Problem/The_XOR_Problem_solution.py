#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxXorValue' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING x
#  2. INTEGER k
#

def maxXorValue(x, k):
    # Write your code here
    st = ''
    for i in x:
        if i == '1' or k == 0:
            st += "0"
        elif k != 0:
            st += '1'
            k -= 1
    return st

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        y = maxXorValue(s, k)

        fptr.write(y + '\n')

    fptr.close()
