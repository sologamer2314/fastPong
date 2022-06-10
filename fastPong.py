import pygame as pg
from math import *

pg.init()
sc = pg.display.set_mode((700,500))
clock = pg.time.Clock()

class Sprite:
    def __init__(self,image,w=None,h=None):
        self.image = pg.image.load(image)
        if w != None or h != None:
            self.image = pg.transform.scale(self.image,(w,h))
    def show(self,pos=None):
        if pos != None:
            self.x = pos[0]
            self.y = pos[1]
        sc.blit(self.image,(self.x,self.y))

class Player(Sprite):
    def __init__(self,x,y,w,h,pl):
        self.playerNum = pl
        self.rect = pg.Rect(x,y,w,h)
        self.speed = 6
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def show(self):
        pg.draw.rect(sc,(0,0,0),(self.rect[0],self.rect[1],self.rect[2],self.rect[3]))
    def control(self):
        keys = pg.key.get_pressed()
        if self.playerNum == 1:
            if keys[pg.K_w]:
                self.rect[1] -= self.speed
            if keys[pg.K_s]:
                self.rect[1] += self.speed
        else:
            if keys[pg.K_UP]:
                self.rect[1] -= self.speed
            if keys[pg.K_DOWN]:
                self.rect[1] += self.speed
        if self.rect[1] < 0:
            self.rect[1] = 0
        elif self.rect[1] > 400:
            self.rect[1] = 400

class Ball(Sprite):
    def __init__(self):
        self.x = 350
        self.y = 250
        self.rect = pg.Rect(self.x,self.y,15,15)
        self.vectorX = 2
        self.vectorY = 2
    def show(self):
        pg.draw.circle(sc,(0,0,0),(self.x+7.5,self.y+7.5),7.5)
    def update(self):
        self.x += self.vectorX
        self.y += self.vectorY
        if self.y + 15 > 500:
            if self.vectorY > 0:
                self.vectorY += 0.1
                self.vectorY = self.vectorY * -1
                if self.vectorX > 0:
                    self.vectorX += 0.1
                else:
                    self.vectorX -= 0.1
        if self.y < 0:
            if self.vectorY < 0:
                self.vectorY -= 0.1
                self.vectorY *= -1
                if self.vectorX > 0:
                    self.vectorX += 0.1
                else:
                    self.vectorX -= 0.1
        self.rect = pg.Rect(self.x,self.y,15,15)
        if self.rect.colliderect(player1.rect):
            if self.vectorX < 0:
                self.vectorX *= -1
        if self.rect.colliderect(player2.rect):
            if self.vectorX > 0:
                self.vectorX *= -1
        if self.x > 700:
            finish(1)
        elif self.x < -15:
            finish(2)
def finish(player):
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        
        pg.font.init()

        if player == 1:
            sc.fill((0,255,0))
            font = pg.font.SysFont("Calibri",30)
            text = font.render("1st player wins!",True,(255,0,0),(128,128,128))
            sc.blit(text,(350,250))
            pg.display.update()
            clock.tick(60)
        else:
            sc.fill((0,255,0))
            font = pg.font.SysFont("Calibri",30)
            text = font.render("2nd player wins!",True,(255,0,0),(128,128,128))
            sc.blit(text,(350,250))
            pg.display.update()
            clock.tick(60)

global player1
player1 = Player(0,300,15,100,1)
global player2
player2 = Player(685,300,15,100,2)

ball = Ball()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    sc.fill((128,128,128))
    player1.show()
    player1.control()
    player2.show()
    player2.control()

    ball.update()
    ball.show()

    pg.display.update()
    clock.tick(60)