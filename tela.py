import pygame
from pygame import *

BLACK = (0,0,0)

pygame.init()

tela = (800, 600)

tela = pygame.display.set_mode(tela)

pygame.display.set_caption("Asteroids")

tela.fill(BLACK)


pygame.display.update()

finaliza = False

while not finaliza:

    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finaliza = True

pygame.quit()