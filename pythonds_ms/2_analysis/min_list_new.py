#!/usr/bin/env python
from random import randint


def getMinQuadratic(l):
    """
    Gets minimum value for a given list in a quadratic time complexity algorithm

    :param l: a list of integers
    :type l: list

    :returns: Minimum element from a list.
    """
    m = l[0]
    for i in l:
        for j in l:
            if j < i and j < m:
                m = j
    return m


def getMinLinear(l):
    """
    Gets minimum value for a given list in a linear time complexity algorithm

    :param l: a list of integers
    :type l: list

    :returns: Minimum element from a list.
    """
    m = l[0]        # O(1)
    for i in l:     # O(n)
        if i < m:   # O(1)
            m = i   # O(1)
    return m        # O(1)


def printResult(l, func):
    """
    Prints result into a standard format4

    :param l: a list of integers
    :type l: list

    :param func: function name
    :type func: function
    """
    # import ipdb; ipdb.sset_trace()
    result = func(l)
    print("{0}\n---------\n{1}\n{2}\n".format(func.__name__, l, result))


def main():
    l1 = [randint(1, 100) for i in range(5)]
    printResult(l1, getMinLinear)
    printResult(l1, getMinQuadratic)


if __name__ == '__main__':
    main()
