#!/usr/bin/env python
# problem38.py

def is_pandigital(value):
    string = ''.join(sorted(str(value)))
    if string == '123456789':
        return True
    return False

def cat_prod(value,len):
    prods=[]
    for n in range(1,len):
        prods.append(str(value*n))
    return int(''.join(prods))

def main():
    pan_list=[]
    for i in range(1, 10000):
        under_limit = True
        n=2
        while under_limit:
            cat = cat_prod(i,n)
            if cat <= 987654321:
                if is_pandigital(cat):
                    pan_list.append(cat)
                n += 1
            else:
                under_limit = False
    print "the answer is", sorted(pan_list)[-1]
main()
