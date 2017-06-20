from pygame.math import Vector2 as Vector

if __name__ == '__main__':
    import pygame, fisica, math, personagens, random, screen, sounds

    pygame.init()
    tela = pygame.display.set_mode((screen.dimensoes[0], screen.dimensoes[1]))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ROTACAO = 0
    # nave_surface = pygame.image.load('./assets/images/jogador.png')

    nave_surface = personagens.cria_nave(tela, (400, 200))

    nave_surface = pygame.transform.rotozoom(nave_surface, -90, 1)

    nave = fisica.cria_corpo(screen.dimensoes[0] / 2, screen.dimensoes[1] / 2)

    nave_rotation = 90
    nave_rotation_speed = 360  # Graus por segundo

    pontos = 0
    vidas = 3

    shotspeed = 1

    while 1:

        screen.print_background(tela)

        forca = Vector(0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        rotation_direction = 0.

        if keys[pygame.K_LEFT]:
            rotation_direction = +1.0

        if keys[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if keys[pygame.K_LSHIFT]:
            nave['posicao'] = random.randint(0, screen.dimensoes[0]), random.randint(0, screen.dimensoes[1])

        if keys[pygame.K_UP]:
            forca += fisica.cria_vetor_unitario(math.radians(nave_rotation))

        if keys[pygame.K_SPACE]:
            sounds.tiro_nave()
            pontos += 1
            if pontos % 100 == 0:
                vidas += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.polygon(nave_surface, WHITE, ((13, 17), (0, 13), (13, 9)), 1)
                sounds.turbina_nave()
                # teta = math.radians(nave_rotation)
                # x = math.cos(teta)
                # y = math.sin(teta)
                # forca += Vector(x, -y)
        else:
            pygame.draw.polygon(nave_surface, BLACK, ((13, 17), (0, 13), (13, 9)), 1)

        time_based = clock.tick()
        time_passed_seconds = time_based / 1000.0

        rotated_nave = pygame.transform.rotate(nave_surface, nave_rotation)
        w, h = rotated_nave.get_size()
        sprite_draw_pos = Vector(nave['posicao'].x - w / 2, nave['posicao'].y - h / 2)
        nave_rotation += rotation_direction * nave_rotation_speed * time_passed_seconds

        nave = fisica.aplica_forca(nave, forca)
        nave = fisica.atualiza_corpo(nave)
        nave = fisica.aplica_atrito(nave, 0.1)
        screen.corrige_posicao(nave)
        tela.blit(rotated_nave, (sprite_draw_pos.x, sprite_draw_pos.y))
        screen.print_tabela(pontos, vidas, tela)

        pygame.display.update()
