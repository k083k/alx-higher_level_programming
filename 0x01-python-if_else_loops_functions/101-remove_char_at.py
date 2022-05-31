#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = ""
    if n < 0 or n > len(str):
        return str
    for i in str:
        if i != str[n]:
            strcopy += i
    return strcopy
