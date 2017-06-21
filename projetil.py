import pygame, fisica

def cria_projetil():
    projetil = {}
    projetil['corpo'] = fisica.cria_corpo()
    return projetil


def atualiza_projetil(projetil):
    projetil['corpo'] = fisica.atualiza_corpo(projetil['corpo'])
    return projetil


def mostra_projetil(projetil, tela):
    corpo = projetil['corpo']
    x, y = int(corpo['posicao'].x), int(corpo['posicao'].y)
    pygame.draw.circle(tela, (255,255,255), (x, y), 3, 3)
