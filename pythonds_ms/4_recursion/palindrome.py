#!/usr/bin/env python


def preproc(s, memo=""):
    if len(s) == 0:
        return memo
    if s[0].isalpha():
        memo += s[0].lower()
    return preproc(s[1:], memo)


def palindrome(s):
    if len(s) == 1:
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])

assert palindrome('racecar') == True
assert palindrome('cat') == False
assert palindrome('this string') == False
assert palindrome('racecar') == True
assert palindrome('aibohphobia') == True

assert palindrome(preproc("Degas, are we not drawn onward, no? In union, drawn onward to new eras aged?")) == True
