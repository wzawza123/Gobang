"""
Description: define view object for visualization
Date: 2022-04-11 13:44:01
LastEditTime: 2022-04-13 21:31:22
"""
import pygame
from abc import ABCMeta, abstractmethod

from game.definitions import *
from game.GobangGame import *


# this is an abstract class for views object
class View:
    def __init__(self, x, y, color, id) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.id = id

    @abstractmethod
    def draw(self, screen):
        pass

    # getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

    def get_id(self):
        return self.id

    # setters
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_color(self, color):
        self.color = color


# this is the abstract button class
class Button(View):
    def __init__(self, x, y, color, id) -> None:
        super().__init__(x, y, color, id)
        self.state = BUTTON_STATE_DEFAULT

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def is_in_button(self, x, y):
        pass

    def update_state(self, state):
        self.state = state
        pass


# this is the class of the text view
class TextView(View):
    def __init__(self, x, y, color, id, text, text_size) -> None:
        super().__init__(x, y, color, id)
        self.text = text
        self.text_size = text_size
        self.font = pygame.font.SysFont('arial', self.text_size)
        self.text_rendered = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        self.text_rendered = self.font.render(self.text, True, self.color)
        screen.blit(self.text_rendered, (self.x, self.y))

    '''
    name: set_pos_middle_x
    description: set the textview to the middle left and right
    param {*} self
    param {*} left left bound
    param {*} right right bound
    '''

    def set_pos_middle_x(self, left, right):
        self.x = (left + right - self.text_rendered.get_width()) / 2

    def set_pos_middle_y(self, top, bottom):
        self.y = (top + bottom - self.text_rendered.get_height()) / 2

    def set_text(self, text):
        self.text = text
        self.font = pygame.font.SysFont('arial', self.text_size)
        self.text_rendered = self.font.render(self.text, True, self.color)

    def get_text(self):
        return self.text


