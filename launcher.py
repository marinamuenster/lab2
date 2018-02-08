#!/usr/bin/python

import serial, pygame, math, sys, colors
from colors import *
from pygame.locals import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0

BASE_X = 0
BASE_Y = 380
LAUNCHER_WIDTH = 8

class Launcher:
  def __init__(self,x,y):
    # the launcher is located at 0,380
#    pygame.draw.line()
    self.x = x
    self.y = y
    self.mag = 20			# initial magnitude
    self.angle = 45
    self.width = 10
    self.color = BLACK

  def changeMagnitude(self,delta):		# adjust the magnitude within MIN/MAX bounds
    self.mag+=delta
    if(self.mag>=MAX_MAG):
      self.mag = MAX_MAG
    if(self.mag<=MIN_MAG):
      self.mag = MIN_MAG
  
  def changeAngle(self,delta):			# adjust the angle w/in MAX/MIN bounds
    self.angle+=delta
    if(self.angle<=MIN_ANGLE):
      self.angle = MIN_ANGLE
    if(self.angle>=MAX_ANGLE):
      self.angle = MAX_ANGLE

  def fire(self, rock):
    rock.v_x = self.mag*math.cos(self.angle*math.pi/180)
    rock.y_y = self.mag*math.sin(self.angle*math.pi/180)

  def draw(self, surf):		# draw launcher on the given surface from polar coordinates
    dx = self.mag*math.cos(self.angle*math.pi/180)
    dy = self.mag*math.sin(self.angle*math.pi/180)

    pygame.draw.line(surf, self.color, (self.x,self.y), (self.x+dx,self.y-dy), self.width)





