import pygame
from pygame import *

black = (0,0,0)

pygame.init()

tela = (800, 600)

tela = pygame.display.set_mode(tela)

pygame.display.set_caption("Hello World")

tela.fill(black)

pygame.quit()