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


def iter_fib(n):
    n1 = n2 = 1
    for i in range(n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
    return n3


def fib(n, a=1, b=1):
    if n <= 0:
        return b
    return fib(n-1, a=b, b=a+b)


def fib2(n):
    if n == 0 or n == 1:
        return 1
    return fib2(n-1) + fib2(n-2)


def recur_count(n):
    if n <= 0:
        return 0
    return 1 + recur_count(n-1)


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
    # print(fib(12))
    assert fib2(11) == 144
    print(recur_count(9))


if __name__ == '__main__':
    main()
