#!/usr/bin/env python
# Impl. of a Stack
import unittest


class EmptyStackError(Exception):
    def __str__(self):
        return "You cannot pop from an empty stack."


class Stack():
    def __init__(self, *args):
        self.__stack__ = [*args]

    def __repr__(self):
        return str(self.__stack__)

    def __len__(self):
        return self.__stack__.__len__()

    def push(self, item):
        self.__stack__.append(item)

    def pop(self):
        try:
            return self.__stack__.pop()
        except:
            raise EmptyStackError

    def peek(self):
        return self.__stack__[-1]

    def isEmpty(self):
        return True if len(self.__stack__) == 0 else False

    def size(self):
        return self.__len__()


class StackTestCase(unittest.TestCase):

    @classmethod
    def fixture(cls):
        return Stack(3, "sum", 3.2)

    def setUp(self):
        self.stack = self.fixture()

    def test_push(self):
        "Testing Stack.push"
        self.stack.push('new element')
        self.assertEqual(self.stack.__stack__[-1], 'new element', 'element pushed ontop of stack')

    def test_pop(self):
        "Testing Stack.pop"
        for i in range(len(self.stack)):
            self.stack.pop()
        self.assertRaises(EmptyStackError, self.stack.pop)

    def test_peek(self):
        "Testing Stack.peek"
        self.assertEquals(self.stack.peek(), self.stack.__stack__[-1], "peek returns topmost element")

    def test_isEmpty(self):
        "Testing Stack.isEmpty"
        self.assertFalse(self.stack.isEmpty(), "Stack is not empty yet.")
        for i in range(len(self.stack)):
            self.stack.pop()
        self.assertTrue(self.stack.isEmpty(), "Stack is indeed empty.")

    def test_size(self):
        "Testing Stack.size"
        self.assertEquals(self.stack.size(), self.stack.__stack__.__len__(), "Size of stack is as anticipated")


def revstring(s):
    """
    Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
    """
    stack = Stack(*s)
    rev = map(lambda i: stack.pop(), range(len(stack)))

    rev_str = str()
    for i in rev:
        rev_str = rev_str + i
    return rev_str


def test_revstring():
    "Testing revstring"
    assert revstring('hello') == 'olleh'
