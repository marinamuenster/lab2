import pygame
from colors import *

G = 12.0
INITIAL_VEL = 100.0

class Rock:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.r = (0,0,0,0)
    self.v_x = 0.0
    self.v_y = 0.0

  def move(self, time):
    self.x += self.v_x*time			# move in x
    if (self.v_y != 0):
      self.v_y += G*time			# move y velocity      
    self.y += self.v_y*time			# move in y
    if (self.y >= 390):
      self.v_x = 0
      self.v_y = 0

  def moveTo(self, x, y):
    self.x = x
    self.y = y
    self.v_x = 0
    self.v_y = 0    

  def getRect(self):
    return self.r

  def draw_rock(self, surf):
    self.r = pygame.Rect((0,0,10,10))
    self.r.center = (self.x, self.y)
    pygame.draw.rect(surf,ROCK,self.r)

  def isMoving(self):
    if (self.v_x == 0) and (self.v_y == 0):
      return False
    else: 
      return True


  
