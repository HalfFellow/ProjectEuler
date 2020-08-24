# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Project Euler
# Problem 55: Lychrel Numbers


def LychrelNumber(UpTo,max_iter):
    '''
    UpTo : Maximum number to test
    max_iter : Number of iterations before the algorithm stops and defines a
    number as a Lychrel Number
    '''
    
    Lychrel = []
    
    for i in range(1,UpTo+1):
        
        number = i
        iteration = 0
        PalyndromeFound = False
        
        while (iteration < max_iter) and not PalyndromeFound:
            number += int(str(number)[::-1])
            if (number == int(str(number)[::-1])):
                PalyndromeFound = True
            iteration += 1
                
        if not PalyndromeFound:
            Lychrel.append(i)
            
    return len(Lychrel)


if __name__ == '__main__':
    print(LychrelNumber(10000,50))
