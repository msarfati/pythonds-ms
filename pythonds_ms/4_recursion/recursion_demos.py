
def word_builder(lst, s=""):
    "Takes list, recursively builds a string from it"
    if len(lst) == 0:
        return s
    return word_builder(lst[1:], s + lst[0])


def main():
    s1 = "my string"
    # print(word_builder(list(s1)))
    assert word_builder(list(s1)) == s1


if __name__ == '__main__':
    main()
