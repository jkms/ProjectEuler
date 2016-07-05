#!/usr/bin/env python
# problem42.py

import csv

def dig_letter(x):
    alpha="abcdefghijklmnopqrstuvwxyz"
    return alpha.index(x.lower())+1

def open_file(file):
    with open(file, 'rb') as f:
        reader = csv.reader(f)
        return list(reader)

def triangle(max):
    values = [1]
    n = 2
    while True:
        values.append((n+1)*n/2)
        if values[-1] > max:
            break
        n += 1
    return values

def sum_word(word):
    sum=0
    for x in word:
        sum += dig_letter(x)
    return sum

def main():
    num_words = 0
    triangles = triangle(5000)
    words = open_file('p042_words.txt')
    for word in words[0]:
        wordsum = sum_word(word)
        if wordsum in triangles:
            # print word, wordsum, wordsum in triangles
            num_words += 1
    return num_words

print "the answer is", main()
