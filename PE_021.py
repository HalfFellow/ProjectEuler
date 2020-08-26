# -*- coding: utf-8 -*-

# Project Euler
# Problem 021: Amicable numbers
# Runtime : 5.7 seconds

import time
import Useful_Functions_PE as Euler

def AmicableNumber(number):
    Sumofdivisors = sum(Euler.ProperDivisorFactors(number))
    Sumofdivisorspair = sum(Euler.ProperDivisorFactors(Sumofdivisors))
    if ((number == Sumofdivisorspair) and (Sumofdivisors != number)):
        return True
    else:
        return False
    
def AmicableNumberList(Start,End):
    Amicable_list = []
    for i in range(Start,End+1):
        if AmicableNumber(i):
            Amicable_list.append(i)
    
    return Amicable_list

print(sum(AmicableNumberList(1,10000)))
            

if __name__ == '__main__':
    start_time = time.time()
    print(sum(AmicableNumberList(1,10000)))
    print('{:2f} seconds'.format(time.time() - start_time)) 