#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    kan_result = False

    while True:
        if x1 == x2:
            kan_result = True
            break
        if(v1>v2 and x1>x2) or (v2>v1 and x2>x1) or(v1==v2 and x2 != x1):
            break
        x1 += v1
        x2 += v2
    
    if(kan_result):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
