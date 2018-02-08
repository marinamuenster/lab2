#!/usr/bin/python

import serial, pygame, sys, colors, math		#sys is a lib full of comp level commands
import launcher
import rock

from pygame.locals import *
from colors import *

HEIGHT = 400
WIDTH = 500
FPS = 30  						# frames per second setting

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
  pygame.display.set_caption('Launchr')			# window title

  my_launcher = launcher.Launcher(0,(HEIGHT-20))
  #my_rock = rock.draw(0,0)

  while True: 						# main game loop


    for event in pygame.event.get(KEYUP):
      if event.key == pygame.K_UP:
	my_launcher.changeAngle(3)
      if event.key == pygame.K_DOWN:
	my_launcher.changeAngle(-3)
      if event.key == pygame.K_RIGHT:
	my_launcher.changeMagnitude(5)
      if event.key == pygame.K_LEFT:
        my_launcher.changeMagnitude(-5)
      if (event.key == pygame.K_SPACE) and (my_rock.isMoving()== False):
  	my_launcher.fire(my_rock)

      if event.type == QUIT:
        pygame.quit()
        sys.exit()
	 
    # game logic
    #my_rock.move(1.0/FPS)

    # Updates game screen  
    draw_world(SURF)
    my_launcher.draw(SURF)
    #my_rock.draw(SURF)
    pygame.display.update()
    fpsClock.tick(FPS)

main()
