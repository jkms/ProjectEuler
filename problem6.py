#!/usr/bin/env python

import math

sums = 0
for x in range(1,101):
	sums += math.pow(x,2)

print sums


sumsx = 0
for x in range(1,101):
	sumsx += x

sumsx = math.pow(sumsx,2)	
print sumsx

answer = sumsx-sums

print "the answer is", sumsx, "-", sums, "=", int(answer)
