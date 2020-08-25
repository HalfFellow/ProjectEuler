# -*- coding: utf-8 -*-

# Project Euler
# Problem 005: Smallest Multiple
# Runtime : 1 ms

import time
import Useful_Functions_PE as Euler

def MultiplyList(x):
    Result = 1
    for i in x:
        Result *= i
        
    return Result


def SmallestMultiple(LowBound, UpBound):
    
    max_primecount = {}
    
    for integer in range(LowBound, UpBound+1):
        PrimeFactors = Euler.CompletePrimeFactors(integer)
        Unique_PrimeFactors = set(PrimeFactors)
        
        for i in Unique_PrimeFactors:
            if i not in max_primecount:
                max_primecount[i] = PrimeFactors.count(i)
            elif PrimeFactors.count(i) > max_primecount[i]:
                max_primecount[i] = PrimeFactors.count(i)
        

    return MultiplyList([base ** exponent for base, exponent in max_primecount.items()])


if __name__ == "__main__":
    start_time = time.time()
    print(SmallestMultiple(1,20))
    print('{:2f} seconds'.format(time.time() - start_time)) 


    
    
    