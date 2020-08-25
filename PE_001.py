# -*- coding: utf-8 -*-

# Project Euler
# Problem 001: Multiples of Three and Five
# Runtime : 0 ms

import time

def SumOfMultiples(mult1,mult2,bound):
    
    SumOfMult = 0
    
    for i in range(bound):
        if ((i % mult1 == 0) or (i % mult2 == 0)):
            SumOfMult += i
    
    return SumOfMult

if __name__ == "__main__":
    start_time = time.time()
    print(SumOfMultiples(3,5,1000))
    print('{:2f} seconds'.format(time.time() - start_time)) 