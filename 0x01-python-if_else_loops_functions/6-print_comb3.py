#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i + 1, 10):
        if not (i == 8 and x == 9):
            print(f"{i:d}{x:d}", end=", ")
        else:
            print(f"{i:d}{x:d}", end="\n")
