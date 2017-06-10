import math
from pygame.math import Vector2 as Vector

VELOCIDADE_MAXIMA = 3

def aplicaForca(corpo, forca):
    corpo['aceleracao'] = forca/corpo['massa']
    return corpo

def limitaVetor(u, lim):
    if Vector.length(u) > lim**2:
        u = Vector.normalize(u)*lim
    return u

def atualiza(corpo):
    corpo['velocidade'] += corpo['aceleracao']
    corpo['velocidade'] = limitaVetor(corpo['velocidade'], VELOCIDADE_MAXIMA)
    corpo['posicao'] += corpo['velocidade']
    corpo['aceleracao'] = 0
    return corpo

def criaCorpo():
    '''Retorna um dicionário com as características de um corpo
    físico'''
    corpo = {}
    corpo['velocidade'] = Vector()
    corpo['aceleracao'] = Vector()
    corpo['posicao'] = Vector()
    corpo['massa'] = 1
    corpo['angulo'] = 0
    return corpo
