#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices = sorted(prices)
    prices_cum_sum = []
    prices_cum_sum.append(prices[0])
    [prices_cum_sum.append(p + prices_cum_sum[-1]) for p in prices[1:]]
    for idx, p in enumerate(prices_cum_sum):
        if p > k:
            return idx



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    n = 5

    # k = 50
    k = 15

    # prices = [1, 12, 5, 111, 200, 1000, 10]
    prices = [3, 7, 2, 9, 4]

    result = maximumToys(prices, k)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