# this is the class of square button with text
class SquareButton(Button):
    def __init__(self, x, y, color, id, height, width, text, text_size) -> None:
        super().__init__(x, y, color, id)
        self.height = height
        self.width = width
        self.text = TextView(x, y, WINDOW_TEXT_COLOR, id, text, text_size)
        self.update_text_pos()

    '''
    name: update text pos
    description: update the text position at the center of the button
    param {*} self
    return {*}
    '''

    def update_text_pos(self):
        self.text.set_pos_middle_x(self.x, self.x + self.width)
        self.text.set_pos_middle_y(self.y, self.y + self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.text.draw(screen)

    def set_text(self, text):
        self.text.set_text(text)
        self.update_text_pos()

    def get_text(self):
        return self.text.get_text()

    def is_in_button(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        else:
            return False


# this is the class of chessman
class Chessman(Button):
    def __init__(self, x, y, color, id, r=CHESSMAN_SIZE, fill=SPACE_NUMBER) -> None:
        super().__init__(x, y, color, id)
        self.r = r
        self.fill = fill

    '''
    name: draw
    description: draw the chessman 
    param {*} self
    param {*} screen
    param {*} cur_player a number, odd,even and 0 for unavailiable
    return {*}
    '''

    def draw(self, screen, cur_player: int):
        # draw the chessman
        if self.fill == SPACE_NUMBER:
            if cur_player != SPACE_NUMBER and self.state == BUTTON_STATE_ON_TOUCH:
                # when the button has not been determined and current button is available
                if cur_player % 2 == 0:
                    pygame.draw.circle(screen, FILL_COLOR_EVEN_TO_SELECT, (self.x, self.y), self.r)
                else:
                    pygame.draw.circle(screen, FILL_COLOR_ODD_TO_SELECT, (self.x, self.y), self.r)
        else:
            # the chessman position is determined
            if self.fill % 2 == 0:
                pygame.draw.circle(screen, FILL_COLOR_EVEN, (self.x, self.y), self.r)
            else:
                pygame.draw.circle(screen, FILL_COLOR_ODD, (self.x, self.y), self.r)

    def set_fill(self, fill):
        self.fill = fill

    def is_in_button(self, x, y):
        if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
            return True
        else:
            return False


# this is the class of chessboard
class Chessboard(View):
    def __init__(self, x, y, color, id, game_core: GobangGame, grid_size=GRID_SIZE, r=CHESSMAN_SIZE) -> None:
        super().__init__(x, y, color, id)
        self.grid_size = grid_size
        self.r = r
        self.chessman_list = []
        self.game_core = game_core
        self.col = BOARD_WIDTH
        self.row = BOARD_HEIGHT
        self.init_chessman_list()

    '''
    name: init chessman list
    description: initialize the chessman list with the position
    param {*} self
    return {*}
    '''

    def init_chessman_list(self):
        for i in range(self.row):
            chessman_in_row = []
            for j in range(self.col):
                chessman_in_row.append(Chessman(x=self.x + j * self.grid_size + PADDING_RATIO * self.grid_size,
                                                y=self.y + i * self.grid_size + PADDING_RATIO * self.grid_size,
                                                color=self.color, id=i * self.col + j, r=self.r))
            self.chessman_list.append(chessman_in_row)

    def draw(self, screen):
        player_type=self.game_core.get_cur_player_type()
        player_number=self.game_core.get_cur_player_number()
        # draw the chessboard
        # background
        pygame.draw.rect(screen, self.color, (self.x, self.y, (self.col + PADDING_RATIO * 2 - 1) * self.grid_size,
                                              (self.row + PADDING_RATIO * 2 - 1) * self.grid_size))
        # draw the grid
        for i in range(self.row):
            pygame.draw.line(screen, GRID_COLOR, (
                self.x + PADDING_RATIO * self.grid_size, self.y + i * self.grid_size + PADDING_RATIO * self.grid_size),
                             (
                                 self.x + self.col * self.grid_size,
                                 self.y + i * self.grid_size + PADDING_RATIO * self.grid_size))
        for j in range(self.col):
            pygame.draw.line(screen, GRID_COLOR, (
                self.x + j * self.grid_size + PADDING_RATIO * self.grid_size, self.y + PADDING_RATIO * self.grid_size),
                             (
                                 self.x + j * self.grid_size + PADDING_RATIO * self.grid_size,
                                 self.y + self.row * self.grid_size))
        # update chessman information
        for i in range(self.row):
            for j in range(self.col):
                self.chessman_list[i][j].fill = self.game_core.chessManual[i][j]
        # draw the chessman
        for i in range(self.row):
            for j in range(self.col):
                if player_type == GAME_HUMAN_MOVE:
                    self.chessman_list[i][j].draw(screen, player_number)
                elif player_type == GAME_AI_MOVE or player_type == GAME_NO_ONE_MOVE:
                    self.chessman_list[i][j].draw(screen, SPACE_NUMBER)  # disable the animation on touch

    '''
    name: get_nearest_chessman
    description: get the chessman object if the position is in the chessman
    param {*} self
    param {*} x
    param {*} y
    return {*} the index of the button, -1 if not in the button
    '''

    def get_nearest_chessman(self, x, y):
        # get the nearest chessman
        for i in range(self.row):
            for j in range(self.col):
                if self.chessman_list[i][j].is_in_button(x, y):
                    return i, j
        return -1, -1

    '''
    name: process_click
    description: process the click event
    param {*} self
    param {*} x
    param {*} y
    return {*} return the index of the chessman if the click is in the chessman, -1 if not
    '''

    def process_click(self, x, y):
        cur_player_type = self.game_core.get_cur_player_type()
        cur_player_number = self.game_core.get_cur_player_number()
        # process the click event
        if cur_player_type != GAME_HUMAN_MOVE:
            return -1, -1
        i, j = self.get_nearest_chessman(x, y)
        if i != -1 and j != -1:
            if self.chessman_list[i][j].fill == SPACE_NUMBER:
                self.chessman_list[i][j].set_fill(cur_player_number)
                self.game_core.update_human_move(i, j)
                return i, j
        return -1, -1

    '''
    name: process_mouse_move
    description: process the touch event
    param {*}
    return {*}
    '''

    def process_mouse_move(self, x, y):
        cur_player_type = self.game_core.get_cur_player_type()
        # process the click event
        if cur_player_type != GAME_HUMAN_MOVE:
            return
        for i in range(self.row):
            for j in range(self.col):
                if self.chessman_list[i][j].is_in_button(x, y):
                    self.chessman_list[i][j].update_state(BUTTON_STATE_ON_TOUCH)
                else:
                    self.chessman_list[i][j].update_state(BUTTON_STATE_DEFAULT)
