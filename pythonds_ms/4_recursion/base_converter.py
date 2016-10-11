
def divideByBase(n, base):
    convString = "0123456789ABCDEF"
    if n < base:
        return convString[n]
    return divideByBase(n // base, base) + convString[n % base]


def main():
    assert divideByBase(10, 2) == bin(10)[2:]
    # print(divideByBase(17, 16))
    assert divideByBase(17, 16) == hex(17)[2:]

if __name__ == '__main__':
    main()
