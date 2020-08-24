# -*- coding: utf-8 -*-

# Project Euler
# Problem 55: Lychrel Numbers
# Runtime : 71 ms (.071 second)

import Useful_Functions_PE as Euler
import time

def LychrelNumber(UpTo,max_iter):
    '''
    UpTo : Maximum number to test
    max_iter : Number of iterations before the algorithm stops and defines a
    number as a Lychrel Number
    '''
    
    Lychrel = []
    
    for i in range(1,UpTo+1):
        
        iteration = 1
        number = i + int(str(i)[::-1])
        
        while (iteration < max_iter) and not Euler.isPalyndrome(number):
            number += int(str(number)[::-1])
            iteration += 1
            if Euler.isPalyndrome(number):
                break
                
        if not Euler.isPalyndrome(number):
            Lychrel.append(i)
            
    return len(Lychrel)


if __name__ == '__main__':
    start_time = time.time()
    print(LychrelNumber(10000,50))
    print('{} seconds'.format(time.time() - start_time))
