'''
Description: 
Date: 2022-04-11 10:33:06
LastEditTime: 2022-05-03 15:17:00
'''
"""
Description: this file defines a Gobang game class which control the basic game process
Date: 2022-04-11 10:33:06
LastEditTime: 2022-04-13 21:02:04
"""
from game.Valuation_Basic import Valuation_Basic
from game.definitions import *
from game.common import *
from game.Search import *
from game.Search_Fast import *


# this class control the game process
class GobangGame:
    chessManual = [[0 for i in range(BOARD_WIDTH)] for j in
                   range(BOARD_HEIGHT)]  # the game manual record the whole game process
    curIndex = 1  # the index of next run
    curPlayerType = GAME_HUMAN_MOVE
    firstPlayerType=GAME_HUMAN_MOVE
    curGameMode=""
    searching_class_odd=0
    searching_class_even=0
    evalView=None
    evalClass=Valuation_Basic()
    def __init__(self) -> None:
        self.restart()

    def restart(self) -> None:
        """
        reset the game
        Returns:None

        """
        self.chessManual = [[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.curIndex = 1
        if self.curGameMode == "HUMAN_VS_HUMAN":
            self.curPlayerType = GAME_HUMAN_MOVE

    def end_check(self) -> int:
        """
        check whether the game is over
        Returns: the result as is defined in definitions.py

        """
        return game_over_check(self.chessManual)

    def get_cur_player_type(self) -> int:
        """
        get the current player type
        Returns: the current player type

        """
        return self.curPlayerType

    def get_cur_player_number(self) -> int:
        '''
        description: 
        param {*}
        return {*}
        '''             
        return self.curIndex

    def display_chessmanual(self) -> None:
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                print(self.chessManual[i][j], end=" ")
            print()
        print()

    def update_human_move(self, row: int, col: int) -> None:
        """
        update the game process by human move
        Args:
            x: the x coordinate of the chessman
            y: the y coordinate of the chessman

        Returns: the result of end check after the move

        """
        assert (0 <= row < BOARD_HEIGHT and 0 <= col < BOARD_WIDTH and self.get_cur_player_type() == GAME_HUMAN_MOVE)
        self.chessManual[row][col] = self.curIndex
        # update the game
        game_result = self.update_game_turn_forward()

    def update_ai_move(self)->None:
        """
        update the game process by ai move
        Returns:None

        """
        assert (self.get_cur_player_type() == GAME_AI_MOVE)
        print("start searching")
        if self.curIndex%2==1:
            self.searching_class_odd.Direction(self.chessManual,self.curIndex);
            next_step=self.searching_class_odd.nextStep
        else:
            self.searching_class_even.Direction(self.chessManual,self.curIndex);
            next_step=self.searching_class_even.nextStep
        self.chessManual[next_step[0]][next_step[1]] = self.curIndex
        print("next step:",next_step)
        self.update_game_turn_forward()

    def update_game_turn_forward(self) -> int:
        """
        update the game process
        Returns:the end check result

        """
        self.update_eval_view()
        self.curIndex += 1
        if self.curGameMode == "HUMAN_VS_HUMAN":
            # no need to change the player type
            pass
        elif self.curGameMode == "HUMAN_VS_AI":
            if self.curPlayerType == GAME_HUMAN_MOVE:
                self.curPlayerType = GAME_AI_MOVE
            else:
                self.curPlayerType = GAME_HUMAN_MOVE
        elif self.curGameMode == "AI_VS_AI":
            pass
        self.display_chessmanual()
        end_result = self.end_check()
        if end_result == GAME_STILL_PLAYING:
            return end_result
            pass
        else:
            return end_result

    def update_game_turn_backward(self):
        if self.curGameMode=="HUMAN_VS_HUMAN":
            pass
        elif self.curGameMode=="HUMAN_VS_AI":
            if self.curPlayerType==GAME_HUMAN_MOVE:
                self.curPlayerType=GAME_AI_MOVE
            else:
                self.curPlayerType=GAME_HUMAN_MOVE
        else:
            pass
        self.display_chessmanual()
        pass

    def undo_move(self) -> bool:
        """
        undo the last move
        Returns:whether undo successfully

        """
        if self.curIndex > 1:
            self.curIndex -= 1
            pos = get_position_by_number(self.chessManual, self.curIndex)
            print("will undo: ", self.curIndex)
            assert (pos[0] != -1 and pos[1] != -1)
            self.chessManual[pos[0]][pos[1]] = 0
            self.update_game_turn_backward()
            return True
        else:
            # nothing has been done yet
            return False

    def stop_game_process(self) -> None:
        """
        stop the game process
        Returns:None

        """
        self.curPlayerType = GAME_NO_ONE_MOVE

    def select_game_mode_pvp(self) -> None:
        """
        select game mode as pvp
        Returns:None

        """
        self.curGameMode = "HUMAN_VS_HUMAN"
    
    def select_game_mode_pvai(self,first_to_go,algorithm_name) -> None:
        """
        select game mode as pvai
        Returns:None

        """
        self.curGameMode = "HUMAN_VS_AI"
        self.curPlayerType = first_to_go
        if algorithm_name=="faster":
            target_alg_class=Search_Fast()
        else:
            target_alg_class=Search()
        if first_to_go == GAME_HUMAN_MOVE:
            self.searching_class_even=target_alg_class;
            self.firstPlayerType=GAME_HUMAN_MOVE
        else:
            self.searching_class_odd=target_alg_class;
            self.firstPlayerType=GAME_AI_MOVE

    def bind_eval_view(self,evalView):
        self.evalView=evalView
    
    def update_eval_view(self):
        if self.evalView!=None:
            eval_result=self.evalClass.Valuation(self.chessManual,self.curIndex)
            self.evalView.insert(eval_result)

def main():
    game = GobangGame()
    # game.display_chessmanual()
    # print(game.chessManual)
    # print(game.curIndex)


if __name__ == '__main__':
    main()
