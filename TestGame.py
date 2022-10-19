import sys
import pygame
from pygame import *

pygame.init()

window = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption("CoolGame")

FPS = pygame.time.Clock()

while True:
    window.fill((0,0,255))
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
    FPS.tick(60)
