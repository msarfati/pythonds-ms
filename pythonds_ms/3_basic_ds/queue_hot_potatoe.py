#!/usr/bin/env python


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


def hotPotateSim(n):
    agents = Queue()
    [agents.enqueue(i) for i in ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]]

    while agents.size() > 1:
        for i in range(n):
            agents.enqueue(agents.dequeue())
        agents.dequeue()

    return agents.dequeue()


def testHotPotatoe():
    assert hotPotateSim(7) == "Susan"


def main():
    testHotPotatoe()

if __name__ == '__main__':
    main()
