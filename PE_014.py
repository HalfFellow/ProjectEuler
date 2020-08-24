# -*- coding: utf-8 -*-

# Project Euler
# Problem 014: Longest Collatz Sequence
# Runtime : 1.81 second

import time

def LongCollatzSeq(LowerBound,UpperBound):
    

    TryList = [i for i in range(LowerBound,UpperBound)]
    iteration = 0
    LongestChain = 0
    
    #Dictionary which keeps track of chain length for tried values
    ChainLength_Dict = {}
    
    while iteration < len(TryList):
        
        number = TryList[iteration]
        number_temp = number
        ChainLength = 1
        
        while number != 1:
            
            ChainLength += 1
            
            if number % 2 == 0:
                number //= 2
    
            elif number % 2 == 1:
                #Since n = 3n + 1 always gives even, two steps at once
                number = (3 * number + 1)//2
                ChainLength += 1
            
            if number in ChainLength_Dict.keys():
                #If number already visited, chain length known
                ChainLength = ChainLength + ChainLength_Dict[number] - 1
                number = 1
         
        if (ChainLength > LongestChain):
            LongestChain = ChainLength
            LongestNum = TryList[iteration]
        
        ChainLength_Dict[number_temp] = ChainLength
        
        iteration += 1
        
    return LongestNum, LongestChain


if __name__ == '__main__':
    start_time = time.time()
    print(LongCollatzSeq(1,1000000))
    print('{:2f} seconds'.format(time.time() - start_time))   