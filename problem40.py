#!/usr/bin/env python
# probem40.py

def gen_number(limit):
    value = '.'
    number = 1
    while len(value) < limit:
        value += str(number)
        number += 1
    return value

def main():
    bignum = gen_number(1000001)
    product = 1
    for i in range(0,7):
        digit = 10**i
        print digit, bignum[digit]
        product *= int(bignum[digit])
    return product
        
print "the answer is", main()
