#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def staircase(n):
    for i in range(0,n):
        for j in range(0,n):
            if(i+j>=n-1):
                print("#", end="")
            else:
                print(" ", end="")
        print("\t")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
