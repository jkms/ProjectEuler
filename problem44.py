#!/usr/bin/env python
# problem44.py
import time
start_time = time.time()


def solve():
    pents = {}
    for n in range(1,2500+1):
      pents[(n*(3*n-1)/2)] = True

    for x in pents:
        for y in pents:
            if (x+y) in pents and abs(x-y) in pents:
                return abs(x-y)

print "the answer is ", solve()

print("--- %s seconds ---" % (time.time() - start_time))
