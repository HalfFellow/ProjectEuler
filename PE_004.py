# -*- coding: utf-8 -*-

# Project Euler
# Problem 004: Largest Palindrom Product
# Runtime : 415 ms

import time
import Useful_Functions_PE as Euler

def LargestPalindrome(Numofdigit):    
    FirstTerm = 10 ** Numofdigit - 1
    Smallest = 10 ** (Numofdigit - 1) - 1
    MaxPalindrome = 0
    
    while (FirstTerm > Smallest):
        
        SecondTerm = FirstTerm - 1
        
        while (SecondTerm > Smallest):
            
            Test = FirstTerm * SecondTerm
            
            if ((Euler.isPalindrome(Test)) and (MaxPalindrome < Test)):
                MaxPalindrome = Test
                Num1 = FirstTerm
                Num2 = SecondTerm
                
            SecondTerm -= 1
        
        FirstTerm -= 1
        
    return MaxPalindrome, Num1, Num2, Numofdigit

if __name__ == '__main__':
    start_time = time.time()
    Palindrome, num1, num2, numofdigit = LargestPalindrome(3)
    print("{}, which is the product of {} and {}, is the largest palindrome made from the product of two {}-digit numbers".format(Palindrome,num1,num2,numofdigit))
    print('{:2f} seconds'.format(time.time() - start_time)) 

        