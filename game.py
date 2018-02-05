#!/usr/bin/python

import serial, pygame, sys

from pygame.locals import *
from colors import *

pygame.display.init()

HEIGHT = 400
WIDTH = 500

#FPS = 30  						# frames per second setting
#fpsClock = pygame.time.Clock()				# clock object
#fpsClock.tick(FPS)
#s = serial.Serial("/dev/ttyACM0")

  # creates game box
SURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Launchr')			# window title


def draw_world(surf):  					# surf is a pygame surface
  # fills in sky and ground
  pygame.draw.rect(surf, SKY, (0,0,WIDTH,HEIGHT-20))
  pygame.draw.rect(surf, GROUND, (0,HEIGHT-20,WIDTH,20))

  # writes and places title
  fontObj = pygame.font.Font('freesansbold.ttf', 32)
  textSurfaceObj = fontObj.render('Launchr 1.8', True, BLACK, SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (WIDTH/2,40)


while True: 						# main game loop
  draw_world(SURF)
  SURF.blit(textSurfaceObj,textRectObj)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
  pygame.display.update()



