#!/usr/bin/enc python
import time
start_time = time.time()

def two_dig():
    return range(11,100)
def palindrome(num):
    return str(num)[::-1]

numerator = 1
denominator = 1

for n in two_dig():
    for d in two_dig():
        if n != d and palindrome(n) != str(n) and palindrome(d) != str(d) and float(n) / float(d) < 1 and d % 10 != 0:
#            print "{} / {}".format(n, d)
            for a in str(n):
                for b in str(d):
                    if a == b:
                        n1 = float(str(n).replace(a,''))
                        d1 = float(str(d).replace(a,''))
#                        print "{}/{},{}.{}".format(n,d,n1,d1)
                        if n1 / d1 == float(n) / float(d):
                            print "hit {} / {}".format(n, d)
                            numerator *= n
                            denominator *= d

print "{} / {} factors to...".format(numerator, denominator)
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    while numerator % p == 0 and denominator % p == 0:
        numerator /= p
        denominator /= p
print "{} / {}".format(numerator, denominator)

print "the answer is %d" % denominator
print("--- %s seconds ---" % (time.time() - start_time))
