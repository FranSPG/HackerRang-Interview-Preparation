#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = 0
    valley_counter = 0

    for i, step in enumerate(path[:-1]):
        if (level == 0) and (path[i] == 'D'):
            valley_counter += 1
        if step == 'U':
            level += 1
        else:
            level -= 1

        print(f"Level: {level}\tStep: {step}\tNext step: {path[i+1]}\tValley counter: {valley_counter}\tNumber: {i+1} of {len(path)}")

    return valley_counter


if __name__ == '__main__':

    steps = 8

    path = "DDUUDDUDUUUD"

    result = countingValleys(steps, path)

    print(result)