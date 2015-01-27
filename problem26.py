#  problem26.py
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
    return_prime = 1
    for i in xrange(2, int(math.sqrt(value))+1):
        if not value % i:
            return_prime = 0
    return return_prime


def get_next_digit(numerator, denomerator):
    """Get the next digit"""

    product = ''
    padding = ''

    if numerator < denomerator:
        numerator *= 10 ** len(str(denomerator))
        padding = "0"

    product = str(int(numerator / denomerator))
    padding = padding * ((len(str(denomerator)) -1) - (len(product)-1))
    product = padding + product

    return product, int(numerator % denomerator)


def get_division(denominator, length=10, numerator=1):
    """Get a sequence of digits"""

    my_decimal = ""
    while len(my_decimal) < length:
        temp = get_next_digit(numerator, denominator)
        # print i, "temp", temp
        my_decimal += temp[0]
        numerator = temp[1]
    # print "garbage:", 1/float(i)
    return my_decimal


for i in range(1, 100):
    if is_prime(i):
        print "1/"+str(i)+"=", get_division(i, 100)