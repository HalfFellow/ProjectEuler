# -*- coding: utf-8 -*-

# Project Euler
# Problem 006: Sum Square Difference
# Runtime : 1 ms

import time

def sumofsquares(n):
    return sum([i ** 2 for i in range(n + 1)])

def squareofsum(n):
    return sum([i for i in range(n + 1)]) ** 2


if __name__ == '__main__':
    start_time = time.time()
    print(squareofsum(100) - sumofsquares(100))
    print('{:2f} seconds'.format(time.time() - start_time)) 
