#!/usr/bin/env python
# problem36.py

def to_bin(i):
    return int(bin(i)[2:])

def is_palindrome(string):
    if str(string) == str(string)[::-1]:
        return True
    return False

def main():
    answer=0
    for i in range(1,1000000):
        b = to_bin(i)
        if is_palindrome(i) and is_palindrome(b):
            answer += i
    return answer

print "the answer is", main()
