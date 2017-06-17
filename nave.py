import pygame
from asteroids.vector2 import Vector2


# Aplica força no corpo da nave, alterando sua aceleração
def ativa_propulsao(nave):
    angulo = math.radians(nave['corpo']['direcao'])
    forca = fisica.cria_vetor_unitario(angulo)
    nave['corpo'] = fisica.aplica_forca(nave['corpo'], forca)
    return nave


# Tudo daqui pra baixo falta arrumar
def atualiza_nave(nave):
    nave['corpo'] = fisica.atualiza_corpo(nave['corpo'])


def desenha_nave(nave):
    pass


# def rotaciona_nave(sprite_pos,w,h,rotation_direction,tempo_passado_segundos):
#     sprite_rotation = 0
#     sprite_rotation_speed = 360
#     rotation_direction = 0.
#
#     sprite_rotation += rotation_direction * sprite_rotation_speed * tempo_passado_segundos
#     sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
#
#     return (sprite_draw_pos.x, sprite_draw_pos.y)
