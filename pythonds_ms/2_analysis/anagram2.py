#!/usr/bin/env python


# def isAnagramQuadratic(w1, w2):
#     for i in range(len(w1)):
#         for j in range(len(w2)):
#             if w1[i] == w2[i]:
#                 return False
#     return True

def isAnagramLinear2(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()

    # count_ltrs = lambda s: map(lambda s, c: pass, s, [i for i in range(256)])

    def count_letters(s):
        c = [0] * 26
        for i in range(len(s)):
            c[ord(s[i]) - 97] += 1
        return c

    c1 = count_letters(w1)
    c2 = count_letters(w2)

    for i, j in zip(c1, c2):
        if i != j:
            return False

    return True


def isAnagramLinear(w1, w2):
    w1 = list(w1)
    w2 = list(w2)
    w1.sort()
    w2.sort()

    for i, j in zip(w1, w2):
        if i != j:
            return False

    return True

print(isAnagramLinear2('asdf', 'fdsa'))
print(isAnagramLinear2('heart', 'earth'))
print(isAnagramLinear2('job', 'bob'))
# print(isAnagramLinear2('job', 'bd34rf3tu8rwfiods8ijo23ewsob'))
