from __future__ import print_function
import random
import os
import sys
import numpy as np 


'''This code is a test code to check how
tic tac toe can be implemented using the minimax algorithm'''

#board = [i for i in range(9)]
board = ["o", "x","o", "x", "x","x","o","o","x"]
def display_current_board(board):
    '''This function displays the board to the user
    depending upon the current state of the board'''

    for row in range(3):
        for col in range(4):
            if (col) // 3 == 1:
                print()
                print("--------")
            else:
                print(str(board[3*row + col]), end="|")
def diagonal_check(board):
    '''Checks the diagonal value in the board'''
    i = 0
    if board[i][i] == board[i+1][i+1] and board[i+1][i+1] == board[i+2][i+2]:
        return True
    elif board[i][i+2] == board[i+1][i+1] and  board[i+1][i+1] == board[i+2][i]:
        return True
    else:
        return False
def horizontal_check(board):
    '''Checks the horizontal value in the board'''
    
    for i in range(3):   
        if board[i][i] == board[i][1] and board[i][1] == board[i][2]:
            return (True, board[i][i])
    else:
        return (False, -1)
        

def vertical_check(board):
    '''Checks the vertical value in the board'''
    for i in range(3):
        
        if board[i][i] == board[1][i] and board[1][i] == board[2][i]:
            return (True, board[i][i] )
    else:
        return (False, -1)
        
def check_board(board):
    '''This function checks the board's positions and see 
    if any one of them have won it already or not. In a 3*3
    matrix, we check row and diagonal positions.
    like 0,4,8; 0, 1, 2; 0,3,6'''
    board = np.reshape(board, (3,3))
    (h_bool, player_h) = horizontal_check(board)
    (v_bool, player_v) = vertical_check(board)
    if diagonal_check(board):
        print("Player {0} won the game".format(board[1][1]))
    elif h_bool:
        
        print("Player {0} won the game".format(player_h))
    elif v_bool:
        print("Player {0} won the game".format(player_v))
    
    
if __name__ == "__main__":
    display_current_board(board)
    check_board(board)
                



    