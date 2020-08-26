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


def isPalindrome(number):
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


def CompletePrimeFactors(Number):
    
    Prime_to_test = PrimeList(Number)
    print(Prime_to_test)
    Prime_Factors = []
    i = 0
    
    while Number != 1:
        if Number % Prime_to_test[i] == 0:
            Prime_Factors.append(Prime_to_test[i])
            Number /= Prime_to_test[i]
            i = 0
        else:
            i += 1
    
    return Prime_Factors


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
    
def sumofdigits(x):
    return sum([int(i) for i in str(x)])


def Fibonacci_NthTerm(nth):
        
    a_n1 = 1
    a_n0 = 1
        
    if (nth == 1):
        return a_n0
    elif (nth == 2):
        return a_n1
    else:
        i = 2
        while i < nth:
            a_ntemp = a_n1
            a_n1 = a_n0 + a_n1
            a_n0 = a_ntemp
            i += 1
            
        return a_n1
        
def Fibonacci_nTermList(n):
        
    a_n1 = 1
    a_n0 = 1
        
    termlist = []
        
    if (n == 1):
        termlist.append(a_n0)
        return termlist
    elif (n == 2):
        termlist.append(a_n0)
        termlist.append(a_n1)
        return termlist
    else:
        termlist.append(a_n0)
        termlist.append(a_n1) 
        i = 2
        while i < n:
            a_ntemp = a_n1
            a_n1 = a_n0 + a_n1
            a_n0 = a_ntemp
            termlist.append(a_n1)
            i += 1
                
        return termlist
        
def Fibonacci_TermListUpTo(bound):
    a_n1 = 1
    a_n0 = 1
        
    termlist = []
        
    if (bound == 1):
        termlist.append(a_n0)
        return termlist
    elif (bound == 2):
        termlist.append(a_n0)
        termlist.append(a_n1)
        return termlist
    else:
        termlist.append(a_n0)
        termlist.append(a_n1)            
        while a_n1 < bound:
            a_ntemp = a_n1
            a_n1 = a_n0 + a_n1
            a_n0 = a_ntemp
                
            if a_n1 < bound:
                termlist.append(a_n1)
            
        return termlist   
    
def TriangularNumber(number):
    return number * (number + 1) / 2

def DivisorFactors(number):
    return [i for i in range(1, int(((number + 1) ** 0.5) // 1)) if int(number) % i == 0]