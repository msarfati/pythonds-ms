#!/usr/bin/env python


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


def balancedParens(s):
    parens = Stack()
    for i in s:
        if i in '({[':
            parens.push(i)
        if i in ')}]':
            if parens.isEmpty():
                return False
            parens.pop()
    return parens.size() == 0


def test_balancedParens():
    assert balancedParens('()') == True
    assert balancedParens('([{}])') == True
    assert balancedParens('([{{}])') == False
    assert balancedParens('(())') == True
    assert balancedParens('(()))') == False
    assert balancedParens('(((((()))') == False


def divideBy2(v: int) -> str:
    assert v > 0, "Must be greater than zero."
    remainders = Stack()
    i = v
    while i > 0:
        remainders.push(i % 2)
        i //= 2

    bin_str = "0b"
    for i in range(remainders.size()):
        bin_str += str(remainders.pop())

    return bin_str


def test_divideBy2():
    assert divideBy2(255) == bin(255)
    assert divideBy2(34) == bin(34)
    assert divideBy2(35) != bin(99)


def main():
    # test_balancedParens()
    test_divideBy2()

if __name__ == '__main__':
    main()
