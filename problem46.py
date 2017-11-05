#!/usr/bin/env python
# problem46.py

import math
from bisect import bisect_left
from math import sqrt
import random

def check_prime(value, primes):
    is_prime=True
    max_pos=bisect_left(primes, int(math.sqrt(value)))+1
    for p in primes[:max_pos]:
        if value % p == 0:
            is_prime=False
            break
    return is_prime

def gen_primes(max, primes=[2,0]):
    primes=[2,]
    for i in xrange(primes[-1]+1,max,2):
        if check_prime(i,primes):
            primes.append(i)
    return primes

def check_goldbach(test, primes):
    solutions=0
    print "testing " + str(test)
    for p in primes:
        if (p > test):
            print "I ran out of primes"
            break
        else:
            #print "checking" + str(p) + "... " + str(test - p) + "... divide by two..." + str(float(test -p)/2) + " .... " + str(sqrt(float(test -p)/2).is_integer())
            if (sqrt(float(test -p)/2).is_integer()):
                print str(p) + " + 2x" + str(int(sqrt(int(test -p)/2))) + "^2"
                solutions+=1
                break

    return solutions




my_primes = gen_primes(100000)

test_range = 1000
test = 3

disproven=False
while not disproven:
    print str(test)
    if not (check_goldbach(test,my_primes)):
        print "the answer is " + str(test)
        disproven=True
    else:
        test += 2
