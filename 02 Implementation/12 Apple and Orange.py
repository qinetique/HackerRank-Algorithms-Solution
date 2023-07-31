#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_apple = 0
    count_orange = 0

    for apple in apples:
        if(apple + a >= s and apple + a <= t):
            count_apple += 1
    
    for orange in oranges:
        if(orange + b <= t and orange + b >= s):
            count_orange += 1
    
    return "\n".join([str(count_apple), str(count_orange)])

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    print(countApplesAndOranges(s, t, a, b, apples, oranges))
