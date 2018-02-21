'''
This is a sudoku solver
Version 1.0
Author: Luocheng Huang
3/28/2016
'''

import time

class newMap():
    #Creating a new mapping for the sudoku
    def __init__ (self):
        #Creating a 9x9 matrix for which all cells are 0.
        self.v = [[0 for x in range(9)] for x in range (9)]
        self.tryList = []
        
    def print(self):
        #Prints the mapping
        for i in list(range(9)):
            print (self.v[i])
            
    def column(self, c):
        #Returns the c-th column of the mapping
        this = [0]*9
        for row in list(range(9)):
            this[row] = self.v[row][c]
        return this
    
    def grid(self, g):
        #Returns the list of the grid
        this = [0]*9
        x = (g//3)*3 #The starting row of the grid
        y = (g%3)*3  #'' '' column '' ''
        index = 0
        for row in list(range(x,x+3,1)):
            for column in list (range(y,y+3,1)):
                this[index] = self.v[row][column]
                index += 1
        return this

    def thereIs(self, row, col, number):
        #True there is a same number in the row, column, or grid
        g = row//3*3+col//3 #Grid number
        if self.v[row].count(number):
            return True
        elif self.column(col).count(number):
            return True
        elif self.grid(g).count(number):
            return True
        return False
        
    def findNext(self):
        #Start trying the next unknown and add the location
        #to the tryList stack
        #Returns the position if the next position is found
        #Returns 0 if next position is not found




        self.print()
        print('Solved!')
        return [-1,-1]
    
    def findPrev(self):
        #Subtract the current tryList stack
        #Returns the previous position if successful, [] if it's not found
        if len(self.tryList) == 1:
            print('No solution was found.')
            return[-1,-1]
        else:
            self.tryList.pop(len(self.tryList)-1)
            return self.tryList[len(self.tryList)-1]

    def tryNext(self, pos):
        #Try the next possible number given the position
        (row, col) = pos
        current = self.v[row][col]
        if current == 0:
            current = 1
        while current <= 9:
            if self.thereIs(row,col,current):
                current += 1
            else:
                return current
        return 0
        
    def solve(self):
        #Returns a solved solution or 'No Solution'
        pos = self.findNext()
        while pos != [-1,-1]: 
            (row,col) = pos
            number = self.tryNext(pos)
            self.v[row][col] = number
            if number != 0: #If there's no solution go back a stack
                pos = self.findNext()
            else: #If a solution is found, go to the next stack
                pos = self.findPrev()


def main():

    a = newMap()
    
    
    a.v[0] = [0,9,0,0,7,0,1,0,0]
    a.v[1] = [0,0,4,0,0,1,0,8,0]
    a.v[2] = [0,0,0,0,0,8,7,0,0]
    a.v[3] = [0,0,0,5,0,0,0,9,6]
    a.v[4] = [0,0,0,0,0,0,0,2,0]
    a.v[5] = [5,4,1,2,0,0,0,0,0]
    a.v[6] = [1,5,8,0,0,0,0,0,2]
    a.v[7] = [0,0,0,0,2,0,0,0,0]
    a.v[8] = [0,0,0,6,8,0,0,0,4]
    

    a.solve()


main()
