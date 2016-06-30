#!/usr/bin/env python
import time

start_time = time.time()

import math
result = 0

for n in range(3,1000000):
    checksum = 0
#    print n
    for d in str(n):
#        print d 
        checksum += math.factorial(int(d))
    if checksum == n:
        print "hit!", checksum, n
        result += n

print "the answer is", result
print("--- %s seconds ===" % (time.time() - start_time))
