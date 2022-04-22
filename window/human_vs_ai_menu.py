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

    """
    # draw the background
    screen.fill(WINDOW_BG_COLOR)
    # init the textview
    text_view = TextView(0, 0, WINDOW_TEXT_COLOR, "choose who go first", "choose who go first", WINDOW_TITLE_FONT_SIZE)
    text_view.set_pos_middle_x(0, WINDOW_WIDTH)
    text_view.set_pos_middle_y(0, WINDOW_HEIGHT)
    # init the switch
    switch = Switch(0, 0, WINDOW_TEXT_COLOR, "human", "ai", WINDOW_TITLE_FONT_SIZE)
    switch.set_pos_middle_x(0, WINDOW_WIDTH)
    # init the button
    button = SquareButton(0, 0, WINDOW_TEXT_COLOR, "start", WINDOW_BUTTON_HEIGHT, WINDOW_BUTTON_WIDTH, "start",
                          WINDOW_BUTTON_TEXT_SIZE)
    isRunning = True
    while isRunning:
        # draw the background
        screen.fill(WINDOW_BG_COLOR)
        # draw the textview
        text_view.draw(screen)
        # draw the switch
        switch.draw(screen)
        # update the screen
        pygame.display.update()
        # get the event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if switch.is_in_button(event.pos[0], event.pos[1]):
                    switch.change_state()

        # draw the button
        button.draw(screen)
        # draw the switch
        switch.draw(screen)
        # draw the textview
        text_view.draw(screen)
        # update the screen
        pygame.display.update()
    pygame.quit()

    return switch.get_state()