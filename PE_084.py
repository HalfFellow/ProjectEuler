# -*- coding: utf-8 -*-

# Project Euler
# Problem 084: Monopoly Odds
# Runtime : 3.65 seconds (1,000,000 simulations)

import random
import time

class Monopoly():
    
    def __init__(self):
        self.board = [i for i in range(40)]
        self.dice = [i for i in range(1,5)]
        self.community = [i for i in range(1,17)]
        self.chance = [i for i in range(1,17)]
        self.communitysquares = [2,17,33]
        self.chancesquares = [7,22,36]
        self.g2jsquare = [30]
        self.jailsquare = [10]
        self.railroads = [5,15,25,35]
        self.consecutivedoubles = 0
        self.currenttile = 0
        
        self.freq = {}
        
        self.max_iter = 1000000
        self.End = False
        
    def dice_throw(self):
        return random.choice(self.dice), random.choice(self.dice)
    
    def isDouble(self,dice1,dice2):
        if (dice1 == dice2):
            self.consecutivedoubles += 1
        else:
            self.consecutivedoubles = 0
    
    def PlayerAdvance(self,dice1,dice2):
        self.currenttile += dice1 + dice2
        self.currenttile = self.currenttile % 40
    
    def GoToJail(self):
        if self.consecutivedoubles == 3:
            self.currenttile = 10
            self.consecutivedoubles = 0
        elif self.currenttile == 30:
            self.currenttile = 10
        else:
            pass


   
    def Community(self):
        
        card = self.community[0]
        
        self.community = self.community[1:] + [self.community[0]]
        
        if (card == 1):
            self.currenttile = 0
        elif (card == 2):
            self.currenttile = 10
        else:
            pass


    
    def Chance(self):
        
        card = self.chance[0]
        
        self.chance = self.chance[1:] + [self.chance[0]]
        
        if (card == 1):
            self.currenttile = 0
        elif (card == 2):
            self.currenttile = 10
        elif (card == 3):
            self.currenttile = 11
        elif (card == 4):
            self.currenttile = 24
        elif (card == 5):
            self.currenttile = 39
        elif (card == 6):
            self.currenttile = 5
        elif (card in (7,8)):
            if (self.currenttile == 7):
                self.currenttile = 15
            elif (self.currenttile == 22):
                self.currenttile = 25
            else:
                self.currenttile = 5
        elif (card == 9):
            if (self.currenttile in (7,36)):
                self.currenttile = 12
            else:
                self.currentile = 28
        elif (card == 10):
            self.currenttile -= 3
        else:
            pass

    def Endgame(self,iterations):
        if (iterations == self.max_iter):
            self.End = True
        else:
            pass

'Main Routine'

if __name__ == '__main__':
    start_time = time.time()
    
    Game = Monopoly()
    
    iter_count = 0
    
    while (Game.End == False):
        dice1, dice2 = Game.dice_throw()
        Game.isDouble(dice1,dice2)
    
        Game.PlayerAdvance(dice1,dice2)
        Game.GoToJail()
        
        if Game.currenttile in Game.chancesquares:
            Game.Chance()    
        if Game.currenttile in Game.communitysquares:
            Game.Community()
    
            
        if '{}'.format(Game.currenttile) in Game.freq:
            Game.freq['{}'.format(Game.currenttile)] += 1
        else:
            Game.freq['{}'.format(Game.currenttile)] = 1
        
        iter_count += 1
        Game.Endgame(iter_count)
    
    a = sorted((Game.freq).items(),key=lambda x: x[1], reverse = True)
    print ([str(tile) for tile,freq in a[:3]])

    print('{:2f} seconds'.format(time.time() - start_time))  

    


    