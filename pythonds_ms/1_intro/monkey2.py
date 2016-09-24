#!/usr/bin/env python

from string import ascii_lowercase
import random
alphabet = list(ascii_lowercase)  # + " ")
shake = "methinks"


def getScore(s):
    score = 0
    total = len(shake)
    for i in range(len(s)):
        if s[i] == shake[i]:
            score = score + 1
    return score / total
    # return True if s == shake else False


def genShakespeare():
    phrase = ""
    for i in range(len(shake)):
        phrase = phrase + random.choice(alphabet)
        # import ipdb; ipdb.sset_trace()
    return phrase


def main():
    correct = False
    attempt_count = 0
    while correct is False:
        attempt = genShakespeare()
        score = getScore(attempt) * 100
        if score == 100.0:
            correct = True
        attempt_count = attempt_count + 1
        print("{0}\t{1}\tAttempt: {2:,}".format(attempt, score, attempt_count))

if __name__ == '__main__':
    main()
