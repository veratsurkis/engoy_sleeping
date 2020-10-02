import pygame
from pygame.draw import *
import numpy as np
pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 500))

 # background
screen.fill((0, 190, 255))
rect(screen, (0, 0, 255), (0, 200, 700, 120))
rect(screen, (255, 255, 20), (0, 320, 700, 180))
x_wave = 25
y_wave = 320
r_wave = 25
for i in range(7):
    circle(screen, (255, 255, 20), (x_wave, y_wave), r_wave)
    circle(screen, (0, 0, 255), (x_wave+2*r_wave, y_wave), r_wave)
    x_wave += 4*r_wave

 # sun
r_sun=40
x_sun_center = 600
y_sun_center = 60
circle(screen, (255, 255, 0), (x_sun_center, y_sun_center), r_sun)

 # cloud
def cloud(x_cl, y_cl, r_cl):
    delta_x=int(x_cl/10)
    delta_y=int(y_cl/10)
    for i in range(7):
        circle(screen, (255, 255, 255), (x_cl, y_cl), r_cl)
        circle(screen, (220, 220, 220), (x_cl, y_cl), r_cl, 1)
        x_cl += delta_x
        y_cl -= delta_y*(-1)**i

 # umbrella
def umbrella(x_um, y_um, width_rect_um, heigth_rect_um, width_polygon_um, heigth_polygon_um):
    rect(screen, (200, 100, 0), (x_um, y_um,width_rect_um, heigth_rect_um))
    polygon(screen, (255, 100, 180), [(x_um, y_um), (x_um - width_polygon_um, y_um + heigth_polygon_um), (x_um + width_polygon_um + width_rect_um, y_um + heigth_polygon_um), (x_um + width_rect_um, y_um)])
    for i in range(5):
        line(screen, (100, 50, 50), (x_um, y_um), (x_um - width_polygon_um + width_polygon_um*(i+1)/5, y_um + heigth_polygon_um))
        line(screen, (100, 50, 50), (x_um + width_rect_um, y_um), (x_um + width_rect_um + width_polygon_um - width_polygon_um*(i+1)/5, y_um + heigth_polygon_um))

 # ship
def ship(x_sh, y_sh, width_sh, height_sh, width_mast, heigth_mast, width_sail):
    rect(screen, (120, 50, 50), (x_sh, y_sh, width_sh, height_sh))
    circle(screen, (120, 50, 50), (x_sh, y_sh), height_sh)
    rect(screen, (0, 0, 255), (x_sh - height_sh, y_sh - height_sh, 2*height_sh, height_sh))
    polygon(screen, (120, 50, 50), [(x_sh + width_sh, y_sh), (x_sh + width_sh + int(1/3*width_sh), y_sh), (x_sh + width_sh, y_sh + height_sh)])
    circle(screen, (255, 255, 255), (x_sh + width_sh + int(1/9*width_sh), y_sh + int(0.4*height_sh)), int(0.25*height_sh))
    circle(screen, (0, 0, 0), (x_sh + width_sh + int(1/9*width_sh), y_sh + int(0.4*height_sh)), int(0.25*height_sh) +1, 1)
    rect(screen, (0, 0, 0), (x_sh + int(0.4*width_sh), y_sh - heigth_mast, width_mast, heigth_mast))
    polygon(screen, (255, 230, 180), [(x_sh + int(0.4*width_sh) + width_mast, y_sh - heigth_mast), (x_sh + int(0.4*width_sh) + width_mast + width_sail, y_sh - int(0.5*heigth_mast)), (x_sh + int(0.4*width_sh) + width_mast, y_sh), (x_sh + int(0.4*width_sh) + width_mast + int(0.2*width_sail), y_sh - int(0.5*heigth_mast))])
    polygon(screen, (150, 100, 100), [(x_sh + int(0.4*width_sh) + width_mast, y_sh - heigth_mast), (x_sh + int(0.4*width_sh) + width_mast + width_sail + 1, y_sh - int(0.5*heigth_mast)), (x_sh + int(0.4*width_sh) + width_mast, y_sh), (x_sh + int(0.4*width_sh) + width_mast + int(0.2*width_sail) - 1, y_sh - int(0.5*heigth_mast))], 1)
    line(screen, (150, 100, 100), (x_sh + int(0.4*width_sh) + width_mast + width_sail + 1, y_sh - int(0.5*heigth_mast)), (x_sh + int(0.4*width_sh) + width_mast + int(0.2*width_sail) - 1, y_sh - int(0.5*heigth_mast)))


cloud(150, 100, 20)
cloud(100, 150, 25)
cloud(300, 100, 35)
umbrella(120, 260, 7, 200, 70, 40)
umbrella(220, 290, 3, 100, 35, 20)
ship(420, 250, 150, 35, 7, 100, 60)
ship(200, 220, 75, 15, 3, 50, 30)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
