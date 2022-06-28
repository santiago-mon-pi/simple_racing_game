import pygame
from pygame.locals import *

size = width, height = (800, 800)

pygame.init()
running = True
# set window size
screen = pygame.display.set_mode((size))
# sets title
pygame.display.set_caption("Monpi's race game")
#set background color
screen.fill((((48, 25, 52))))

# applies changes
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
