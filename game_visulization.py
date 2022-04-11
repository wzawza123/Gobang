'''
Description: visualize the game process
Date: 2022-04-11 13:30:24
LastEditTime: 2022-04-11 19:03:34
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
    #init the button view
    button_view = SquareButton(WINDOW_WIDTH/2+100,WINDOW_HEIGHT/2+100,WINDOW_BUTTON_AVAILABLE_COLOR,0,WINDOW_BUTTON_HEIGHT,WINDOW_BUTTON_WIDTH,'button',20)
    chessman_list=[]
    chessman_list.append(Chessman(x=WINDOW_WIDTH/3,y=WINDOW_HEIGHT/3,color=(0,0,0),id=0,r=CHESSMAN_SIZE,fill=SPACE_NUMBER))
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
                #check if the button is clicked
                for button in chessman_list:
                    if button.is_in_button(mouse_pos[0],mouse_pos[1]):
                        button.update_state(BUTTON_STATE_ON_TOUCH)
                    else:
                        button.update_state(BUTTON_STATE_DEFAULT)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                #check if the button is clicked
                if button_view.is_in_button(mouse_pos[0],mouse_pos[1]):
                    #change the text
                    text_view.set_text('hello world')
                for button in chessman_list:
                    if button.is_in_button(mouse_pos[0],mouse_pos[1]):
                        button.set_fill(gameClass.get_cur_player_number())
                    else:
                        button.update_state(BUTTON_STATE_DEFAULT)
        #draw the background
        screen.blit(background,(0,0))
        #draw the text view
        text_view.draw(screen)
        #draw the button view
        button_view.draw(screen)
        #draw the chessman
        for button in chessman_list:
            button.draw(screen,gameClass.get_cur_player_type())
        #update the screen
        pygame.display.flip()
    #quit the game
    pygame.quit()

if __name__ == '__main__':
    visualization_main()