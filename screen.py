import pygame, personagens
from pygame import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

def criar_texto(text, tamanho):
    basicfont = pygame.font.SysFont(None, tamanho)
    texto = basicfont.render(text, True, WHITE)
    return texto

def print_background(tela):
    pygame.display.set_caption("Asteroids")
    background_file = 'assets/images/space.jpg'
    background = pygame.image.load(background_file).convert()
    tela.blit(background, (0, 0))

def print_tabela(pontos,vidas,tela):
    score = criar_texto(str(pontos), 25)
    lifes = criar_texto((str(vidas) + ' x'), 35)
    production = criar_texto('Sistemas de Informação', 15)
    university = criar_texto('UEA - 2017', 15)

    tela.blit(score, (50, 25))
    tela.blit(lifes, (60, 45))
    personagens.cria_nave(tela, (125, 45))
    tela.blit(production, (350, 570))
    tela.blit(university, (380,585))