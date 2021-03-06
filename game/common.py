"""
Description: this file define some common functions that are used in the game
Date: 2022-04-11 10:33:41
LastEditTime: 2022-04-13 20:21:46
"""
from typing import Tuple
from game.definitions import *


def game_over_check(board_state: list[list[int]]) -> int:
    """
    check if the game is over
    Args:
        board_state: the board manual list

    Returns: whether the game is over, as is defined in definitions

    """
    boardFull = True
    dirVecX = [1, 0, 1, -1]  # the vector of direction in x-axis in checking: row column diagonal anti-diagonal
    dirVecY = [0, 1, 1, 1]
    # check all
    # iteration between directions
    for dirIndex in range(len(dirVecX)):
        # iteration the start position
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                flagOdd = True
                flagEven = True
                # iteration the length of the line
                for num in range(5):
                    # out of boundary check
                    if i + dirVecX[dirIndex] * num >= BOARD_HEIGHT or j + dirVecY[dirIndex] * num >= BOARD_WIDTH or i + \
                            dirVecX[dirIndex] * num < 0 or j + dirVecY[dirIndex] * num < 0:
                        flagOdd = False
                        flagEven = False
                        break
                    # check the space
                    if board_state[i + dirVecX[dirIndex] * num][j + dirVecY[dirIndex] * num] == SPACE_NUMBER:
                        boardFull = False
                        flagOdd = False
                        flagEven = False
                        break
                    # check odd win
                    if board_state[i + dirVecX[dirIndex] * num][j + dirVecY[dirIndex] * num] % 2 == 0:
                        flagOdd = False
                    # check even win
                    elif board_state[i + dirVecX[dirIndex] * num][j + dirVecY[dirIndex] * num] % 2 == 1:
                        flagEven = False
                if flagOdd:
                    return GAME_END_ODD_WIN
                if flagEven:
                    return GAME_END_EVEN_WIN
    # check draw
    if boardFull:
        return GAME_END_DRAW
    return GAME_STILL_PLAYING


def get_position_by_number(chess_manual: list[list[int]], number: int) -> Tuple[int, int]:
    """
    get the position of the chessman by its number
    Args:
        chess_manual: the chess manual list
        number: the number of the chessman to find

    Returns: the index of the chessman

    """
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if chess_manual[i][j] == number:
                return i, j
    return -1, -1
