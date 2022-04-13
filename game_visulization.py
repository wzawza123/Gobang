'''
Description: visualize the game process
Date: 2022-04-11 13:30:24
LastEditTime: 2022-04-13 18:45:08
'''
from http.client import ImproperConnectionState
import pygame
from abc import ABCMeta, abstractmethod
#import definitions
from game.definitions import *
from game.GobangGame import *
#import the view classes
from view.view import *

#visualize the game process
def visualization_main():
    #init game object
    gameClass=GobangGame()
    gameClass.display_chessmanual()
    #init the chessboard view
    chessboard_view = Chessboard(x=50,y=50,color=CHESSBOARD_BG_COLOR,id="chessboard",game_core=gameClass)
    #init pygame window
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Gobang')
    #init the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WINDOW_BG_COLOR)
    #init the text view
    text_view = TextView(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,WINDOW_TEXT_COLOR,0,'hello',40)
    #game running flags
    isRunning=True
    #fps controller
    clock = pygame.time.Clock()
    #game loop
    while isRunning:
        #fps controller
        clock.tick(FPS)
        #handle the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.MOUSEMOTION:
                #get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                #chessboard update the mouse position
                chessboard_view.process_mouse_move(mouse_pos[0],mouse_pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                #check if the button is clicked
                chessboard_view.process_click(mouse_pos[0],mouse_pos[1])
        #draw the background
        screen.blit(background,(0,0))
        #draw the text view
        text_view.draw(screen)
        #draw the chessboard
        chessboard_view.draw(screen,gameClass.get_cur_player_type(),gameClass.get_cur_player_number())
        #draw the chessman
        # for button in chessman_list:
        #     button.draw(screen,gameClass.get_cur_player_type())
        #update the screen
        pygame.display.flip()
        #update the game
        game_result=gameClass.update_game_turn()
        if game_result!=GAME_STILL_PLAYING:
            gameClass.stop_game_process()
            print("game end with result:",game_result)
    #quit the game
    pygame.quit()

if __name__ == '__main__':
    visualization_main()