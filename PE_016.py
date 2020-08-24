# -*- coding: utf-8 -*-

# Project Euler
# Problem 016: Power Digit Sum
# Runtime : 1 ms (0.001 second)
    
import time

def sumofdigits(x):
    return sum([int(i) for i in str(x)])

if __name__ == '__main__':
    start_time = time.time()
    print(sumofdigits(2 ** 1000))
    print('{:2f} seconds'.format(time.time() - start_time))    