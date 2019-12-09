import pygame

import personagens

dimensoes = (800, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()


def criar_texto(text, tamanho):
    basicfont = pygame.font.Font("assets/fonts/bitdust1.ttf", tamanho)
    texto = basicfont.render(text, True, WHITE)
    return texto


def print_background(tela):
    pygame.display.set_caption("Asteroids")
    background_file = "assets/images/space.jpg"
    background = pygame.image.load(background_file).convert()
    tela.blit(background, (0, 0))


def print_tabela(pontos, vidas, tela):
    score = criar_texto(str(pontos), 25)
    lifes = criar_texto((str(vidas) + " x"), 25)
    production = criar_texto("Sistemas de Informação", 15)
    university = criar_texto("UEA - 2017", 15)

    tela.blit(score, (50, 20))
    tela.blit(lifes, (60, 55))
    personagens.cria_nave(tela, (130, 45))
    tela.blit(production, (300, 570))
    tela.blit(university, (360, 585))


def corrige_posicao(corpo, surface):
    w, h = surface.get_size()
    if corpo["posicao"].x > dimensoes[0]:
        corpo["posicao"].x = -w
    if corpo["posicao"].x + w < 0:
        corpo["posicao"].x = dimensoes[0]
    if corpo["posicao"].y > dimensoes[1]:
        corpo["posicao"].y = -h
    if corpo["posicao"].y + h < 0:
        corpo["posicao"].y = dimensoes[1]


def tem_colisao(objetos):
    hitboxes = []
    for objeto in objetos:
        hitbox = objeto["surface"].get_rect()
        hitbox.x = objeto["corpo"]["posicao"].x
        hitbox.y = objeto["corpo"]["posicao"].y
        hitboxes.append(hitbox)
    for i in range(1, len(hitboxes)):
        if hitboxes[i - 1].colliderect(hitboxes[i]):
            return True
    return False
