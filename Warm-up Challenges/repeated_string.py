#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    if set(s) == {'a'}:
        return n
    n_a = s.count('a')
    ratio_a_in_s = n_a * (n//len(s)) + s[: n % len(s)].count('a')
    return ratio_a_in_s


if __name__ == '__main__':

    s = 'aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce'
    n = 731869010806
    # Expected: 168329872486
    # 164281

    result = repeatedString(s, n)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
