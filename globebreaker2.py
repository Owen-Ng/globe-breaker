from __future__ import division 
from math import atan2, degrees, pi
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("globebreaker")
CENTER = (400, 400)
RADIUS = 350
clock = pygame.time.Clock()
satelliteCenter = (CENTER[0]+RADIUS, CENTER[1])
satelliteCenter2 = (CENTER[0]+RADIUS , CENTER[1] )
running = True



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
  
  
  screen.fill((192,192,192))
  pygame.draw.circle(screen, (71,153,192), CENTER, RADIUS - 5, 1)
  drawCircleArc(screen,(128,128,128),CENTER,RADIUS, degs -10,degs + 10 ,10)
  
  clock.tick(30)

  pygame.display.update()
  
pygame.quit()