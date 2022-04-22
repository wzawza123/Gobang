# -*- encoding: utf-8 -*-
"""
@File    :   main_menu.py.py   
@Contact :   936956317@qq.com
  
@Modify Time      @Author      @Version   
------------      -------      --------    
2022/4/22 13:26   potatomine     1.0  
@Description : 
"""
from game.definitions import *
from view.view import *


def main_menu(screen):
    """
    the main menu
    Args:
        screen:

    Returns: the game mode "HUMAN VS HUMAN","HUMAN VS AI", "AI VS AI"

    """
    # init the view
    BACKGROUND_IMG_PATH = "./images/background.jpg"

    background = pygame.image.load(BACKGROUND_IMG_PATH).convert()
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # init the button
    button_view_list = [
        TextButton(WINDOW_TITLE_BUTTON_X, WINDOW_TITLE_BUTTON_Y, WINDOW_TITLE_TEXT_COLOR, "human vs human",
                   "HUMAN VS HUMAN", WINDOW_TITLE_FONT_SIZE),
        TextButton(WINDOW_TITLE_BUTTON_X, WINDOW_TITLE_BUTTON_Y + WINDOW_BUTTON_HEIGHT + WINDOW_TITLE_BUTTON_PADDING_Y,
                   WINDOW_TITLE_TEXT_COLOR, "human vs human", "HUMAN VS AI", WINDOW_TITLE_FONT_SIZE),
        TextButton(WINDOW_TITLE_BUTTON_X,
                   WINDOW_TITLE_BUTTON_Y + (WINDOW_BUTTON_HEIGHT + WINDOW_TITLE_BUTTON_PADDING_Y) * 2,
                   WINDOW_TITLE_TEXT_COLOR, "human vs human", "AI VS AI", WINDOW_TITLE_FONT_SIZE)]
    isRunning = True
    while isRunning:
        # get the event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button_view in button_view_list:
                    if button_view.is_in_button(mouse_pos[0], mouse_pos[1]):
                        isRunning = False
                        return button_view.get_text()
        # update the view
        screen.blit(background, (0, 0))
        for button_view in button_view_list:
            button_view.draw(screen)
        # update the screen
        pygame.display.flip()
    pygame.quit()
