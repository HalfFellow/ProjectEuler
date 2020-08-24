# -*- coding: utf-8 -*-

# Project Euler
# Problem 015: Lattice Paths
# Runtime : 0 ms

import time
import Useful_Functions_PE as Euler
    
def NumberofPaths(a,b):
    return Euler.factorial(a + b) / (Euler.factorial(a) * Euler.factorial(b))


if __name__ == '__main__':
    start_time = time.time()
    print(NumberofPaths(20,20))
    print('{:2f} seconds'.format(time.time() - start_time))  



