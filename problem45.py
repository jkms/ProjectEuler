#!/usr/bin/env python
# problem45.py

def main():
    T = {}
    P = {}
    H = {}
    for n in range(1,500000):
        T[(n*(n+1)/2)]=True
        P[(n*(3*n-1)/2)]=True
        H[n*(2*n-1)]=True
    for a in T:
        if a in P and a in H and a != 1:
            print "hit", a
main()
