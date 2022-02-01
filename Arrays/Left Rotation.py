#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    return a[d:] + a[:d]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # first_multiple_input = input().rstrip().split()

    n = 5

    d = 4

    a = list(range(1, n+1))
    print(a)

    result = rotLeft(a, d)

    # fptr.write(' '.join(map(str, result)))
    #
    # fptr.write('\n')
    # fptr.close()
