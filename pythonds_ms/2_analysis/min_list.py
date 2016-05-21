# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list O(n^2) . The second function should be linear O(n) .

def find_min1(seq):
    "at: O(n)"
    small = seq[0]
    for i in seq:
        small = i if i < small else small
    return small

def find_min2(seq):
    "Supposed to be at: O(n^2)"
    small = seq[0]
    for i in seq:
        for j in seq:
            small = j if j < i and j < small else small
    return small
