#!/usr/bin/env python
import sys


def main_loop():
    while True:
        try:
            print(eval(input("> ")))
        except EOFError:
            exit()
            print("Exiting REPL.")
        except KeyboardInterrupt:
            print("\n")
        except:
            print("({0} {1}) I don't recognize that.".format(sys.exc_info()[0], sys.exc_info()[1]))


def main():
    main_loop()

if __name__ == '__main__':
    main()
