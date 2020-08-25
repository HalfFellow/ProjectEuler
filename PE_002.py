# -*- coding: utf-8 -*-

# Project Euler
# Problem 002: Even Fibonacci Numbers
# Runtime : 0 ms

import time
import Useful_Functions_PE as Euler

if __name__ == "__main__":
    start_time = time.time()
    print(sum([i for i in Euler.Fibonacci_TermListUpTo(4000001) if i%2==0]))
    print('{:2f} seconds'.format(time.time() - start_time)) 

