"""
Description: this file defines a Gobang game class which control the basic game process
Date: 2022-04-11 10:33:06
LastEditTime: 2022-04-13 21:02:04
"""
from game.definitions import *
from game.common import *


# this class control the game process
class GobangGame:
    chessManual = [[0 for i in range(BOARD_WIDTH)] for j in
                   range(BOARD_HEIGHT)]  # the game manual record the whole game process
    curIndex = 1  # the index of next run
    curPlayerType = GAME_HUMAN_MOVE

    def __init__(self) -> None:
        self.restart()

    def restart(self) -> None:
        """
        reset the game
        Returns:None

        """
        self.chessManual = [[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.curIndex = 1

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
        return self.curIndex

    def display_chessmanual(self) -> None:
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                print(self.chessManual[i][j], end=" ")
            print()
        print()

    def update_human_move(self, x: int, y: int) -> None:
        """
        update the game process by human move
        Args:
            x: the x coordinate of the chessman
            y: the y coordinate of the chessman

        Returns: the result of end check after the move

        """
        assert (0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT and self.get_cur_player_type() == GAME_HUMAN_MOVE)
        self.chessManual[x][y] = self.curIndex
        self.curIndex += 1
        # update the game
        game_result = self.update_game_turn_forward()

    def update_game_turn_forward(self) -> int:
        """
        update the game process
        Returns:the end check result

        """
        self.display_chessmanual()
        end_result = self.end_check()
        if end_result == GAME_STILL_PLAYING:
            # self.curPlayerType=GAME_AI_MOVE if self.curPlayerType==GAME_HUMAN_MOVE else GAME_HUMAN_MOVE
            return end_result
            pass
        else:
            return end_result

    def update_game_turn_backward(self):
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


def main():
    game = GobangGame()
    # game.display_chessmanual()
    # print(game.chessManual)
    # print(game.curIndex)


if __name__ == '__main__':
    main()
