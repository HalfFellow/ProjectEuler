# -*- coding: utf-8 -*-

# Project Euler
# Problem 017: Number letter counts
# Runtime : 6 ms

#Only problem which I didn't bother to optimize or test very much beyond the scope of the problem (letters in numbers from 1 to 1000).

import time

def Nbcar(From,Upto):
    
    #Function only has been verified for up to one thousand. 
    
    
    dictionary_unit = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:''}
    dictionary_counter = {6:'hundredthousand',4:['thousand'],3:['hundred','hundredand']}
    dictionary_dizaine = {1:{0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'},2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:''}
    nbcar = 0
    
    for i in range(From,Upto+1):
         
        if (len(str(i)) >= 2) and str(i)[-2] == '1':
            nbcar += len(dictionary_dizaine[1][int(str(i)[-1])])
        elif (len(str(i)) >= 2) and str(i)[-2] != '1':
            nbcar += len(dictionary_dizaine[int(str(i)[-2])])
            nbcar += len(dictionary_unit[int((str(i)[-1]))])     
        
        if int(len(str(i))) in dictionary_counter.keys():
            nbcar += len(dictionary_unit[int(str(i)[0])])
            if str(i)[-2:] != "00":
                
                nbcar += len(dictionary_counter[len(str(i))][1])
            else:
                print(i)
                nbcar += len(dictionary_counter[len(str(i))][0])            
        
        if len(str(i)) == 1:
            nbcar += len(dictionary_unit[int((str(i)[-1]))])
             
    return nbcar


if __name__ == '__main__':
    start_time = time.time() 
    print(Nbcar(1,1000))
    print('{:2f} seconds'.format(time.time() - start_time)) 