#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_hourglass = -math.inf
    for i in range(4):
        for x in range(4):
            hourglass_sum = sum(arr[i][x:x+3]) + arr[i+1][x+1] + sum(arr[i+2][x:x+3])
            if hourglass_sum > max_hourglass:
                max_hourglass = hourglass_sum
    return max_hourglass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
