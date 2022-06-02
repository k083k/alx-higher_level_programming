#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv) - 1
    total = 0
    for n in range(i):
        total = total + int(sys.argv[n + 1])

    print("{}".format(total))
