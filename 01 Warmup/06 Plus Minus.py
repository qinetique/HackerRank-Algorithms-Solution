#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def plusMinus(arr):
    # Write your code here
    p,q,r = 0,0,0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            q += 1
        elif arr[i] == 0:
            r += 1
    print(p/len(arr))
    print(q/len(arr))
    print(r/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
