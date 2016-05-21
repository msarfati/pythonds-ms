#!/usr/bin/env python
# Impl. of a Stack
from unittest import TestCase

class EmptyStack(Exception):
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
            raise EmptyStack

    def peek(self):
        return self.__stack__[-1]


def StackTestCase(TestCase):
   def test_pop():
        s = Stack(3, "sum", 3.2)
        for i in range(len(s)):
            s.pop()
        s.pop()

