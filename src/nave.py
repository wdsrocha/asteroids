import math

import pygame

import fisica
import screen

WHITE = (255, 255, 255)

VELOCIDADE_DE_ROTACAO = 360  # 360 graus por segundo


def cria_nave(posicao):
    nave = {}

    nave["contador"] = 0

    nave["corpo"] = fisica.cria_corpo(posicao[0], posicao[1])
    nave["corpo"]["massa"] = 5
    nave["corpo"]["direcao"] = 90

    nave["surface"] = pygame.surface.Surface(
        (24, 38), pygame.SRCALPHA, 32
    ).convert_alpha()
    pygame.draw.line(nave["surface"], WHITE, (1, 34), (12, 1), 2)
    pygame.draw.line(nave["surface"], WHITE, (24, 34), (12, 1), 2)
    pygame.draw.line(nave["surface"], WHITE, (3, 24), (21, 24), 2)
    nave["surface"] = pygame.transform.rotozoom(nave["surface"], -90, 1)

    return nave


def atualiza_nave(nave, direcao, tempo_passado):
    if nave["corpo"]["posicao"] == (-100, -100):
        return
    nave["contador"] += 1
    fisica.atualiza_corpo(nave["corpo"])
    fisica.aplica_atrito(nave["corpo"], 0.1)
    nave["corpo"]["direcao"] += direcao * VELOCIDADE_DE_ROTACAO * tempo_passado


def mostra_nave(nave, tela):
    if nave["corpo"]["posicao"] == (-100, -100):
        return
    if nave["contador"] < 90 and nave["contador"] % 5 == 0:
        return
    nave_rotacionada = pygame.transform.rotate(
        nave["surface"], nave["corpo"]["direcao"]
    )
    w, h = nave_rotacionada.get_size()
    origem_x = nave["corpo"]["posicao"].x - w / 2
    origem_y = nave["corpo"]["posicao"].y - h / 2
    screen.corrige_posicao(nave["corpo"], nave["surface"])
    tela.blit(nave_rotacionada, (origem_x, origem_y))


# Aplica força no corpo da nave, alterando sua aceleração
def ativa_propulsao(nave):
    angulo = math.radians(nave["corpo"]["direcao"])
    forca = fisica.cria_vetor_unitario(angulo)
    nave["corpo"] = fisica.aplica_forca(nave["corpo"], forca)
