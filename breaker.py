import pygame 
import math
pygame.init()
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello")
width = 800
height = 800
run = True
#center_of_rotation_x = width/2 - 1
#center_of_rotation_y = height/2 - 1
#radius = 350
#angle = math.radians(90)
#vel = 0.1
#x = width/2 -20 + radius * math.cos(angle) + 2
#y = height/2 + radius * math.sin(angle) - 2
CENTER = (400,400)
RADIUS = 350
satelliteCenter = (CENTER[0]+RADIUS, CENTER[1])
lst = [(347, 744),(312, 737),(279, 727),(247, 713),(216, 696),(187, 677),
       (160, 654),(136, 629),(114, 601),(95, 572),(79, 541),(67, 508)
       ,(57, 474),(51, 440),(49, 405),(50, 370),(54, 335),(62, 301),(74, 268)
       ,(88, 236),(106, 206),(127, 178),(150, 152),(176, 128),(204, 107),(234, 89)
       ,(265, 74),(298, 62),(332, 54),(367, 49),(402, 48),(437, 50),(471, 55)
       ,(505, 64),(538, 76),(569, 92),(599, 110),(627, 132),(652, 156),(675, 182)
       ,(695, 211),(712, 242),(726, 274),(737, 307),(745, 341),(748, 376)
       ,(749, 411),(746, 446),(739, 480),(729, 514),(716, 546),(700, 577)
       ,(680, 606),(658, 633),(633, 658),(606, 680),(577, 699),(546, 716)
       ,(514, 729),(480, 738),(445, 745),(411, 748),(376, 747)]
i = 1
start = 0
end = 2
current = 100000000000000
best = (0,0)
while run: 
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.mouse.get_pos()
    vector = (keys[0]-CENTER[0], keys[1]-CENTER[1])
    distance = (vector[0]**2 + vector[1]**2)**0.5

    if distance > 0:
        scalar = RADIUS / distance
        satelliteCenter = (
      int(round( CENTER[0] + vector[0]*scalar )),
      int(round( CENTER[1] + vector[1]*scalar )) )
        
    if keys[pygame.K_LEFT]:
         i -= 1
         start -= 1
         end -= 1
         if i < 0:
             i = len(lst) -1
         if start < 0:
             start = len(lst) -1
         if end < 0 :
             
             end = len(lst) -1
    if keys[pygame.K_RIGHT]:
        i += 1
        start += 1
        end += 1
        if i > len(lst) -1:
            i = 0
        if start > len(lst) -1:
            start = 0
        if end > len(lst) -1:
            end = 0

    win.fill((0,0,0))
    pygame.draw.line(win, (255,255,255), lst[start], lst[end], 20)
    pygame.draw.circle(win, (255,255,255), satelliteCenter, 1, 1)
    pygame.draw.circle(win, (255,0,0),(400,400),350, 1)
    pygame.display.update()
    
pygame.quit()

