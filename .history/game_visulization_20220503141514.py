"""
Description: visualize the game process
Date: 2022-04-11 13:30:24
LastEditTime: 2022-04-13 20:56:06
"""
from random import randint

import pygame
from abc import ABCMeta, abstractmethod

import window
from game.definitions import *
from game.GobangGame import *
# import the view classes
from view.view import *
from window.ai_vs_ai_menu import ai_vs_ai_menu
from window.main_menu import main_menu
from window.human_vs_ai_menu import human_vs_ai_menu


def game_window(screen, game_mode):
    """
    visualize the game process
    Returns:None

    """
    # init game object
    gameClass = GobangGame()
    # check the branches depending on the game mode
    if game_mode == "HUMAN VS AI":
        first_player_type = human_vs_ai_menu(screen)
        gameClass.select_game_mode_pvai(first_player_type)
    elif game_mode == "AI VS AI":
        algorithm_id_odd, algorithm_id_even = ai_vs_ai_menu(screen)
        
    else:
        gameClass.select_game_mode_pvp()
    # init the chessboard view
    chessboard_view = Chessboard(
        x=WINDOW_CHESSBOARD_X, y=WINDOW_CHESSBOARD_Y, color=CHESSBOARD_BG_COLOR, id="chessboard", game_core=gameClass)
    print(chessboard_view.get_size())
    # init the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WINDOW_BG_COLOR)
    # init the text view
    status_board_view = TextView(0, WINDOW_STATUS_BOARD_Y, WINDOW_TEXT_COLOR, 0, 'hello', 40)
    status_board_view.set_pos_middle_x(WINDOW_LEFT_PADDING, WINDOW_LEFT_EDGE)
    # init the button view
    undo_button = SquareButton(x=750, y=500, color=WINDOW_BUTTON_AVAILABLE_COLOR, id="undo",
                               height=WINDOW_BUTTON_HEIGHT, width=WINDOW_BUTTON_WIDTH, text="undo",
                               text_size=WINDOW_BUTTON_TEXT_SIZE)
    restart_button=SquareButton(x=850, y=500, color=WINDOW_BUTTON_AVAILABLE_COLOR, id="restart",
                               height=WINDOW_BUTTON_HEIGHT, width=WINDOW_BUTTON_WIDTH, text="restart",
                               text_size=WINDOW_BUTTON_TEXT_SIZE)
    # init the plot view
    plot_view = PlotView(x=WINDOW_PLOT_VIEW_X, y=WINDOW_PLOT_VIEW_Y, color=WINDOW_PLOT_COLOR,
                         id="plot", font_size=20, width=WINDOW_PLOT_VIEW_WIDTH, height=WINDOW_PLOT_VIEW_HEIGHT)
    # init the switch view
    switch_view = Switch(x=WINDOW_SWITCH_VIEW_X, y=WINDOW_SWITCH_VIEW_Y, color=WINDOW_SWITCH_COLOR, id="switch",
                         width=WINDOW_SWITCH_VIEW_WIDTH, height=WINDOW_SWITCH_VIEW_HEIGHT, left_text="left",
                         right_text="right", font_size=WINDOW_SWITCH_VIEW_FONT_SIZE)
    # game running flags
    isRunning = True
    # fps controller
    clock = pygame.time.Clock()
    # game loop
    while isRunning:
        # fps controller
        clock.tick(FPS)
        # handle the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.MOUSEMOTION:
                # get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                # chessboard update the mouse position
                chessboard_view.process_mouse_move(mouse_pos[0], mouse_pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                # check if the button is clicked
                update_index = chessboard_view.process_click(mouse_pos[0], mouse_pos[1])
                if update_index[0] != -1 and update_index[1] != -1:
                    # a valid move has been made
                    plot_view.insert(randint(-100, 100))
                if undo_button.is_in_button(mouse_pos[0], mouse_pos[1]):
                    gameClass.undo_move()
                    plot_view.pop()
                if restart_button.is_in_button(mouse_pos[0], mouse_pos[1]):
                    gameClass.restart()
                    plot_view.clear()
        # update the view
        game_result = gameClass.end_check()
        if game_result == GAME_STILL_PLAYING:
            if gameClass.get_cur_player_type() == GAME_HUMAN_MOVE:
                status_board_view.set_text("human moving")
            else:
                status_board_view.set_text("AI moving")
        else:
            if game_result == GAME_END_ODD_WIN:
                status_board_view.set_text("black wins")
            elif game_result == GAME_END_EVEN_WIN:
                status_board_view.set_text("white wins")

        status_board_view.set_pos_middle_x(WINDOW_LEFT_PADDING, WINDOW_LEFT_EDGE)

        # draw the background
        screen.blit(background, (0, 0))
        # draw the text view
        status_board_view.draw(screen)
        # draw the chessboard
        chessboard_view.draw(screen)
        # draw the button
        undo_button.draw(screen)
        restart_button.draw(screen)
        # draw the plot
        plot_view.draw(screen)
        # draw the switch
        switch_view.set_state("right")
        switch_view.draw(screen)
        # update the screen
        pygame.display.flip()
        # update game result
        game_result = gameClass.end_check()
        if game_result != GAME_STILL_PLAYING:
            gameClass.stop_game_process()
            print("game end with result:", game_result)
    # quit the game
    pygame.quit()


def init_pygame_window():
    """
    init the pygame window
    Returns: the screen surface

    """
    pygame.init()
    init_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Gobang')
    return init_screen


if __name__ == '__main__':
    screen = init_pygame_window()
    while True:
        game_mode = main_menu(screen)
        print(game_mode)
        game_window(screen, game_mode)
