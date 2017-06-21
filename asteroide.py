import pygame, personagens, random, fisica, screen

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def cria_asteroide(tela, posicao):
    asteroide = {}

    asteroide['corpo'] = fisica.cria_corpo(posicao[0], posicao[1])
    asteroide['corpo']['massa'] = 3.0
    forca = fisica.cria_vetor_unitario(random.uniform(0, 6.28))
    fisica.aplica_forca(asteroide['corpo'], forca)

    asteroide['surface'] = pygame.surface.Surface(
        (90, 84), pygame.SRCALPHA, 32).convert_alpha()
    pontos_asteroide_1 = (
        (19,  0), (40, 18), (60,  0), (80, 18), (64, 38),
        (78, 59), (50, 80), (15, 80), ( 0, 63), ( 0, 20))
    pontos_asteroide_2 = (
        ( 3, 21), (33, 21), (22,  3), (52,  3), (82, 21), (82, 31),
        (46, 42), (82, 62), (63, 82), (47, 71), (19, 82), ( 3, 51))
    pontos_asteroide_3 = (
        (32,  5), (63,  5), (82, 33), (82, 47), (53, 82),
        (32, 82), (38, 47), (18, 82), ( 3, 53), (21, 43), (3, 35))
    asteroides = [pontos_asteroide_1, pontos_asteroide_2, pontos_asteroide_3]
    pygame.draw.polygon(asteroide['surface'], WHITE, asteroides[random.randint(0, 2)], 1)

    return asteroide


def atualiza_asteroide(asteroide):
    asteroide['corpo'] = fisica.atualiza_corpo(asteroide['corpo'])
    return asteroide


def mostra_asteroide(asteroide, tela):
    screen.corrige_posicao(asteroide['corpo'])
    tela.blit(asteroide['surface'], asteroide['corpo']['posicao'])
