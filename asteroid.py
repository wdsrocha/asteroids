import pygame, personagens, random, fisica

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Aqui, contamos 90 passos do gameloop, então criamos um novo asteroide e acrescentamos à lista de asteroides, reiniciando o contador.
passos_asteroid = 90
asteroids = []


def cria_arteroide(tela, posicao):
    arteroide = {}
    arteroide['corpo'] = fisica.cria_corpo(posicao[0], posicao[1])
    forca = fisica.cria_vetor_unitario(random.uniform(0, 6.28))
    arteroide['corpo']['massa'] = 3.0
    arteroide['corpo'] = fisica.aplica_forca(arteroide['corpo'], forca)

    arteroide['surface'] = pygame.surface.Surface((90, 84), pygame.SRCALPHA, 32).convert_alpha()

    pontos_asteroide_1 = (
        (19, 0), (40, 18), (60, 0), (80, 18), (64, 38), (78, 59), (50, 80), (15, 80), (0, 63), (0, 20))

    pontos_asteroide_2 = (
        (3, 21), (33, 21), (22, 3), (52, 3), (82, 21), (82, 31), (46, 42), (82, 62), (63, 82), (47, 71), (19, 82),
        (3, 51))

    pontos_asteroide_3 = (
        (32, 5), (63, 5), (82, 33), (82, 47), (53, 82), (32, 82), (38, 47), (18, 82), (3, 53), (21, 43), (3, 35))

    asteroides = [pontos_asteroide_1, pontos_asteroide_2, pontos_asteroide_3]

    pygame.draw.polygon(arteroide['surface'], WHITE, asteroides[random.randint(0, 2)], 1)
    tela.blit(arteroide['surface'], arteroide['corpo']['posicao'])

    return arteroide

def atualiza_asteroide(asteroide):
    asteroide['corpo'] = fisica.atualiza_corpo(asteroide['corpo'])
    return asteroide

def move_asteroide():
    for asteroid in asteroids:
        asteroid['corpo'] = fisica.atualiza_corpo(asteroid['corpo'])


def remove_asteroide_usados():
    for asteroid in asteroids:
        if asteroid['corpo']['posicao'][1] > 560:
            asteroids.remove(asteroid)
