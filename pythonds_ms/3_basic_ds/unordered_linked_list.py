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


class UnorderedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def iterate_all(self):
        current = self.head
        lst = [current]
        while current != None:
            current = current.getNext()
            lst.append(current)
        return lst[:-1]

    def search(self, item):
        current = self.head
        while hasattr(current, "getValue"):
            if current.getValue() == item:
                return current
            current = current.getNext()

        return None

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getValue() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        'Appends to the tail'
        item = Node(item)
        original = self.head
        while self.head != None:
            prev = self.head
            self.head = self.head.getNext()
        prev.setNext(item)
        self.head = original

    def insert(self, index, item):
        if index > self.size():
            return None
        count = 0
        while count <= index:

def utlist_fixture():
    ulist = UnorderedList()
    for i in ["cat", "foo", 542, "bar"]:
        ulist.add(i)
    return ulist


def test_search():
    ulist = utlist_fixture()
    assert ulist.search("cat").getValue() == "cat"
    assert ulist.search("asdfadsf") == None


def test_remove():
    ulist = utlist_fixture()
    init_size = ulist.size()

    # Remove from the beginning of the list
    ulist.remove("bar")
    print(ulist.iterate_all())
    assert ulist.size() == init_size - 1

    ulist.remove("foo")
    print(ulist.iterate_all())
    assert ulist.size() == init_size - 2


def test_append():
    ulist = utlist_fixture()
    init_size = ulist.size()

    ulist.append(3.14159268)
    print(ulist.iterate_all())
    assert ulist.search(3.14159268) != None
    assert ulist.size() == init_size + 1


def main():
    print(utlist_fixture().iterate_all())
    test_search()
    test_remove()
    test_append()

if __name__ == '__main__':
    main()
