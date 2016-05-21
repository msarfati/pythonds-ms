#!/usr/bin/env python
import itertools as it
from functools import reduce


def make_sentence():
    "Makes and compares the sentence"
    correct = "methinks it is like a weasel"  # 28 characters long

    alphabet = it.permutations("abcdefghijklmnopqrstuvwxyz ")
    sentence = ""
    i = 0

    while sentence is not correct:
        sentence = reduce(
            lambda j, k: j+k,  # turns tuple into string for comparison
            next(alphabet))  # Iterates through tuple
        i += 1
        if i % 1000 == 0:
            print("Attempt #{0}: {1}".format(i, sentence))

    print("Correct after {0} attempts".format(i))


def main():
    make_sentence()

if __name__ == '__main__':
    main()
