from __future__ import division 
from math import atan2, degrees, pi
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("globebreaker")
CENTER = (400, 400)
RADIUS = 350

satelliteCenter = (CENTER[0]+RADIUS, CENTER[1])
satelliteCenter2 = (CENTER[0]+RADIUS , CENTER[1] )
running = True

screen.fill((152,206,231))
pygame.draw.circle(screen, (71,153,192), CENTER, RADIUS)
pygame.display.update()

def drawCircleArc(screen,color,center,radius,startDeg,endDeg,thickness):
    (x,y) = center
    rect = (x-radius,y-radius,radius*2,radius*2)
    startRad = math.radians(startDeg)
    endRad = math.radians(endDeg)

    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)
    
    
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
        running = False

  mouse = pygame.mouse.get_pos()
  
  relx = mouse[0] - CENTER[0]
  rely = mouse[1] - CENTER[1]
  rad = atan2(-rely,relx)
  rad %= 2*pi
  degs = degrees(rad)
  
  mouse2 = (mouse[0] , mouse[1] )
  vector2 = (mouse2[0]-CENTER[0], mouse2[1]-CENTER[1])
  distance2 = (vector2[0]**2 + vector2[1]**2)**0.5
  
  vector = (mouse[0]-CENTER[0], mouse[1]-CENTER[1])
  distance = (vector[0]**2 + vector[1]**2)**0.5

  if distance > 0:
    scalar = RADIUS / distance
    satelliteCenter = (
      int(round( CENTER[0] + vector[0]*scalar )),
      int(round( CENTER[1] + vector[1]*scalar )) )
  if distance > 0:
      scalar = RADIUS / distance2
      satelliteCenter2 = (
              int(round( CENTER[0] + vector2[0]*scalar )),
              int(round( CENTER[1] + vector2[1]*scalar )) )

 # screen.fill((152,206,231))
  drawCircleArc(screen,(243,79,79),CENTER,RADIUS, degs + 90,degs + 100 ,10)
#  pygame.draw.rect(screen, (243,79,79), pygame.Rect((satelliteCenter[0] - 2, 
#                   satelliteCenter[1] + 1),(satelliteCenter[0] + 2,satelliteCenter[1] - 1)))
#  pygame.draw.circle(screen, (71,153,192), CENTER, RADIUS)
#  pygame.draw.circle(screen, (243,79,79), satelliteCenter, 16)
#  pygame.draw.circle(screen, (243,79,79), satelliteCenter2, 16)
#  pygame.draw.arc(screen, (243,79,79),(50,50,50,50), 90, 100)
#  pygame.display.update()
  pygame.display.flip()
  
pygame.quit()