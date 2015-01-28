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
    for i in xrange(2, int(math.sqrt(value))+1):
        if not value % i:
            return_prime = False
    return return_prime


def euler_primes(a, b):
    euler_primes=[]
    for n in range (39):
        temp = n ** 2 + n * a + b
        if is_prime(temp):
            euler_primes.append(temp)
    return euler_primes

print euler_primes(1,41)
