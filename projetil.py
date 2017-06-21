import pygame, fisica, personagens, testes, screen

def cria_projetil(posicao, direcao):
    projetil = {}

    projetil['contador'] = 0

    projetil['corpo'] = fisica.cria_corpo(posicao[0], posicao[1])
    projetil['corpo']['massa'] = 0.05
    forca = fisica.cria_vetor_unitario(direcao)
    projetil['corpo'] = fisica.aplica_forca(projetil['corpo'], forca)

    projetil['surface'] = pygame.surface.Surface((3, 3), pygame.SRCALPHA, 32).convert_alpha()
    pygame.draw.circle(projetil['surface'], (255,255,255), (0,0), 10, 10)

    return projetil


def atualiza_projetil(projetil):
    projetil['contador'] += 1
    projetil['corpo'] = fisica.atualiza_corpo(projetil['corpo'])
    return projetil


def mostra_projetil(projetil, tela):
    screen.corrige_posicao(projetil['corpo'],projetil['surface'])
    tela.blit(projetil['surface'], projetil['corpo']['posicao'])
