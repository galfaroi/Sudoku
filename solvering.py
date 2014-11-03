#import pdb
import numpy as np

def main():
 
#load numpy array from csv two default options of games
    #arr=np.loadtxt('sudoeasy.csv', delimiter=',')
    arr=np.loadtxt('sudoku.csv', delimiter=',')

#cast the array to int for efficiency  and leave original array inmutable
    board=arr.astype(int)
    global row, col
    row=0; col=0; 

    
 #check for correct board size
    assert arr.size  == 81
   
    print "Sudoku to solve:"
    print board
    print ""
  
    if solve(board,row, col)  == True:
        print "Solution:"
	print board
    else: 
        print "no solution"

#looks for blanks (0's)
def findBlanks(board, row, col):
   nx, ny = board.shape
  
   for row in xrange(0, nx):
       for col in xrange(0, ny):
          if  board[row,col] == 0 :
              
               return row, col
   return False 

#check if is not collision in the row with the same number
def checkRow(board, row, num):

    slice = board[row,0:9]
  
    for x in slice:
         if x == num:
             return True
         
    return False

#checks for column for collision with the same number 
def checkCol(board, col, num):
    slice = board[0:9,col]
    
    for x in slice:
         if x == num:
             return True
    return False

def checkBox(board, rowpos, colpos, num):
    #pdb.set_trace()
    for row in xrange(0, 3):
       for col in xrange(0, 3):
          if board[row+rowpos][col+colpos] == num :
              return True
    return False

def checks(board, row, col, num):

    return not checkRow(board, row, num) and not checkCol(board, col, num) and not checkBox(board, row-(row%3), col-(col%3), num)
  

def solve(board, row, col):
  
    row
    col

    if not findBlanks(board, row, col):
	return True
   
    find = findBlanks(board, row, col)
        
    row=find[0]; col=find[1]
   
        #start trying numbers in blanks
    for num in xrange(1,10):
    

            #checks if is valid
            if checks(board, row, col, num):

                board[row,col] = num

                if solve(board, row, col):
	    #if solve(board):
                    return True

                board[row,col] = 0

     
       
    return False

if __name__ == "__main__":
   main()
