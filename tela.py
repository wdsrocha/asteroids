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

def print_tela(pontos, vidas):
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Asteroids")
    background = pygame.image.load('./assets/images/space.jpg').convert()
    tela.blit(background, (0, 0))

    score = imprimir_texto(str(pontos), 25)
    lifes = imprimir_texto((str(vidas) + ' x'), 35)
    production = imprimir_texto('Sistemas de Informação', 15)
    university = imprimir_texto('UEA - 2017', 15)

    tela.blit(score, (50, 25))
    tela.blit(lifes, (60, 45))
    personagens.cria_nave(tela, (125, 45))
    tela.blit(production, (350, 570))
    tela.blit(university, (380,585))



clock = pygame.time.Clock()

finaliza = True

while finaliza:

    pontos = 0
    vidas = 3
    print_tela(pontos, vidas)

    taxa_frame = 60
    clock.tick(taxa_frame)

    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finaliza = False

    pygame.display.update()


pygame.quit()
