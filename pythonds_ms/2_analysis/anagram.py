#!/usr/bin/env python
def is_anagram(w1, w2):
    "Verifies if these two are anagrams."
    print("Are {0} and {1} anagrams?".format(w1, w2))
    w1, w2 = map(lambda w: w.lower(), [w1, w2])
    rev = ""
    for i in range(1, len(w2)+1):
        rev += w2[-i]
    if rev == w1:
        print("\tYes")
    else:
        print("\tNo")


def main():
    is_anagram("racecar", "racecar")
    is_anagram("test", "tset")
    is_anagram("apples", "oranges")


if __name__=="__main__":
    main()

