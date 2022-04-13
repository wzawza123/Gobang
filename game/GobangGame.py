'''
Description: this file define a Gobang game class which control the basic game process
Date: 2022-04-11 10:33:06
LastEditTime: 2022-04-13 18:37:58
'''
from game.definitions import *
from game.common import *

#this class control the game process
class GobangGame:
    chessManual=[[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)] #the game manual record the whole game process
    curIndex=1 #the index of next run
    curPlayerType=GAME_HUMAN_MOVE
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
    
    def display_chessmanual(self) -> None:
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                print(self.chessManual[i][j],end=" ")
            print()
        print()
    '''
    name: update_human_move
    description: 
    param {*} self
    param {int} x
    param {int} y
    return {*}
    '''    
    def update_human_move(self,x:int,y:int) -> None:
        assert(x>=0 and x<BOARD_WIDTH and y>=0 and y<BOARD_HEIGHT and self.get_cur_player_type()==GAME_HUMAN_MOVE)
        self.chessManual[x][y]=self.curIndex
        self.curIndex+=1
    '''
    name: 
    description: 
    param {*} self
    return {*} the game result
    '''    
    def update_game_turn(self)-> int:
        end_result=self.end_check()
        if end_result==GAME_STILL_PLAYING:
            # self.curPlayerType=GAME_AI_MOVE if self.curPlayerType==GAME_HUMAN_MOVE else GAME_HUMAN_MOVE    
            return end_result
            pass
        else:
            return end_result
    '''
    name: stop game process
    description: simply stop game process
    param {*} self
    return {*}
    '''    
    def stop_game_process(self)-> None:
        self.curPlayerType=GAME_NO_ONE_MOVE
def main():
    game=GobangGame()
    # game.display_chessmanual()
    # print(game.chessManual)
    # print(game.curIndex)

if __name__ == '__main__':
    main()