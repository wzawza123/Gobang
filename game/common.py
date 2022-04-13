'''
Description: this file define some common functions that are used in the game
Date: 2022-04-11 10:33:41
LastEditTime: 2022-04-13 17:28:47
'''
from game.definitions import *

'''
name: game_over_check
description: check whether the game is over and return the result
param {list} board_state in list format distinguished by odd and even
return {int} the game result, following the definitions in definitions.py
'''
def game_over_check(board_state:list[list[int]])->int:
    boardFull = True
    dirVecX=[1,0,1,-1] #the vector of direction in x-axis in checking: row column diagnoal anti-diagnoal
    dirVecY=[0,1,1,1]
    #check all
    #iteration between directions
    for dirIndex in range(len(dirVecX)):
        #iteration the start position
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                flagOdd=True
                flagEven=True
                #iteration the length of the line
                for num in range(5):
                    #out of boundary check
                    if i+dirVecX[dirIndex]*num>=BOARD_HEIGHT or j+dirVecY[dirIndex]*num>=BOARD_WIDTH or i+dirVecX[dirIndex]*num<0 or j+dirVecY[dirIndex]*num<0:
                        flagOdd=False
                        flagEven=False
                        break
                    #check the space
                    if board_state[i+dirVecX[dirIndex]*num][j+dirVecY[dirIndex]*num]==SPACE_NUMBER:
                        boardFull=False
                        flagOdd=False
                        flagEven=False
                        break
                    #check odd win
                    if board_state[i+dirVecX[dirIndex]*num][j+dirVecY[dirIndex]*num]%2==0:
                        flagOdd=False
                    #check even win
                    elif board_state[i+dirVecX[dirIndex]*num][j+dirVecY[dirIndex]*num]%2==1:
                        flagEven=False
                if flagOdd:
                    return GAME_END_ODD_WIN
                if flagEven:
                    return GAME_END_EVEN_WIN
    #check draw
    if boardFull:
        return GAME_END_DRAW
    return GAME_STILL_PLAYING