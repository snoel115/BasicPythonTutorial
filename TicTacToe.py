# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:27:12 2017

@author: snoel
"""

""" 
Tic Tac Toe game 

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
"""

from IPython.display import clear_output
#import random
gbExitRequested = False  #this will be a number between 1-9 or -99

""" **********************************************************
* Function: 
* Input   :
* Output  :
**************************************************************"""
def display_board(board):
    
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


""" **********************************************************
* Function: PositionTaken
* Input   :
* Output  :
**************************************************************"""    
def PositionTaken(board, pos = 1):
    if not board[pos] == ' ':
        print('Sorry the position is taken already, please chose something else')
        return True
    
    return False
    
    
""" **********************************************************
* Function: ChoseAPosition
* Input   :
* Output  :
**************************************************************"""    
def ChoseAPosition(board, playerName = ' ', sign = 'X'):
    print('Please ' + playerName + ' (' + sign +  '), chose a position between 1 and 9:')
    
    iPos = int(input())
    
    try:        
        if iPos >= 1 and iPos <= 9:
            if not PositionTaken(board, iPos):
                board[iPos] = sign
                return True  
        elif iPos == -99:
            global gbExitRequested
            gbExitRequested = True
                
    except ValueError:
        print('Please provide a number between 1 and 9')
    
    return False

""" **********************************************************
* Function: AllPositionTaken
* Input   :
* Output  :
**************************************************************"""   
def AllPositionTaken(board):
    for sign in board:
        if sign == ' ':
            return False
        
    return True

""" **********************************************************
* Function: WinnerBoard
* Input   :
* Output  :
**************************************************************"""        
def WinnerBoard(board, sPlayerName, mark):

    return ((board[7] == board[8] == board[9] == mark) or # across the top
    (board[4] == board[5] == board[6] == mark) or # across the middle
    (board[1] == board[2] == board[3] == mark) or # across the bottom
    (board[7] == board[4] == board[1] == mark) or # down the middle
    (board[8] == board[5] == board[2] == mark) or # down the middle
    (board[9] == board[6] == board[3] == mark) or # down the right side
    (board[7] == board[5] == board[3] == mark) or # diagonal
    (board[9] == board[5] == board[1] == mark)) # diagonal

            
""" **********************************************************
* Function: Main
* Input   :
* Output  :
**************************************************************"""

board = [' ']*10    #The list is set with 10 elements instead of 9 to allow the user to play between 1-9
board[0] = 'N/A'    #set this element to N/A to avoid it to be empty

clear_output()
print('Welcome to Tic Tac Toe!')
print ('This Tic Tac Toe is 3x3 as displayed below')

display_board(board)

#Gather users name
print('Please provide the name of the first player:' ) 
sPlayer1 = input()

print('Please provide the name of the second player:' ) 
sPlayer2 = input()

# loop until we find a winner or the exit code -99
while True:

    if not gbExitRequested:
        if not AllPositionTaken(board):
            while True:
                if ChoseAPosition(board, sPlayer1, 'O')  or gbExitRequested: 
                    break 
                
            display_board(board)
            if WinnerBoard(board, sPlayer1, 'O'): 
                print('We have a winner! Congratulation ' + sPlayer1)
                break
        else:
            print('Game over!')
            break
    
    if not gbExitRequested:
        if not AllPositionTaken(board):
            while True:
                if ChoseAPosition(board, sPlayer2, 'X') or gbExitRequested: 
                    break
                
            display_board(board)        
            if WinnerBoard(board, sPlayer2, 'X'):
                print('We have a winner! Congratulation ' + sPlayer2)
                break
        else:
            print('Game over!')
            break

    if gbExitRequested:
        print('You used the exit code to exit the game. Good bye')
        break
