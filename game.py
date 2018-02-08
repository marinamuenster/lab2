#!/usr/bin/python

import serial, pygame, sys, colors, math, time		#sys is a lib full of comp level commands
import launcher
import rock
import random
import target

from pygame.locals import *
from colors import *

HEIGHT = 400
WIDTH = 500
TARGET_WIDTH = 40
FPS = 30 						# frames per second setting
G = 10

#s = serial.Serial("/dev/ttyACM0")

def draw_world(surf):  					# surf is a pygame surface
  # fills in sky and ground
  pygame.draw.rect(surf, SKY, (0,0,WIDTH,HEIGHT-20))
  pygame.draw.rect(surf, GROUND, (0,HEIGHT-20,WIDTH,20))

  # writes and places title
  fontObj = pygame.font.Font('freesansbold.ttf', 32)
  textSurfaceObj = fontObj.render('Launchr 1.8', True, BLACK, SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = ((WIDTH/2),40)

  surf.blit(textSurfaceObj,textRectObj)

def main():
  pygame.init()
  pygame.display.init()
  fpsClock = pygame.time.Clock()				# clock object

  SURF = pygame.display.set_mode((WIDTH, HEIGHT))		# creates game box
  pygame.display.set_caption('Launchr')				# window title

  my_launcher = launcher.Launcher(0,(HEIGHT-20))
  my_rock = rock.Rock(0,(HEIGHT-20))
  my_target = target.Target(100+(random.random()*WIDTH-100),HEIGHT-20, TARGET_WIDTH)

  while True: 							# main game loop
    for event in pygame.event.get(KEYUP):
      if event.key == pygame.K_UP:
	my_launcher.changeAngle(3)
      if event.key == pygame.K_DOWN:
	my_launcher.changeAngle(-3)
      if event.key == pygame.K_RIGHT:
	my_launcher.changeMagnitude(5)
      if event.key == pygame.K_LEFT:
        my_launcher.changeMagnitude(-5)
      if (event.key == pygame.K_SPACE) and (my_rock.isMoving() == False):
  	my_launcher.fire(my_rock)

      if event.type == QUIT:
        pygame.quit()
        sys.exit()
	 
    # game logic
    my_rock.move(1.0/FPS)
    if (my_rock.y>HEIGHT-19):
      my_rock.moveTo(0, HEIGHT-20)
      displayText("You missed!", SURF)
    if my_target.hitBy(my_rock):
      my_rock.moveTo(0, HEIGHT-20)
      displayText("Got eeeem", SURF)

    # Updates game screen  
    draw_world(SURF)
    my_launcher.draw_launcher(SURF)
    my_target.draw_target(SURF)
    my_rock.draw_rock(SURF)
    pygame.display.update()
    fpsClock.tick(FPS)

def displayText(str, surf):
  fontObj = pygame.font.Font('freesansbold.ttf', 32)
  textSurfaceObj = fontObj.render(str, True, MSG_COLOR, MSG_BKGRND)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = ((WIDTH/2),200)

  surf.blit(textSurfaceObj,textRectObj)
  pygame.display.update()
  time.sleep(1)  
  
main()
