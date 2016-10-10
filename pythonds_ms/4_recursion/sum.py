#!/usr/bin/env python
from functools import reduce


def iterSum(lst):
    accum = 0
    for i in lst:
        accum += i
    return accum


def recurSum(lst):
    n = lst.pop()  # Stateful
    if len(lst) == 0:
        return n
    return n + recurSum(lst)


def recurSum2(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + recurSum2(lst[1:])


def recurSum3(lst):
    return lst[0] + recurSum2(lst[1:]) if not (len(lst) == 1) else lst[0]


def iterProduct(lst):
    accum = 1
    for i in lst:
        accum *= i
    return accum


def recurProduct(lst):
    return lst[0] * recurProduct(lst[1:]) if not (len(lst) == 1) else lst[0]


def recurExp(base, exp):
    if exp == 0:
        return 1
    return base * recurExp(base, exp - 1)


def main():
    lst = [4, 3, 68, 34, 67, 12]
    product = lambda lst: reduce(lambda x, y: x * y, lst)
    assert iterSum(lst) == sum(lst)

    assert recurSum(list(lst)) == sum(lst)  # Operation is stateful because it pops, so we create a new list from the same element set
    assert recurSum2(lst) == sum(lst)
    assert recurSum3(lst) == sum(lst)

    assert iterProduct(lst) == product(lst)
    assert recurProduct(lst) == product(lst)
    assert recurExp(2, 6) == 2**6
    # print(recurSum(lst))
    # print(sum(lst))

if __name__ == '__main__':
    main()
