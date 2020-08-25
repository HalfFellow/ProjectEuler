# -*- coding: utf-8 -*-

# Project Euler
# Problem 010: SummationofPrimes
# Runtime : 2.5 seconds

import time
import Useful_Functions_PE as Euler
  
if __name__ == '__main__':
    start_time = time.time()
    print(sum(Euler.PrimeList(1999999)))
    print('{:2f} seconds'.format(time.time() - start_time))