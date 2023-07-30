#Author: Tonmoy M
#URL: https://github.com/qinetique

import math
import os
import random
import re
import sys
def compareTriplets(a, b):
    result = []
    p = 0
    q = 0

    for i in range(0, len(a)):
        if a[i] > b[i]:
            p += 1
        elif a[i] < b[i]:
            q += 1
        else:
            continue
    result.append(p)
    result.append(q)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
