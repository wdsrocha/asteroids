import pygame
from pygame import *
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

tela = (800, 600)

tela = pygame.display.set_mode(tela)

pygame.display.set_caption("Asteroids - Personagens")

tela.fill(BLACK)


# Personagem: Nave Espacial
def cria_nave(posicao):
    nave = pygame.surface.Surface((24, 34))
    nave_linha1 = pygame.draw.line(nave, WHITE, (0, 34), (12, 0), 1)
    nave_linha2 = pygame.draw.line(nave, WHITE, (24, 34), (12, 0), 1)
    nave_linha3 = pygame.draw.line(nave, WHITE, (3, 24), (21, 24), 1)
    tela.blit(nave, posicao)




cria_nave((200, 200))

pygame.display.update()

finaliza = False

while not finaliza:

    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finaliza = True

pygame.quit()
