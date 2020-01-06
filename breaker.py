from __future__ import division 
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("globebreaker")
CENTER = (400, 400)
RADIUS = 350
clock = pygame.time.Clock()
running = True
angle = 45


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

  keys = pygame.key.get_pressed()
    
  if keys[pygame.K_LEFT]:
      angle += -2
             
  if keys[pygame.K_RIGHT]:
      angle += 2
  
  
  screen.fill((192,192,192))
  pygame.draw.circle(screen, (71,153,192), CENTER, RADIUS - 5, 1)
  drawCircleArc(screen,(128,128,128),CENTER,RADIUS, angle -10,angle + 10 ,10)
  
  clock.tick(60)

  pygame.display.update()
  
pygame.quit()