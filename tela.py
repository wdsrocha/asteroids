import pygame
from pygame import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

def imprimir_texto(text, tamanho):
    basicfont = pygame.font.SysFont(None, tamanho)
    texto = basicfont.render(text, True, WHITE)
    return texto

def cria_nave(posicao):
    nave = pygame.surface.Surface((24, 34))
    nave_linha1 = pygame.draw.line(nave, WHITE, (0, 34), (12, 0), 1)
    nave_linha2 = pygame.draw.line(nave, WHITE, (24, 34), (12, 0), 1)
    nave_linha3 = pygame.draw.line(nave, WHITE, (3, 24), (21, 24), 1)
    tela.blit(nave, posicao)
    return nave

tela = (800, 600)

tela = pygame.display.set_mode(tela)

pygame.display.set_caption("Asteroids")

tela.fill(BLACK)

clock = pygame.time.Clock()

score = imprimir_texto('0', 25)
lifes = imprimir_texto('3 x', 35)
production = imprimir_texto('UEA - 2017', 15)

tela.blit(score, (50, 25))
tela.blit(lifes, (60, 45))
tela.blit(production, (400, 570))
nave = cria_nave((125, 45))

finaliza = True

while finaliza:

    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finaliza = False

    pygame.display.update()

    taxa_frame = clock.tick(70)

pygame.quit()
