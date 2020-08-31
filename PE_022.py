# -*- coding: utf-8 -*-

# Project Euler
# Problem 022: Names Scores
# Runtime : 6 ms

import time

filename = 'PE_022_names.txt'
name_list = []
A_value = ord('A') - 1


with open(filename) as f:
    for line in f:
        name_list = [name.strip() for name in line.split(',')]

def NamesScores(name_list):
    name_list.sort()
    TotalScore = 0
    
    for name in range(len(name_list)):
        TotalScore += (sum([ord(letter) - A_value for letter in name_list[name]]) * (name + 1))

    return TotalScore   
    
if __name__ == '__main__':
    start_time = time.time()
    print(NamesScores(name_list))
    print('{:2f} seconds'.format(time.time() - start_time)) 
