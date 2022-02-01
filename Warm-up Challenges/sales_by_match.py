#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    uniques = set(ar)

    pair_of_socks = 0
    for u in uniques:
        counter = 0
        for i in ar:
            if u == i:
                counter += 1
        if counter > 1:
            if counter % 2 != 0:
                counter -= 1
            pair_of_socks += int(counter / 2)

    return pair_of_socks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
