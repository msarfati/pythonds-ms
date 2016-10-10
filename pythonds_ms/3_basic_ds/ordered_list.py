#!/usr/bin/env python

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class OrderedList:
    def __init__(self):
        pass

    def add(self, item):
        pass

def main():
    pass

if __name__ == '__main__':
    main()
