#!/usr/bin/env python


def guess_sqrt(n):
    guess = n/2
    for i in range(20):
        guess = (1/2) * (guess + (n/guess))
    return guess
