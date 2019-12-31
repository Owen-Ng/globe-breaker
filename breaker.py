import pygame 
import math
pygame.init()
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello")
width = 800
height = 800
run = True
center_of_rotation_x = width/2 - 1
center_of_rotation_y = height/2 - 1
radius = 350
angle = math.radians(90)
vel = 0.1
x = width/2 -20 + radius * math.cos(angle) + 2
y = height/2 + radius * math.sin(angle) - 2

while run: 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle = angle + vel
        x = x + radius * vel * math.cos(angle + math.pi/2) 
        y = y + radius * vel * math.sin(angle + math.pi / 2)
        print((int(x),int(y)))
        print(",")
    
    if keys[pygame.K_RIGHT]:
        angle = angle - vel
        x = x - radius * vel * math.cos(angle + math.pi/2) 
        y = y - radius * vel * math.sin(angle + math.pi / 2)
        
    pygame.draw.circle(win, (255,255,255), (int(x),int(y)), 1, 1)
    pygame.draw.circle(win, (255,0,0),(400,400),350, 1)
    pygame.display.update()
    
pygame.quit()

#def listcoor((x,y), radius):
#    lst = []
#    lst.append((x + radius * math.cos(angle), y + radius * math.sin(angle))
#    while 
    