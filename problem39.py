#!/usr/bin/env python
# problem39.py

def int_triangle(p):
    count = 0
    # find the hypo
    limit = int(p/(2+2**(0.5)))
    for a in range(1,limit):
        for b in range(1,(p-a)/2):
            c=(a**2+b**2)**(0.5)
            if a + b + c == p:
                count += 1
                break
    return count

def main():
    max = [0,0]
    for p in range (10,1000):
        print p
        ints = int_triangle(p)
        if ints > max[1]:
            max = [p,ints]
    print "the answer is", max[0]
main()
