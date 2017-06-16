from sys import exit
from untitled.gameobjeto.vector2 import Vector2
# from pygame.math import Vector2

if __name__ == '__main__':
    import pygame, math, random

    # prepara para podermos usar o pygame
    pygame.init()

    # cria uma tela 640x480
    tela = pygame.display.set_mode((640, 480), 0, 32)

    # guarda o nome do arquivo
    plano_fundo_nome = 'space.jpg'
    nave_name = 'jogador.png'

    # carrega a imagem
    plano_fundo = pygame.image.load(plano_fundo_nome).convert()
    sprite = pygame.image.load(nave_name).convert_alpha()

    # coloca o titulo
    pygame.display.set_caption('Asteroids')

    # objeto clock
    clock = pygame.time.Clock()

    sprite_pos = Vector2(200, 150)
    sprite_speed = 300
    sprite_rotation = 0
    sprite_rotation_speed = 360  # Graus por segundo
    heading = Vector2()
    # loop do game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # retornar uma tecla pressionada
        teclas_precionadas = pygame.key.get_pressed()

        rotation_direction = 0.
        movement_direction = 0.

        if teclas_precionadas[pygame.K_LEFT]:
            rotation_direction = +1.0

        if teclas_precionadas[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if teclas_precionadas[pygame.K_LSHIFT]:
            nave_posicao = random.randint(0, 800), random.randint(0, 600)

        if teclas_precionadas[pygame.K_UP]:
            rotation_direction = +1.0

        if teclas_precionadas[pygame.KEYDOWN]:
            rotation_direction = -1.0

        # coloca uma surperficie em cima da tela.
        tela.blit(plano_fundo, (0, 0))

        rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
        w, h = rotated_sprite.get_size()
        sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
        tela.blit(rotated_sprite, (sprite_draw_pos.x, sprite_draw_pos.y))

        # limitador para nao passar de 30 interacoes por segundo
        tempo_passado = clock.tick()
        tempo_passado_segundos = tempo_passado / 1000.0

        sprite_rotation += rotation_direction * sprite_rotation_speed * tempo_passado_segundos
        heading_x = math.sin(sprite_rotation * math.pi / 180.0)
        heading_y = math.cos(sprite_rotation * math.pi / 180.0)
        heading = Vector2(heading_x, heading.y)
        heading *= movement_direction
        # sprite_pos *= heading * sprite_speed * tempo_passado_segundos

        # if posicao > 800:
        #     posicao -= 800
        # if posicao > 600:
        #     posicao -= 600

        # atualiza a telaR
        pygame.display.update()
