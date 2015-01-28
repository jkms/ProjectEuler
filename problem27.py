#  problem27.py
#
#  Copyright 2015 John Stafford <john@jkms.me>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#!/usr/bin/env python

import math


def is_prime(value):
    """check for primes"""
    return_prime = True
    for i in xrange(2, int(math.sqrt(abs(value)))+1):
        if not value % i:
            return_prime = False
    return return_prime


def euler_primes(n, a, b):
    return n ** 2 + n * a + b
    
base_primes=[]
for i in range (1000):
    if is_prime(i):
        base_primes.append(i)
        base_primes.append(i*-1)
base_primes=sorted(base_primes)

quads=[]
quads.append([0,0])
for a in base_primes:
    for b in base_primes:
        last_prime=True
        n=0
        while last_prime == True:
            temp = euler_primes(n, a, b)
            #~ print a,b,temp
            if is_prime(temp):
                n += 1
            else:
                last_prime = False
                if n > quads[-1][0]:
                    quads.append([n, a*b])
                break

print "the answer is", quads[-1][1]
