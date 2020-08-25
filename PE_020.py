# -*- coding: utf-8 -*-

# Project Euler
# Problem 020: Factorial Digit Sum
# Runtime : 0 ms

import time
import Useful_Functions_PE as Euler

if __name__ == '__main__':
    start_time = time.time()
    print(Euler.sumofdigits(Euler.factorial(100)))
    print('{:2f} seconds'.format(time.time() - start_time)) 