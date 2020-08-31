# -*- coding: utf-8 -*-

# Project Euler
# Problem 013: Large Sum
# Runtime : 0 ms

import time

filename = 'PE_013_grid.txt'

def LargeSum(filename,digits):
    with open(filename) as f:
        for line in f:       
            # Since only first ten digits are asked in the problem, and there are 100 numbers, any digits after the first 10 + log(100) are not important.
            grid = [int(i.split()[0][0:(digits + 2)]) for i in f.readlines()]

    return str(sum(grid))[0:digits]

       
if __name__ == '__main__':
    start_time = time.time()
    print(LargeSum(filename,10))
    print('{:2f} seconds'.format(time.time() - start_time)) 
