import pygame
p = pygame
p.init()

WIDTH, HEIGHT = 1100, 600
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60
PWIDTH, PHEIGHT = 20, 200
BSIZE = 10
SFONT = p.font.SysFont("systembold",32)
WIN = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("pong game")

class Ball:
    COLOR = WHITE
    MAX_VEL = 10
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.xvel = self.MAX_VEL
        self.yvel = 0
    def draw(self,win):
        p.draw.circle(win,self.COLOR,(self.x,self.y),self.size)
    def move(self):
        self.x += self.xvel
        self.y += self.yvel


class paddle:
    COLOR = WHITE
    VEL = 8
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,win):
        p.draw.rect(win,self.COLOR,(self.x ,self.y ,self.width,self.height),border_radius=self.width//2)

    def move(self,up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


def draw(win, paddles, ball,lscore,rscore):
    win.fill(BLACK)
    
    ltext = SFONT.render(f"{lscore}",1,WHITE)
    rtext = SFONT.render(f"{rscore}",1,WHITE)
   
    win.blit(rtext,((WIDTH - WIDTH //4) - rtext.get_width() //2,15))
    win.blit(ltext,(WIDTH//4 - ltext.get_width()//2,15))
    for paddle in paddles:
        paddle.draw(win)
   
    ball.draw(win)
    for i in range(HEIGHT):
        if i%2 == 1:
            p.draw.rect(win,WHITE,(WIDTH/2, i *25,5,25))
    p.display.update()


def collisions(ball,lpaddle,rpaddle):
    
    if ball.y <= 0 + ball.size:
        ball.yvel *= -1
    if ball.y >= HEIGHT + ball.size:
        ball.yvel *= -1
    if ball.xvel < 0:
        if ball.y >= lpaddle.y and ball.y <= lpaddle.y + lpaddle.height:
            if ball.x - ball.size <= lpaddle.x + lpaddle.width:
                ball.xvel *= -1

                middley = lpaddle.y + lpaddle.height // 2
                ydis = middley -ball.y
                rfac = (lpaddle.height /2 )/ ball.MAX_VEL
                yvel = ydis / rfac
                ball.yvel = -1 * yvel
                
   
        
    else:
        if ball.y >= rpaddle.y and ball.y <= rpaddle.y + rpaddle.height:
            if ball.x + ball.size >= rpaddle.x:
                ball.xvel *= -1

                middley = rpaddle.y + rpaddle.height // 2
                ydis = middley -ball.y
                rfac = (rpaddle.height /2 )/ ball.MAX_VEL
                yvel = ydis / rfac
                ball.yvel = -1 *yvel
   
    

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
    ball = Ball(WIDTH // 2,HEIGHT // 2,BSIZE)
    lscore = 0
    rscore = 0

    while run:
        clock.tick(FPS)
        
        
        draw(WIN,[lpaddle,rpaddle],ball,lscore,rscore)
        for e in p.event.get():
            
            if e.type == p.QUIT:
                run = False
                break
        key = p.key.get_pressed()
        movePaddles(key,lpaddle,rpaddle)
        
        ball.move()
        collisions(ball,lpaddle,rpaddle)
        if ball.x >= WIDTH:
            lscore += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball.yvel = 0
            ball.xvel = ball.MAX_VEL * -1
            lpaddle.y = HEIGHT // 2 - lpaddle.height // 2
            rpaddle.y = HEIGHT // 2 - lpaddle.height // 2
           
           
        if ball.x <= 0:
            rscore += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball.yvel = 0
            ball.xvel = ball.MAX_VEL
            lpaddle.y = HEIGHT // 2 - lpaddle.height // 2
            rpaddle.y = HEIGHT // 2 - lpaddle.height // 2
           
            
           

        
    p.quit()


if __name__ == '__main__':
    main()