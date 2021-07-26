import pygame,time
from pygame.locals import *
black = 0,0,0
pygame.display.init()
pygame.init()
screen = pygame.display.set_mode((1280,720),0,32)

class NewSprite(pygame.sprite.Sprite):
    def __init__(self,filename):
        pygame.sprite.Sprite.__init__(self)
        self.picture = pygame.image.load(filename)#.convert_alpha
        self.frame_w = 32
        self.frame_h = 32
        self.rect = Rect(0,0,32,32)
        #self.rect = self.picture.get_rect()
        self.image = self.picture.subsurface(self.rect)
        self.frame = 0
        self.fps = 30

    def next(self):
        self.frame += 1

    def update(self):
        self.rect.y += 100
        self.image = self.picture.subsurface(self.rect)

people = NewSprite(".\p1.jpg")
peoples = pygame.sprite.Group()
peoples.add(people)
while 1:
    #peoples.update()
    peoples.draw(screen)
    pygame.display.update()
    time.sleep(1)

