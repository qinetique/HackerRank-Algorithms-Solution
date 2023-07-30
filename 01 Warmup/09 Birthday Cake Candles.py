#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def birthdayCakeCandles(candles):
    # Write your code here
    maxCand = max(candles)
    countCand = 0
    for i in range(0, len(candles)):
        if(candles[i] == maxCand):
            countCand += 1
    return countCand

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
