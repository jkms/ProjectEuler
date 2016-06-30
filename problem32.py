#!/usr/bin/env python
import time
start_time = time.time()

import itertools
combs=[]
a = range(1,10)
b = len(a)
combs = list(itertools.permutations(a, b))

detects = []

def test_set(mone,mtwo,mtre,set):
    sets = int(''.join(map(str,set)))
    mlier = int(''.join(map(str,mone)))
    mand = int(''.join(map(str,mtwo)))
    prod = int(''.join(map(str,mtre)))
    if mlier * mand == prod:
        if sets == int(''.join(map(str,[mlier,mand,prod]))):
            if prod in detects:
                print "dupe!", sets, "dupe!"
                print "dupe!", mlier, mand, prod, "dupe!"
            else:
                detects.append(prod)
                print sets
                print mlier, mand, prod
                return True

def iter_set(set):
    theanswer = 0
    mone = []
    mtwo = []
    mthr = []
#    print "=========="
#    print set
#    print "=========="
    for n in range(1,len(set)-0):
        for o in range(n+1,len(set)-0):
#            print set[0:n], set[n:o], set[o:]
            if test_set(set[0:n], set[n:o], set[o:], set):
                print "success!"

for set in combs:
    iter_set(set)
#    if test_set(set[0],set[1],set[2]):
#        print set

result = 0

result = sum(detects)
print "the answer is %d" % result 
print("--- %s seconds ---" % (time.time() - start_time))
