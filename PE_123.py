# -*- coding: utf-8 -*-

# Project Euler
# Problem 123: Prime Square Remainders
# Runtime : 61 s

import time
import Useful_Functions_PE as Euler

def PrimeSquareRemainders(Bound,FirstRemainderAbove):
    PrimeList = Euler.PrimeList(Bound)
    print('Prime List Generated')
    print(PrimeList)
    i = 7036                #since first at 10^9 is at 7037
    Remainder = 0
    
    while i < len(PrimeList) and Remainder < FirstRemainderAbove:
        i += 2
        Remainder = ((PrimeList[i] - 1) ** (i+1) + (PrimeList[i] + 1) ** (i+1)) % (PrimeList[i] ** 2)

        
    return i + 1

if __name__ == '__main__':
    start_time = time.time()
    print(PrimeSquareRemainders(10000000,10 ** 10))
    print('{:2f} seconds'.format(time.time() - start_time)) 