#!/usr/bin/env python

fib = [1,2]
count = 0

while (fib[-1]+fib[-2])<4000000:
	fib.append(fib[-1] + fib[-2])

print fib

for i in range(0,len(fib)):
	if fib[i-1] % 2 == 0:
		print "%d is even" % fib[i-1]
		count += fib[i-1]

print "The answer is %d" % count
