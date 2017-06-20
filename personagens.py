import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Personagem: Nave Espacial
def cria_nave(tela, posicao):
    nave = pygame.surface.Surface((24, 38), pygame.SRCALPHA, 32).convert_alpha()
    pygame.draw.line(nave, WHITE, (1, 34), (12, 1), 1)
    pygame.draw.line(nave, WHITE, (24, 34), (12, 1), 1)
    pygame.draw.line(nave, WHITE, (3, 24), (21, 24), 1)
    tela.blit(nave, posicao)
    return nave


def cria_turbina(tela, nave_surface):
    turbina_nave = pygame.draw.polygon(nave_surface, WHITE, ((13, 17), (0, 13), (13, 9)), 1)
    return turbina_nave


# projétil/míssil 
def cria_projetil(tela):
    cria_projetil = pygame.surface.Surface((2, 2), pygame.SRCALPHA, 32).convert_alpha()
    pygame.draw.circle(cria_projetil, WHITE, (200,300), 10, 0)
    return cria_projetil


# Personagem: Asteroide

# Função que cria asteroides de formatos diferentes aleatoriamente
def cria_arteroide(tela, posicao):
    arteroide = pygame.surface.Surface((90, 84), pygame.SRCALPHA, 32).convert_alpha()

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

def cria_patrulha(tela, posicao, tamanho):
    patrulha = pygame.surface.Surface((45, 27), pygame.SRCALPHA, 32).convert_alpha()

    contornos = (
        (16, 0), (28, 0), (33, 9), (43, 17), (32, 26), (12, 26), (1, 17), (11, 9))

    pygame.draw.polygon(patrulha, WHITE, contornos, 1)
    pygame.draw.line(patrulha, WHITE, (11, 9), (33, 9), 1)
    pygame.draw.line(patrulha, WHITE, (12, 26), (32, 26), 1)
    pygame.draw.line(patrulha, WHITE, (1, 17), (43, 17), 1)

    tela.blit(patrulha, posicao)