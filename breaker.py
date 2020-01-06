from __future__ import division 
import math
import pygame
background = pygame.image.load('pics/background.png')
balld = pygame.image.load('pics/ball.png')
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("globebreaker")

CENTER = (400, 400)
RADIUS = 350
clock = pygame.time.Clock()

class ball:
    def __init__(self, start_pos):
        self.position = start_pos
    def draw(self):
        screen.blit(balld, self.position)
        pygame.display.update()
        
        

def redrawscreen(angle):
      screen.blit(background, (0,0))
      pygame.draw.circle(screen, (0,0,0), CENTER, RADIUS - 5, 1)
      drawCircleArc(screen,(0,0,0),CENTER,RADIUS, angle -10,angle + 10 ,10)
      pygame.display.update()

def drawCircleArc(screen,color,center,radius,startDeg,endDeg,thickness):
    (x,y) = center
    rect = (x-radius,y-radius,radius*2,radius*2)
    startRad = math.radians(startDeg)
    endRad = math.radians(endDeg)

    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)
    
def game_loop(): 
    running = True
    angle = 45
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
      keys = pygame.key.get_pressed()

      
      if keys[pygame.K_LEFT]:
          angle += -2
                 
      if keys[pygame.K_RIGHT]:
          angle += 2
     
#      if distance > 0:
#          scalar = RADIUS / distance
#          satelliteCenter = (
#                  int(round( CENTER[0] + vector[0]*scalar )),
#                  int(round( CENTER[1] + vector[1]*scalar )) )
      

      satelliteCenter = (CENTER[0] + (RADIUS )*math.cos(-angle), CENTER[1] + (RADIUS )*math.sin(-angle))
      clock.tick(60)
    
      redrawscreen(angle)
      ball1 = ball(satelliteCenter)
      ball1.draw()
  
    pygame.quit()
    
game_loop()