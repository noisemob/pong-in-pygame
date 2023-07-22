import pygame
p = pygame
p.init()

WIDTH, HEIGHT = 700, 500
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60
PWIDTH, PHEIGHT = 20, 140
WIN = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("pong game")


class paddle:
    COLOR = WHITE
    VEL = 5
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,win):
        p.draw.rect(win,self.COLOR,(self.x ,self.y ,self.width,self.height))

    def move(self,up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

def draw(win, paddles):
    win.fill(BLACK)
    for paddle in paddles:
        paddle.draw(win)
    p.display.update()

def movePaddles(key,lpaddle,rpaddle):
    if key[p.K_w] and lpaddle.y - lpaddle.VEL >= 0:
        lpaddle.move(up=True)
    if key[p.K_s] and lpaddle.y + lpaddle.VEL + lpaddle.height <= HEIGHT:
        lpaddle.move(up=False)

    if key[p.K_UP] and rpaddle.y - rpaddle.VEL >= 0:
        rpaddle.move(up=True)
    if key[p.K_DOWN]and rpaddle.y + rpaddle.VEL + rpaddle.height <= HEIGHT:
        rpaddle.move(up=False)
def main():
    run = True
    clock = p.time.Clock()

    lpaddle = paddle(10,(HEIGHT // 2) - (PHEIGHT / 2), PWIDTH,PHEIGHT)
    rpaddle = paddle(WIDTH - PWIDTH - 10,(HEIGHT // 2) - (PHEIGHT / 2), PWIDTH,PHEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN,[lpaddle,rpaddle])
        for e in p.event.get():
            
            if e.type == p.QUIT:
                run = False
                break
        key = p.key.get_pressed()
        movePaddles(key,lpaddle,rpaddle)

    p.quit()


if __name__ == '__main__':
    main()