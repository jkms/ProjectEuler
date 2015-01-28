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


def get_next_digit(numerator, denominator):
    """Get the next digit"""

    padding = ''

    if numerator < denominator:
        numerator *= 10 ** len(str(denominator))
        padding = "0"

    product = str(int(numerator / denominator))
    padding = padding * ((len(str(denominator)) -1) - (len(product)-1))
    product = padding + product

    return product, int(numerator % denominator)


def get_division(denominator, length=5000, numerator=1):
    """Get a sequence of digits"""

    my_decimal = ""
    while len(my_decimal) < length:
        temp = get_next_digit(numerator, denominator)
        # print i, "temp", temp
        my_decimal += temp[0]
        numerator = temp[1]
    # print "garbage:", 1/float(i)
    return my_decimal


def get_products(value):
    """Get list of products"""

    i = 2
    products_return = [value]
    while i < products_return[-1]:
        if not value % i:
            products_return.append(i)
            products_return.append(value/i)
        i += 1
    products_return.remove(value)
    return sorted(products_return, reverse=True)


def find_pattern(haystack, find_length):
    """Find a pattern in a haystack"""

    start_point = 0
    found_pattern = False
    while not found_pattern:
        needle = haystack[start_point:start_point+find_length]
        number_repeats = len(haystack)-start_point
        number_repeats -= number_repeats % len(needle)
        number_repeats /= len(needle)
        if needle * number_repeats == haystack[start_point:start_point+(find_length * number_repeats)]:
            return haystack[start_point:start_point+find_length]
            found_pattern = True
        if start_point >= (len(haystack) - len(needle))/2:
            return None
            break
        start_point+=1


repeating = []
for i in range(1, 1000):
    if is_prime(i):
        print i
        pattern_found = False
        temp = get_division(i, i  *2)
        pattern_length = 2
        while not pattern_found:
            pattern_found = False
            pattern = ''
            pattern = find_pattern(temp, pattern_length)
            if pattern:
                pattern_found = True
                repeating.append([i, pattern_length, pattern])
                break
            pattern_length += 1


repeating = sorted(repeating, key=lambda x: x[1])

print repeating[-1][2]
print "the answer is", repeating[-1][0], "(it has a", repeating[-1][1], "digit reciprocal cycle)"
