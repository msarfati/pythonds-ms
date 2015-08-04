#!/usr/bin/env python

from time import time

def foo(tom):
    s = time()
    fred = 0
    for bill in range(1,tom+1):
       barney = bill
       fred = fred + barney

    return fred, time() - s

print(foo(10))

