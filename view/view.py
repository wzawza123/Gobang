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

    def set_pos_right_x(self, right_bound):
        """
        set the position of current view at the right of given boundary of x
        Args:
            right_bound: the right boundary of x

        Returns:

        """
        self.x = right_bound - self.text_rendered.get_width()

    def set_pos_middle_x(self, left, right):
        """
        set the position of current view at the middle of given boundary of x
        Args:
            left: the left boundary of x
            right: the right boundary of x

        Returns:

        """
        self.x = (left + right - self.text_rendered.get_width()) / 2

    def set_pos_middle_y(self, top, bottom):
        self.y = (top + bottom - self.text_rendered.get_height()) / 2

    def set_text(self, text):
        self.text = text
        self.font = pygame.font.SysFont('arial', self.text_size)
        self.text_rendered = self.font.render(self.text, True, self.color)

    def get_text(self):
        return self.text

    def get_width(self):
        return self.text_rendered.get_width()

    def get_height(self):
        return self.text_rendered.get_height()


# this is the class of square button with text
class SquareButton(Button):
    def __init__(self, x, y, color, id, height, width, text, text_size) -> None:
        super().__init__(x, y, color, id)
        self.height = height
        self.width = width
        self.text = TextView(x, y, WINDOW_TEXT_COLOR, id, text, text_size)
        self.update_text_pos()

    def update_text_pos(self):
        """
        reset the textview position
        Returns:

        """
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

    def draw(self, screen, cur_player: int):
        """
        draw the chessman
        Args:
            screen: the screen surface
            cur_player: the current player

        Returns:

        """
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

    def init_chessman_list(self):
        """
        initialize the chessman list
        Returns:

        """
        for i in range(self.row):
            chessman_in_row = []
            for j in range(self.col):
                chessman_in_row.append(Chessman(x=self.x + j * self.grid_size + PADDING_RATIO * self.grid_size,
                                                y=self.y + i * self.grid_size + PADDING_RATIO * self.grid_size,
                                                color=self.color, id=i * self.col + j, r=self.r))
            self.chessman_list.append(chessman_in_row)

    def draw(self, screen):
        player_type = self.game_core.get_cur_player_type()
        player_number = self.game_core.get_cur_player_number()
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

    def get_size(self):
        return self.grid_size * (self.col - 1) + PADDING_RATIO * 2 * self.grid_size, self.grid_size * (
                self.row - 1) + PADDING_RATIO * 2 * self.grid_size

    def get_nearest_chessman(self, row, col):
        """
        get the nearest chessman by the mouse position
        Args:
            row: row position of the mouse
            col: col position of the mouse

        Returns: the index of the nearest chessman

        """
        # get the nearest chessman
        for i in range(self.row):
            for j in range(self.col):
                if self.chessman_list[i][j].is_in_button(row, col):
                    return i, j
        return -1, -1

    def process_click(self, x, y):
        """
        process the click event
        Args:
            x: x position of the mouse
            y: y position of the mouse

        Returns: whether the click has make a valid move, return the move position

        """
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

    def process_mouse_move(self, x, y):
        """
        process the mouse move event
        Args:
            x: the x position of the mouse
            y: the y position of the mouse

        Returns:

        """
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


