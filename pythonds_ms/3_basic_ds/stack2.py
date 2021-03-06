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

    def peek(self):
        return self.items[-1]

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
    "A method for converting decimal to binary."
    assert v > 0, "Must be greater than zero."
    remainders = Stack()
    while v > 0:
        remainders.push(v % 2)
        v //= 2

    bin_str = "0b"
    while not remainders.isEmpty():
        bin_str += str(remainders.pop())

    return bin_str


def test_divideBy2():
    assert divideBy2(255) == bin(255)
    assert divideBy2(34) == bin(34)
    assert divideBy2(35) != bin(99)


def divideByN(v: int, base: int) -> str:
    "A method for converting any decimal number into any base."
    assert v > 0, "Must be greater than zero."
    remainders = Stack()
    while v > 0:
        remainders.push(v % base)
        v //= base

    converted_str = ""
    from string import ascii_lowercase
    num_map = {k+10: v for k, v in zip(range(26), ascii_lowercase)}
    while not remainders.isEmpty():
        remainder = remainders.pop()
        if remainder > 9:
            remainder = num_map[remainder]
        converted_str += str(remainder)

    return converted_str


def test_divideByN():
    assert divideByN(255, 16) == hex(255)[2:]
    assert divideByN(34, 8) == oct(34)[2:]
    assert divideByN(42, 2) == bin(42)[2:]


def infixToPostfixNotation(exp):
    'Tokenizes and parses basic arithmetic expressions.'
    import string
    exp = exp.upper()
    prec = {
        '*': 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1,
    }
    opStack = Stack()
    postfixList = []
    tokenList = exp.split()

    for token in tokenList:
        if token in string.ascii_uppercase or token in string.digits:
            postfixList.append(tok-en)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


def test_infixToPostfixNotation():
    assert infixToPostfixNotation("A * B + C * D") == "A B * C D * +"
    assert infixToPostfixNotation(
        "( A + B ) * C - ( D - E ) * ( F + G )") == "A B + C * D E - F G + * -"
    assert infixToPostfixNotation("( A + B ) * ( C + D )") == 'A B + C D + *'


def main():
    # test_balancedParens()
    # test_divideBy2()
    # test_divideByN()
    test_infixToPostfixNotation()

if __name__ == '__main__':
    main()
