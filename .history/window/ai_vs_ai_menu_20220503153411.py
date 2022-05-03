'''
Description: 
Date: 2022-04-22 12:17:00
LastEditTime: 2022-05-03 15:25:36
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


def ai_vs_ai_menu(screen):
    """
    the ai vs AI menu
    Args:
        screen:

    Returns: the first player algorithm: "faster" or "stronger"

    """
    # draw the background
    screen.fill(WINDOW_BG_COLOR)
    # init the textview
    text_view = TextView(0, 0, WINDOW_TEXT_COLOR, "choose who goes first", "choose algorithm type of black", WINDOW_TITLE_FONT_SIZE)
    text_view.set_pos_middle_x(0, WINDOW_WIDTH)
    text_view.set_pos_middle_y(0, WINDOW_HEIGHT)
    # init the switch
    algorithm_switch = Switch(0, 400, WINDOW_SWITCH_COLOR, "algorithm", WINDOW_SWITCH_VIEW_WIDTH, WINDOW_SWITCH_VIEW_HEIGHT, "faster","stronger",WINDOW_SWITCH_VIEW_FONT_SIZE)
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
                if algorithm_switch.is_in_button(event.pos[0], event.pos[1]):
                    algorithm_switch.change_state()
                if button.is_in_button(event.pos[0], event.pos[1]):
                    algorithm_selection=algorithm_switch.get_state()
                    if algorithm_selection == "left":
                        algorithm_result= "faster"
                    else:
                        algorithm_result= "stronger"
                    return algorithm_result
        # draw the background
        screen.fill(WINDOW_BG_COLOR)
        # draw the button
        button.draw(screen)
        # draw the switch
        algorithm_switch.draw(screen)
        # draw the textview
        text_view.draw(screen)
        # update the screen
        pygame.display.update()
    pygame.quit()

    return algorithm_switch.get_state()
