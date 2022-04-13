'''
Description: this file define some basic constant variables for the game
Date: 2022-04-11 10:34:14
LastEditTime: 2022-04-13 11:02:44
'''
#the board size definitions
BOARD_HEIGHT=15
BOARD_WIDTH=15
#the chessman number definitions
SPACE_NUMBER=0

#game result definitions
GAME_END_ODD_WIN=1
GAME_END_EVEN_WIN=2
GAME_END_DRAW=0
GAME_STILL_PLAYING=3

GAME_AI_MOVE=2
GAME_HUMAN_MOVE=1

#visualization constants
#FPS
FPS=20
#sizes
WINDOW_HEIGHT=640
WINDOW_WIDTH=1080

WINDOW_BUTTON_HEIGHT=40
WINDOW_BUTTON_WIDTH=80

CHESSMAN_SIZE=10
GRID_SIZE=30
PADDING_RATIO=1 #the ratio of padding between grid and board boundary
GRID_WIDTH=1 #the width of the grid lines
#colors
WINDOW_BG_COLOR=(127,127,127)
WINDOW_TEXT_COLOR=(0,0,0)

WINDOW_BUTTON_AVAILABLE_COLOR=(0,255,0)
WINDOW_BUTTON_UNAVAILABLE_COLOR=(255,0,0)
#the chessman button color
FILL_COLOR_ODD=(0,0,0)
FILL_COLOR_EVEN=(255,255,255)
FILL_COLOR_ODD_TO_SELECT=(0,0,0,50)
FILL_COLOR_EVEN_TO_SELECT=(255,255,255,50)

#colors in chessboard
GRID_COLOR=(0,0,0)
CHESSBOARD_BG_COLOR=(188,176,71)

#view control constants
BUTTON_STATE_DEFAULT=0
BUTTON_STATE_ON_TOUCH=1