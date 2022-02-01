#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    list_zeros = ''.join(str(x) for x in c).split('1')
    for zeros in list_zeros[:-1]:
        l_zeros = len(zeros)
        if l_zeros % 2 != 0:
            l_zeros = l_zeros - 1
        jumps += int((l_zeros/2) + 1)

    last_l_zeros = len(list_zeros[-1])
    if last_l_zeros % 2 != 0:
        last_l_zeros = last_l_zeros - 1
    jumps += int((last_l_zeros/2))

    return int(jumps)


if __name__ == '__main__':

    # n = int(input().strip())

    c = [0, 0, 1, 0, 0, 0,
         0, 1, 0, 0, 0, 0,
         1, 0, 0, 0, 0, 0,
         1, 0, 1, 0, 0, 0,
         1, 0, 0, 1, 0, 0,
         0, 1, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 0,
         1, 0, 0, 1, 0, 1,
         0, 0]


    result = jumpingOnClouds(c)

    print(result)