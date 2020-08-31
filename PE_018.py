# -*- coding: utf-8 -*-

# Project Euler
# Problem 018: Maximum Path Sum I
# Runtime : 0 ms

import time

filename = 'PE_018_grid.txt'
int_list = []

with open(filename) as f:
    for line in f:
        int_list.append([int(i) for i in line.split()])


def LargestSumPath(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])

    return triangle[0][0]        
    
if __name__ == '__main__':
    start_time = time.time()
    print(LargestSumPath(int_list))
    print('{:2f} seconds'.format(time.time() - start_time)) 