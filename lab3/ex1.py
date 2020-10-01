import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))
 # face
circle(screen, (255, 255, 0), (250,250), 180)
 # eyes
circle(screen, (255, 0, 0), (180,200), 40)
circle(screen, (0, 0, 0), (180,200), 10)
circle(screen, (255, 0, 0), (330,200), 30)
circle(screen, (0, 0, 0), (330,200), 10)
 # mouth
rect(screen, (0,0,0), (180, 340, 150, 20))
 #eyebrows
polygon(screen, (0, 0, 0), [(130,130), (120,140), (200,180),(210,170)])
polygon(screen, (0, 0, 0), [(400,110), (390,100), (230,190), (240,200)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
