#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes_cont = 0
    for idx, value in enumerate(q[:-1]):
        diff_plus_one = q[idx] - q[idx+1]
        if diff_plus_one < 0:
            pass
        elif diff_plus_one > 3:
            return print('Too chaotic')
        else:
            bribes_cont += diff_plus_one
    return print(bribes_cont)

if __name__ == '__main__':
    # t = int(input().strip())
    t = 2
    for t_itr in range(t):
        n = 5

        # q = [2, 1, 5, 3, 4]
        q = [1, 2, 5, 3,
             7, 8, 6, 4]
        # q = [1, 2, 5,
        #      3, 4, 7,
        #      8, 6]

        minimumBribes(q)
