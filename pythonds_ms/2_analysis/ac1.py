#!/usr/bin/env python

from time import time


def sumOfN(n):
    s = time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    return theSum, time() - s

print(sumOfN(10))

