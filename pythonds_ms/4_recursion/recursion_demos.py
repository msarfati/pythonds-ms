from functools import reduce


def word_builder(lst, s=""):
    "Takes list, recursively builds a string from it"
    if len(lst) == 0:
        return s
    return word_builder(lst[1:], s + lst[0])


def reverse(s):
    if len(s) < 1:
        return ""
    return s[-1] + reverse(s[:-1])


def main():
    s1 = "my string"
    reverse_str = lambda s: reduce(lambda x, y: x + y, reversed(s))
    # print(word_builder(list(s1)))
    assert word_builder(list(s1)) == s1
    assert reverse(s1) == reverse_str(s1)
    s2 = "Foobar and fdfawf3fr34redsf9ijokp3gq394g erhvdkmi23opr vou2389rvh 3"
    assert reverse(s2) == reverse_str(s2)


if __name__ == '__main__':
    main()
