# -*- coding: utf-8 -*-

# Project Euler
# Problem 027: Quadratic Primes
# Runtime : 2 seconds

import time
import Useful_Functions_PE as Euler

def QuadraticPrime(a,b):
    
    ReasonablePrimeList = Euler.PrimeList(a*100)

    dictofPrimes = {}
    for i in ReasonablePrimeList:
        if len(str(i)) in dictofPrimes.keys():
            dictofPrimes[len(str(i))].append(i)
        else:
            dictofPrimes[len(str(i))] = [i]
        

    Uptob_PrimeList = Euler.PrimeList(b + 1)
    consecutiveprime = 0

    for j in Uptob_PrimeList:
        print(j)
        for i in range(-j + 1,a):
            if (i + j + 1) > 1 :
                n = 0
                inPrime = True
                while inPrime:
                    evaluate = n * n + i * n + j
                    if evaluate in dictofPrimes[len(str(evaluate))]:
                        n += 1
                    else:
                        inPrime = False
                
                if n > consecutiveprime:
                    coefficient = i * j
                    a_coeff = i
                    b_coeff = j
                    consecutiveprime = n
    
    return coefficient, a_coeff, b_coeff, consecutiveprime
            


if __name__ == '__main__':
    start_time = time.time()
    print(QuadraticPrime(1000,1001))
    print('{:2f} seconds'.format(time.time() - start_time)) 