# the plot view of the game
class PlotView(View):
    def __init__(self, x, y, color, id, width, height, font_size, cnt_in_screen=-1) -> None:
        super().__init__(x, y, color, id)
        self.val = []
        self.cnt = 0
        self.max_val = 0
        self.min_val = 0
        self.width = width
        self.height = height
        self.font_size = font_size
        self.left_boundary = 0
        self.down_boundary = 0
        self.right_boundary = 0
        self.up_boundary = 0
        if min(self.width, self.height) < PLOT_VIEW_PADDING * 2:
            self.padding = 0
        else:
            self.padding = PLOT_VIEW_PADDING
        self.up_text = TextView(self.x + self.padding, self.y + self.padding, WINDOW_TEXT_COLOR, "up",
                                str(self.max_val), self.font_size)
        self.down_text = TextView(self.x + self.padding, self.y + self.padding, WINDOW_TEXT_COLOR, "down",
                                  str(self.min_val), self.font_size)
        self.left_text = TextView(self.x + self.padding, self.y + self.padding, WINDOW_TEXT_COLOR, "left", str(0),
                                  self.font_size)
        self.right_text = TextView(self.x + self.padding, self.y + self.padding, WINDOW_TEXT_COLOR, "right",
                                   str(len(self.val)), self.font_size)
        self.update_text_view()

    def insert(self, val):
        """
        insert element into the plot
        Args:
            val: the value of the new point

        Returns:

        """
        self.val.append(val)
        # update the max and min value
        self.max_val = max(self.val)
        self.min_val = min(self.val)
        self.cnt += 1
        self.update_text_view()

    def pop(self):
        """
        pop a value from the val list
        Args:

        Returns:

        """
        if self.cnt < 1:
            return
        self.val.pop()
        self.cnt -= 1
        if self.cnt < 1:
            self.max_val = 0
            self.min_val = 0
        else:
            self.max_val = max(self.val)
            self.min_val = min(self.val)
        self.update_text_view()

    def update_boundary(self):
        """
        update the boundary of the display area
        Returns:

        """
        self.left_boundary = max(self.up_text.get_width(),
                                 self.down_text.get_width()) + self.x + self.padding + self.padding // 2
        self.down_boundary = self.y + self.height - self.padding - self.left_text.get_height() - self.padding // 2
        self.right_boundary = self.x + self.width - self.padding
        self.up_boundary = self.y + self.padding

    def update_text_view(self):
        """
        update the text view text and position, and update the boundary
        Returns:

        """
        self.up_text.set_text(str(self.max_val))
        self.up_text.set_pos(self.x + self.padding, self.y + self.padding)
        self.down_text.set_text(str(self.min_val))
        self.down_text.set_pos(self.x + self.padding,
                               self.y + self.height - self.padding - self.down_text.get_height() * 2)
        self.left_text.set_text(str(0))
        self.left_text.set_pos(self.x + self.padding + self.up_text.get_width(),
                               self.y + self.height - self.padding - self.left_text.get_height())
        self.right_text.set_text(str(self.cnt))
        self.right_text.set_pos(self.x + self.width - self.padding - self.right_text.get_width(),
                                self.y + self.height - self.padding - self.right_text.get_height())
        self.update_boundary()

    def transform_pos(self, x, y) -> Tuple[int, int]:
        """
        transform the actual value into the position on screen
        Args:
            x: the x coordinate
            y: the value

        Returns: the position on screen

        """
        if self.cnt == 1:
            ans_x = (self.left_boundary + self.right_boundary) // 2
            ans_y = (self.up_boundary + self.down_boundary) // 2
        else:
            ans_x = self.left_boundary + x / (self.cnt - 1) * (self.right_boundary - self.left_boundary)
            ans_y = self.up_boundary + ((self.max_val - y) / (self.max_val - self.min_val)) * (
                    self.down_boundary - self.up_boundary)
        return ans_x, ans_y

    def draw(self, screen):
        """
        draw the plot out on the screen
        Args:
            screen: the pygame surface

        Returns:

        """
        # draw the background square
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        # draw the text views
        self.draw_text_view(screen)
        # draw the boundary
        self.draw_boundaries(screen)
        # draw the plot
        last_pos = (0, 0)
        for i in range(self.cnt):
            actual_pos = self.transform_pos(i, self.val[i])
            # pygame.draw.circle(screen, (255, 0, 0), actual_pos, 3)
            if i >= 1:
                pygame.draw.line(screen, (0, 0, 255), last_pos, actual_pos)
            last_pos = self.transform_pos(i, self.val[i])

    def draw_text_view(self, screen):
        """
        draw the text view
        Args:
            screen:

        Returns:

        """
        self.up_text.draw(screen)
        self.down_text.draw(screen)
        self.left_text.draw(screen)
        self.right_text.draw(screen)

    def draw_boundaries(self, screen):
        """
        draw the boundaries
        Returns:

        """
        pygame.draw.line(screen, (255, 0, 255), (self.left_boundary, self.up_boundary),
                         (self.left_boundary, self.down_boundary))
        pygame.draw.line(screen, (255, 0, 255), (self.right_boundary, self.up_boundary),
                         (self.right_boundary, self.down_boundary))
        pygame.draw.line(screen, (255, 0, 255), (self.left_boundary, self.up_boundary),
                         (self.right_boundary, self.up_boundary))
        pygame.draw.line(screen, (255, 0, 255), (self.left_boundary, self.down_boundary),
                         (self.right_boundary, self.down_boundary))


# the text button
class TextButton(Button):
    def __init__(self, x, y, color, id, text, font_size=20):
        super().__init__(x, y, color, id)
        self.text = text
        self.font_size = font_size
        self.text_view=TextView(x,y,color,"text view for text button",text,font_size)
        self.height=self.text_view.get_height()
        self.width=self.text_view.get_width()

    def draw(self, screen):
        # draw the textview
        self.text_view.draw(screen)

    def is_in_button(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def get_text(self):
        return self.text_view.get_text()

# the switch object
class Switch(Button):
    def __init__(self, x, y, color, id, width, height, left_text, right_text, font_size) -> None:
        super().__init__(x, y, color, id)
        self.width = width
        self.height = height
        # init the textview
        self.left_text_view = TextView(x, y, WINDOW_TEXT_COLOR, "left_text", left_text, font_size)
        self.left_text_view.set_pos_right_x(self.x)
        self.right_text_view = TextView(x, y, WINDOW_TEXT_COLOR, "right_text", right_text, font_size)
        self.right_text_view.set_x(self.x + self.width)
        self.current_state = "left"

    def draw(self, screen):
        self.left_text_view.draw(screen)
        self.right_text_view.draw(screen)
        if self.current_state == "left":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width / 3, self.height))
            pygame.draw.rect(screen, WINDOW_BUTTON_AVAILABLE_COLOR,
                             (self.x + self.width / 3, self.y, self.width / 3 * 2, self.height))
        else:
            pygame.draw.rect(screen, self.color,
                             (self.x + self.width - self.width / 3, self.y, self.width / 3, self.height))
            pygame.draw.rect(screen, WINDOW_BUTTON_AVAILABLE_COLOR, (self.x, self.y, self.width / 3 * 2, self.height))

    def is_in_button(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def set_state(self, state: str = "left"):
        """
        set the state of the switch
        Args:
            state: "left" or "right"

        Returns:

        """
        self.current_state = state

    def get_state(self) -> str:
        return self.current_state

    def set_pos_middle_x(self, left, right):
        self.x = (left + right) / 2 - self.width / 2

    def change_state(self):
        if self.current_state == "left":
            self.current_state = "right"
        else:
            self.current_state = "left"
