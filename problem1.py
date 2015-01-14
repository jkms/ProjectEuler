#!/usr/bin/env python

count=0

for x in range (0, 1000):
	if (x % 3 == 0) or (x % 5 == 0):
		count += x
		print "%d makes %d" % (x, count)
		
print "The Answer is %d" % count
