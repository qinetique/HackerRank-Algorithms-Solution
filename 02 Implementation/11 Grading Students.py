#!/bin/python3

import math
import os
import random
import re
import sys

#Author: Tonmoy M
#URL: https://github.com/qinetique

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if(grades[i] >= 38):
            if((grades[i] % 5) > 2):
                while((grades[i] % 5) != 0):
                    grades[i] += 1
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
