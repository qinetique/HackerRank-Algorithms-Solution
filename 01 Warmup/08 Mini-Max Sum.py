#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        total = 0
        for j in range(i, i+4):
            total += arr[j]
        sum[i] = total
    print(sum[0],sum[-1])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
