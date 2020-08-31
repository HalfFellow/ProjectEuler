# -*- coding: utf-8 -*-

# Project Euler
# Problem 011: Largest Product in a grid
# Runtime : 0 ms

# Assumption that grid submitted is a square grid

import time

filename = 'PE_011_grid.txt'
grid = []

with open(filename) as f:
    for line in f:
        grid.append([int(i) for i in line.split()])


def LargestProductGrid(grid,consecutive):
    LargestProduct = 0
    
    for i in range(len(grid) - (consecutive - 1)):

        for j in range(len(grid)):
            
            Product = grid[j][i] * grid[j][i + 1] * grid[j][i + 2] * grid[j][i + 3]
            if (Product > LargestProduct):
                LargestProduct = Product
                
            Product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            if (Product > LargestProduct):
                LargestProduct = Product
            
            if j < 17:
                Product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
                if (Product > LargestProduct):
                    LargestProduct = Product
            
            if (i > 3) and (j < 17):
                Product = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
                if (Product > LargestProduct):
                    LargestProduct = Product
                
            

    return LargestProduct        
    
if __name__ == '__main__':
    start_time = time.time()
    print(LargestProductGrid(grid,4))
    print('{:2f} seconds'.format(time.time() - start_time)) 

