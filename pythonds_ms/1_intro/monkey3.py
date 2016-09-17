#!/usr/bin/env python

from string import ascii_lowercase
import random
alphabet = list(ascii_lowercase)
alphabet.append(" ")
shake = list("methinks it is like a weasel")


def check_phrase(p):
    'Returns a list of indicies that should be replaced'
    replace_i = []
    for i in range(len(p)):
        if p[i] != shake[i]:
            replace_i.append(i)
    return replace_i


def gen_phrase():
    "Generates a random phrase."
    phrase = list()
    for i in range(len(shake)):
        phrase.append(random.choice(alphabet))
    return list(phrase)


def correct_phrase(p):
    "Takes existing phrase and corrects it"
    replace_index = check_phrase(p)
    # import ipdb; ipdb.sset_trace()
    for i in replace_index:
        p[i] = random.choice(alphabet)
    return p


def main():
    phrase = gen_phrase()
    attempts = 0
    while phrase != shake:
        phrase = correct_phrase(phrase)
        attempts = attempts + 1
        print("".join(phrase), attempts, sep="\t")

if __name__ == '__main__':
    main()
