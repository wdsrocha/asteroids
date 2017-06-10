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
    return nave


# girar nave
def girar_nave(nave, angulo):
    return True


# função que faz a nave aparecer do outro lado da tela
def nave_borda(sprite, x):
    tela.blit(sprite, (x, 100))
    x += 1
    if x > 800:
        x -= 800
    pygame.display.update()


# Personagem: Asteroide
# Função que cria asteroides de formatos diferentes aleatoriamente
def cria_arteroide(posicao):
    arteroide = pygame.surface.Surface((90, 84))

    pontos_asteroide_1 = (
        (19, 0), (40, 18), (60, 0), (80, 18), (64, 38), (78, 59), (50, 80), (15, 80), (0, 63), (0, 20))

    pontos_asteroide_2 = (
        (3, 21), (33, 21), (22, 3), (52, 3), (82, 21), (82, 31), (46, 42), (82, 62), (63, 82), (47, 71), (19, 82),
        (3, 51))

    pontos_asteroide_3 = (
        (32, 5), (63, 5), (82, 33), (82, 47), (53, 82), (32, 82), (38, 47), (18, 82), (3, 53), (21, 43), (3, 35))

    asteroides = [pontos_asteroide_1, pontos_asteroide_2, pontos_asteroide_3]

    pygame.draw.polygon(arteroide, WHITE, asteroides[random.randint(0, 2)], 1)

    tela.blit(arteroide, posicao)


# função que cria o personagem patrulha

def cria_patrulha(posicao):
    patrulha = pygame.surface.Surface((45, 27))

    contornos = (
        (16, 0), (28, 0), (33, 9), (43, 17), (32, 26), (12, 26), (1, 17), (11, 9))

    pygame.draw.polygon(patrulha, WHITE, contornos, 1)
    pygame.draw.line(patrulha, WHITE, (11, 9), (33, 9), 1)
    pygame.draw.line(patrulha, WHITE, (12, 26), (32, 26), 1)
    pygame.draw.line(patrulha, WHITE, (1, 17), (43, 17), 1)

    tela.blit(patrulha, posicao)


nave = cria_nave((200, 200))
patrulha = cria_patrulha((150, 200))

cria_arteroide((400, 50))
cria_arteroide((300, 300))
cria_arteroide((400, 400))

pygame.display.update()

finaliza = False

while not finaliza:

    # --- Loop principal
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finaliza = True

pygame.quit()
