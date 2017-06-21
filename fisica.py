from pygame.math import Vector2 as Vector
import math

#Retorna um dicionário com as características de um corpo físico
def cria_corpo(x, y):
    corpo = {}
    corpo['velocidade'] = Vector(0, 0)
    corpo['aceleracao'] = Vector(0, 0)
    corpo['posicao'] = Vector(x, y)
    corpo['massa'] = 1
    corpo['direcao'] = 0
    return corpo


def atualiza_corpo(corpo):
    corpo['velocidade'] += corpo['aceleracao']
    corpo['aceleracao'] = Vector(0, 0)
    corpo['posicao'] += corpo['velocidade']
    return corpo


def aplica_atrito(corpo, coeficiente_de_atrito):
    if corpo['velocidade'] == Vector(0, 0):
        return corpo
    atrito = -coeficiente_de_atrito*Vector.normalize(corpo['velocidade'])
    return aplica_forca(corpo, atrito)


def aplica_forca(corpo, forca):
    corpo['aceleracao'] += forca / corpo['massa']
    return corpo


def cria_vetor_unitario(angulo):
    return Vector(math.cos(angulo), -math.sin(angulo))
