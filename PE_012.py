# -*- coding: utf-8 -*-

# Project Euler
# Problem 012: Highly divisible triangular number
# Runtime : 12.2 seconds

import time
import Useful_Functions_PE as Euler

def First_n_divisors(num_of_divisors):    
    div_list = []
    iteration = 0
    while (len(div_list) * 2 < num_of_divisors):
        iteration += 1
        div_list = Euler.DivisorFactors(Euler.TriangularNumber(iteration))
    return iteration, Euler.TriangularNumber(iteration)

if __name__ == '__main__':
    start_time = time.time()
    print(First_n_divisors(500))
    print('{:2f} seconds'.format(time.time() - start_time))