# -*- coding: utf-8 -*-

# Project Euler
# Problem 009: Special Pythagorean triplet
# Runtime : 173 ms

import time
import math

def PythagoreanTriplet(sumoftriplet):
    for c in range(sumoftriplet, math.floor(sumoftriplet / 3), -1):
        for b in range(sumoftriplet - c - 1 ,math.floor((sumoftriplet - c) / 2), -1):
            a = sumoftriplet - c - b
            if (a ** 2 + b ** 2 == c ** 2):
                print("a - {}\nb - {}\nc - {}\nAnswer {}".format(a,b,c,a * b * c))

if __name__ == '__main__':
    start_time = time.time()
    print(PythagoreanTriplet(1000))
    print('{:2f} seconds'.format(time.time() - start_time)) 
