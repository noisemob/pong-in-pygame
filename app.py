import pygame
pygame.init()
#set dimentions
WIDTH,HEIGHT = 600,400
#initialise game loop
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#variables
run = True
MIDDLEX = WIDTH / 2
MIDDLEY = HEIGHT / 2
lx = 10
ly = MIDDLEY
lwidth = 20
lheight = 120

def draw():
    WIN.fill((0,0,0))
    pygame.draw.rect(WIN,(255,255,255),(lx,ly,lwidth,lheight))
    pygame.display.update()          

def update():
   draw()
while run:
    update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    


pygame.quit()
