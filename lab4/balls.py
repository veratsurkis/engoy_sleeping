import pygame
from pygame.draw import *
from random import randint
pygame.init()


FPS = 2
screen = pygame.display.set_mode((1200, 900))


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''This function draws a new ball.'''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    

def click():
    '''This function defines coordinates of circle's centre
         and it's radius.'''
    x_circle = x
    y_circle = y 
    r_circle = r

def click_mouse(event):
    x_mouse, y_mouse = event.pos


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0
x_mouse = 100000
y_mouse = 100000
x_circle = 0
y_circle = 0
r_circle = 0

while not finished:
    clock.tick(FPS)
    new_ball()
    click()
    pygame.display.update()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_mouse(event)
    if ((x_mouse - x_circle)^2 + (y_mouse - y_circle)^2 <= r_circle^2):
        score += 1
    new_ball()
    click()
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()
print(score)

