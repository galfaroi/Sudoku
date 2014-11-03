Sudoku
======

This Sudoku solver uses Backtracking for solving, it is programed in Python and uses Numpy narray as main data structure for the board. 

For running in your command line:

$python solvering.py

Assuming you have pre installed Python. This was created with Python Enthought distro in a Ubuntu 12.04 machine, it has Numpy as dependency. The Sudoku to solve is a .csv file that has to be in the same directory. 

    '''python

    #load numpy array from csv two default options of games
    #arr=np.loadtxt('sudoeasy.csv', delimiter=',')
    #arr=np.loadtxt('sudoku.csv', delimiter=',')
    arr=np.loadtxt('unsolvable.csv', delimiter=',')
    
    '''
