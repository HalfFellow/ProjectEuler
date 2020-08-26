# -*- coding: utf-8 -*-

# Project Euler
# Problem 025: 1000-digit Fibonacci number
# Runtime : 2 ms

import time
import Useful_Functions_PE as Euler

if __name__ == '__main__':
    start_time = time.time()
    
    #Function starts at 1-2 instead of 1-1. By bounding at 1000 digits - 1, we know that the next term will be 1000-digit
    print(len(Euler.Fibonacci_TermListUpTo(10 ** 999))+1)
    print('{:2f} seconds'.format(time.time() - start_time)) 