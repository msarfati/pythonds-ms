#!/usr/bin/env python


class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def addRear(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def __repr__(self):
        return str(self.items)


def palindromeChecker(s):
    'Checks if a given string is a palindrome'
    deque = Deque()
    for i in s:
        deque.addRear(i)

    while deque.size() > 1:
        if deque.removeFront() != deque.removeRear():
            return False

    return True


def test_palindromeChecker():
    assert palindromeChecker("toot") == True
    assert palindromeChecker("racecar") == True
    assert palindromeChecker("book") == False
    assert palindromeChecker("l" * 99) == True


def main():
    test_palindromeChecker()

if __name__ == '__main__':
    main()
