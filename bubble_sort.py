#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    numSwapsTotal = 0
    for i in range(n):
        numSwapsRound = 0
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwapsRound += 1

        if numSwapsRound == 0:
            break
        numSwapsTotal += numSwapsRound

    print(f"Array is sorted in {numSwapsTotal} swaps.")
    print("First element:", a[0])
    print("Last element:", a[-1])