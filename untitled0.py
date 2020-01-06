# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:22:21 2020

@author: snige
"""

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
  
  
  screen.fill((152,206,231))
  pygame.draw.circle(screen, (71,153,192), CENTER, RADIUS)
  drawCircleArc(screen,(243,79,79),CENTER,RADIUS, angle -10,angle + 10 ,10)
  
  clock.tick(60)

  pygame.display.update()
  
pygame.quit()