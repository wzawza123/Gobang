'''
Description: 
Date: 2022-04-22 12:17:00
LastEditTime: 2022-05-03 15:09:50
'''
# -*- encoding: utf-8 -*-
"""
@File    :   human_vs_ai_menu.py   
@Contact :   936956317@qq.com
  
@Modify Time      @Author      @Version   
------------      -------      --------    
2022/4/22 12:17   potatomine     1.0  
@Description : 
"""
from game import definitions
import pygame

from game.definitions import *
from view.view import *


def human_vs_ai_menu(screen):
    """
    the human vs AI menu
    Args:
        screen:

    Returns: the first player type defined in definitions.py
             the algorithm: "faster" or "stronger"

    """
    # draw the background
    screen.fill(WINDOW_BG_COLOR)
    # init the textview
    text_view = TextView(0, 0, WINDOW_TEXT_COLOR, "choose who goes first", "choose who goes first and algorithm type", WINDOW_TITLE_FONT_SIZE)
    text_view.set_pos_middle_x(0, WINDOW_WIDTH)
    text_view.set_pos_middle_y(0, WINDOW_HEIGHT)
    # init the switch
    first_player_switch = Switch(0, 350, WINDOW_SWITCH_COLOR, "human", WINDOW_SWITCH_VIEW_WIDTH, WINDOW_SWITCH_VIEW_HEIGHT, "human",
                    "ai", WINDOW_SWITCH_VIEW_FONT_SIZE)
    algorithm_switch = Switch(0, 400, WINDOW_SWITCH_COLOR, "algorithm", WINDOW_SWITCH_VIEW_WIDTH, WINDOW_SWITCH_VIEW_HEIGHT, "faster","stronger",WINDOW_SWITCH_VIEW_FONT_SIZE)
    first_player_switch.set_pos_middle_x(0, WINDOW_WIDTH)
    algorithm_switch.set_pos_middle_x(0, WINDOW_WIDTH)
    # init the button
    button = SquareButton(0, 500, WINDOW_BUTTON_AVAILABLE_COLOR, "start", WINDOW_BUTTON_HEIGHT, WINDOW_BUTTON_WIDTH, "start",
                          WINDOW_BUTTON_TEXT_SIZE)
    button.set_pos_middle_x(0, WINDOW_WIDTH)
    isRunning = True
    while isRunning:
        # get the event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if first_player_switch.is_in_button(event.pos[0], event.pos[1]):
                    first_player_switch.change_state()
                if algorithm_switch.is_in_button(event.pos[0], event.pos[1]):
                    algorithm_switch.change_state()
                if button.is_in_button(event.pos[0], event.pos[1]):
                    first_player_selection=first_player_switch.get_state()
                    algorithm_selection=algorithm_switch.get_state()
                    if first_player_selection == "left":
                        first_player_result= GAME_HUMAN_MOVE
                    else:
                        first_player_result= GAME_AI_MOVE
                    if algorithm_selection == "left":
                        algorithm_result= "faster"
                    else:
                        algorithm_result= "stronger"
                    return first_player_result,algorithm_result
        # draw the background
        screen.fill(WINDOW_BG_COLOR)
        # draw the button
        button.draw(screen)
        # draw the switch
        first_player_switch.draw(screen)
        algorithm_switch.draw(screen)
        # draw the textview
        text_view.draw(screen)
        # update the screen
        pygame.display.update()
    pygame.quit()

    return first_player_switch.get_state()
