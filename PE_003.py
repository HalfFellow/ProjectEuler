# -*- coding: utf-8 -*-

# Project Euler
# Problem 3: Largest Prime Factor
# Runtime : 1.96 s

import time
import Useful_Functions_PE as Euler


if __name__ == '__main__':
    start_time = time.time()
    print(sum(Euler.PrimeList(2000000)))
    print('{} seconds'.format(time.time() - start_time))