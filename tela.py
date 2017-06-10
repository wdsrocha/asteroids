import pygame, personagens
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

def print_contadores(pontos, vidas, screen):
    score = imprimir_texto(pontos, 25)
    lifes = imprimir_texto((vidas+' x'), 35)
    production = imprimir_texto('UEA - 2017', 15)

    tela.blit(score, (50, 25))
    tela.blit(lifes, (60, 45))
    tela.blit(production, (400, 570))
    nave = personagens.cria_nave(screen, (125, 45))
    tela.blit(nave,(125,45))


tela = (800, 600)

tela = pygame.display.set_mode(tela)

pygame.display.set_caption("Asteroids")

clock = pygame.time.Clock()

finaliza = True

while finaliza:

    background = pygame.image.load('./assets/images/space.jpg').convert()
    tela.blit(background, (0, 0))

    print_contadores('0','3',tela)

    taxa_frame = clock.tick(60)
    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finaliza = False

    pygame.display.update()



pygame.quit()
