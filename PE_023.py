# -*- coding: utf-8 -*-

# Project Euler
# Problem 023: Non-abundant sums
# Runtime : 6 seconds

import time
import Useful_Functions_PE as Euler

def isAbundantNumber(number):
    if (sum(Euler.ProperDivisorFactors(number)) > number):
        return True
    else:
        return False

def AbundantNumbersList(From,UpTo):
    Abundant_List = []
    
    for i in range(From,UpTo+1):
        if isAbundantNumber(i):
            Abundant_List.append(i)
    
    return Abundant_List

def AbundantNumbersSum(x):
    AbundantSum_List = []
    
    for i in range(0,len(x)):
        for j in range(i,len(x)):
            AbundantSum_List.append(x[i] + x[j])
    
    return set(AbundantSum_List)

if __name__ == '__main__':
    start_time = time.time()
    AbundantNum_List = AbundantNumbersList(1,28124)
    print(AbundantNum_List)
    AbundantNum_Sum  = AbundantNumbersSum(AbundantNum_List)
    Int_noabundantsum = [i for i in range(28124) if i not in AbundantNum_Sum]
    print(sum(Int_noabundantsum))
    print('{:2f} seconds'.format(time.time() - start_time)) 

            
    
            
