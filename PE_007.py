# -*- coding: utf-8 -*-

# Project Euler
# Problem 007: 10001st Prime
# Runtime : 120 ms

import time
import Useful_Functions_PE as Euler

if __name__ == '__main__':
    start_time = time.time()
    print(Euler.nthPrime(10001))
    print('{:2f} seconds'.format(time.time() - start_time))