'''
Description: this file define a Gobang game class which control the basic game process
Date: 2022-04-11 10:33:06
LastEditTime: 2022-04-11 18:51:00
'''
from game.definitions import *
from game.common import *

#this class control the game process
class GobangGame:
    chessManual=[[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)] #the game manual record the whole game process
    curIndex=1 #the index of next run
    curPlayerType=GAME_HUMAN_MOVE
    print(chessManual)
    def __init__(self) -> None:
        self.restart()
    '''
    name: restart
    description: restart the whole game
    param {*} self
    '''        
    def restart(self) -> None:
        self.chessManual=[[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.curIndex=1
    '''
    name: endCheck
    description: check the game is over or not and return the result
    param {*} self
    return {*} the game result according to definitions.py
    '''    
    def end_check(self) -> int:
        return game_over_check(self.chessManual)

    '''
    name: get_cur_player_type
    description: get the type of current player
    param {*} self
    return {*} GAME_HUMAN_MOVE or GAME_AI_MOVE
    '''    
    def get_cur_player_type(self) -> int:
        return self.curPlayerType

    def get_cur_player_number(self) -> int:
        return self.curIndex

def main():
    game=GobangGame()
    print(game.chessManual)
    print(game.curIndex)

if __name__ == '__main__':
    main()