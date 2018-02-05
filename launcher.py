#!/usr/bin/python

import serial, pygame, math, sys
from pygame.locals import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0

BASE_X = 0
BASE_Y = 380
LAUNCHER_WIDTH = 8

def class Launcher:
  def __init__(self, x, y):
    # the launcher is located at 0,380
    pygame.draw.line()
    self.x = x
    self.y = y
    self.mag = 20			# initial magnitude
    self.ang = 45
    # with the initial state
    
    # magnitude = 20, angle = 45 deg or pi/4 rads


  def changeMagnitude(delta):
    # adjust the magnitude within MIN/MAX bounds

  
  def changeAngle(delta):
    # adjust the angle w/in MAX/MIN bounds


  def draw(surf):
    # draw launcher on the given surface
