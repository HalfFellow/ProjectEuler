# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:38:23 2020

@author: lemax
"""
import math

def factorial(x):
    if (x == 1):
        return 1
    else:
        return x * factorial(x - 1)


def isPalyndrome(number):
    return str(number) == str(number)[::-1]

   
def PrimeList(Bound):
    """ Using Sieve of Eratosthenes in order to extract the list """
    MarkedList = [i for i in range(2,Bound+1)]
        
    p = 2
    initial_pos = 0
    
    while (initial_pos < (Bound - 1)):    
        for k in range(2,(Bound+1)//p+1):
            if (k * p - 2 < Bound - 1):
                MarkedList[k*p-2]=0
        
        initial_pos += 1
        new_p = False
        
        while (initial_pos < (Bound - 1)) and not new_p:
            if (MarkedList[initial_pos] > 0):
                p = MarkedList[initial_pos]
                new_p = True
            else:
                initial_pos += 1
        
    FinalList = [i for i in MarkedList if (i != 0)]    
            
    return FinalList


def UniquePrimeFactors(Number):
    PrimeList1 = PrimeList(int(Number ** 0.5 // 1))
    
    return [prime for prime in PrimeList1 if (Number % prime) == 0]


def nthPrime(nth): 
    if nth == 1:
        return 2
    else:
        ln = math.log(nth)
        lln = math.log(math.log(nth))
    
    if (nth >= 688383):
        upper = nth * (ln + lln - 1 + (lln - 2) / ln)
    elif (nth >= 178974):
        upper = nth * (ln + lln - 1 + (lln - 1.95) / ln)
    elif (nth > 39017):
        upper = nth * (ln + lln - 0.9484)
    elif (nth > 5):
        upper = nth * (ln + 0.6 * lln)
    else:
        pass
    
    if nth < 6:
        small_prime = [2,3,5,7,11]
        return small_prime[nth - 1]
    else:
        return PrimeList(int(math.ceil(upper)))[nth - 1]