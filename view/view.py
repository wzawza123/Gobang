'''
Description: define view object for visualization
Date: 2022-04-11 13:44:01
LastEditTime: 2022-04-11 19:07:13
'''
import pygame
from abc import ABCMeta, abstractmethod

from game.definitions import *
#this is an abstract class for views object
class View:
    def __init__(self,x,y,color,id) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.id=id
    @abstractmethod
    def draw(self,screen):
        pass
    #getters
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_color(self):
        return self.color
    def get_id(self):
        return self.id
    #setters
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_pos(self,x,y):
        self.x = x
        self.y = y
    def set_color(self,color):
        self.color = color

#this is the abstract button class
class Button(View):
    def __init__(self,x,y,color,id) -> None:
        super().__init__(x,y,color,id)
        self.state=BUTTON_STATE_DEFAULT
    @abstractmethod
    def draw(self,screen):
        pass
    @abstractmethod
    def is_in_button(self,x,y):
        pass
    def update_state(self,state):
        self.state=state
        pass
#this is the class of the text view
class TextView(View):
    def __init__(self,x,y,color,id,text,text_size) -> None:
        super().__init__(x,y,color,id)
        self.text = text
        self.text_size = text_size
        self.font = pygame.font.SysFont('arial',self.text_size)
        self.text_rendered = self.font.render(self.text,True,self.color)
    def draw(self,screen):
        self.text_rendered = self.font.render(self.text,True,self.color)
        screen.blit(self.text_rendered,(self.x,self.y))
    
    '''
    name: set_pos_middle_x
    description: set the textview to the middle left and right
    param {*} self
    param {*} left left bound
    param {*} right right bound
    '''
    def set_pos_middle_x(self,left,right):
        self.x = (left+right-self.text_rendered.get_width())/2
    def set_pos_middle_y(self,top,bottom):
        self.y = (top+bottom-self.text_rendered.get_height())/2

    def set_text(self,text):
        self.text = text
        self.font = pygame.font.SysFont('arial',self.text_size)
        self.text_rendered = self.font.render(self.text,True,self.color)
    def get_text(self):
        return self.text
        
#this is the class of square button with text
class SquareButton(Button):
    def __init__(self,x,y,color,id,height,width,text,text_size) -> None:
        super().__init__(x,y,color,id)
        self.height = height
        self.width = width
        self.text=TextView(x,y,WINDOW_TEXT_COLOR,id,text,text_size)
        self.update_text_pos()
    '''
    name: update text pos
    description: update the text position at the center of the button
    param {*} self
    return {*}
    '''    
    def update_text_pos(self):
        self.text.set_pos_middle_x(self.x,self.x+self.width)
        self.text.set_pos_middle_y(self.y,self.y+self.height)
    
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        self.text.draw(screen)
    
    def set_text(self,text):
        self.text.set_text(text)
        self.update_text_pos()
    
    def get_text(self):
        return self.text.get_text()

    def is_in_button(self,x,y):
        if x>=self.x and x<=self.x+self.width and y>=self.y and y<=self.y+self.height:
            return True
        else:
            return False

#this is the class of chessman
class Chessman(Button):
    def __init__(self,x,y,color,id,r=CHESSMAN_SIZE,fill=SPACE_NUMBER) -> None:
        super().__init__(x,y,color,id)
        self.r=r
        self.fill=fill
    '''
    name: draw
    description: draw the chessman 
    param {*} self
    param {*} screen
    param {*} cur_player a number, odd,even and 0 for unavailiable
    return {*}
    '''    
    def draw(self,screen,cur_player:int):
        #draw the chessman
        if self.fill==SPACE_NUMBER:
            if cur_player!=SPACE_NUMBER and self.state==BUTTON_STATE_ON_TOUCH:
                #when the button has not been determined and current button is available
                if cur_player%2==0:
                    pygame.draw.circle(screen,FILL_COLOR_EVEN_TO_SELECT,(self.x,self.y),self.r)
                else:
                    pygame.draw.circle(screen,FILL_COLOR_ODD_TO_SELECT,(self.x,self.y),self.r)
        else:
            #the chessman position is determined
            if self.fill%2==0:
                    pygame.draw.circle(screen,FILL_COLOR_EVEN,(self.x,self.y),self.r)
            else:
                pygame.draw.circle(screen,FILL_COLOR_ODD,(self.x,self.y),self.r)
    
    def set_fill(self,fill):
        self.fill=fill
    def is_in_button(self,x,y):
        if (x-self.x)**2+(y-self.y)**2<=self.r**2:
            return True
        else:
            return False