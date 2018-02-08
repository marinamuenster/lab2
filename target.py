import pygame, colors
from colors import *

class Target:
  def __init__(self, X_POS, Y_POS, TARGET_WIDTH):
    self.x = X_POS
    self.y = Y_POS
    self.h = 10
    self.w = TARGET_WIDTH
    self.rect = pygame.Rect((0,0,self.w,self.h))

  def draw_target(self, surf):
    self.rect.center = (self.x, self.y)
    pygame.draw.rect(surf, TARGET_COLOR, self.rect)

  def hitBy(self, obj):
    return self.rect.colliderect(obj.getRect())
    

