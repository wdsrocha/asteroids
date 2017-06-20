from pygame.math import Vector2 as Vector

LARGURA = 800
ALTURA = 600


def corrige_posicao(corpo):
    if corpo['posicao'].x > LARGURA:
        corpo['posicao'].x = 0
    if corpo['posicao'].x < 0:
        corpo['posicao'].x = LARGURA

    if corpo['posicao'].y > ALTURA:
        corpo['posicao'].y = 0
    if corpo['posicao'].y < 0:
        corpo['posicao'].y = ALTURA

    return corpo


if __name__ == '__main__':
    import pygame, fisica, math, personagens, random, screen, sounds

    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ROTACAO = 0
    # nave_surface = pygame.image.load('./assets/images/jogador.png')

    nave_surface = personagens.cria_nave(tela, (400, 200))

    nave_surface = pygame.transform.rotozoom(nave_surface, -90, 1)

    nave = fisica.cria_corpo(LARGURA / 2, ALTURA / 2)

    nave_rotation = 90
    nave_rotation_speed = 360  # Graus por segundo

    pontos = 0
    vidas = 3

    shotspeed = 1

    while 1:

        screen.print_background(tela)

        clock.tick(60)

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
            nave['posicao'] = random.randint(0, LARGURA), random.randint(0, ALTURA)

        if keys[pygame.K_UP]:
            forca += fisica.cria_vetor_unitario(math.radians(nave_rotation))

        if keys[pygame.K_SPACE]:
            sounds.tiro_nave()
            missil = personagens.missil(tela)

            for i in range(50):
                tela.blit(missil, (int(nave['posicao'].x - i), int(nave['posicao'].y - i)))
                pygame.display.update()

            print(nave['posicao'])
            print(nave)




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

        rotated_nave = pygame.transform.rotate(nave_surface, nave_rotation)

        time_based = clock.tick()
        time_passed_seconds = time_based / 20.0

        nave_rotation += rotation_direction * nave_rotation_speed * time_passed_seconds

        nave = fisica.aplica_forca(nave, forca)
        nave = fisica.atualiza_corpo(nave)
        nave = fisica.aplica_atrito(nave, 0.1)
        corrige_posicao(nave)
        tela.blit(rotated_nave, nave['posicao'])
        screen.print_tabela(pontos, vidas, tela)

        pygame.display.update()
