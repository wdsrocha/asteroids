from pygame.math import Vector2 as Vector

if __name__ == '__main__':
    import pygame, fisica, math, personagens, random, screen, sounds, menu, highscore, asteroid
    import projetil

    pygame.init()
    tela = pygame.display.set_mode((screen.dimensoes[0], screen.dimensoes[1]))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Projéteis da nave
    projeteis = []

    passos_asteroide = 90
    asteroides = []

    nave_surface = personagens.cria_nave(tela, (400, 200))

    nave_surface = pygame.transform.rotozoom(nave_surface, -90, 1)

    asteroide = asteroid.cria_arteroide(tela, (100, 100))

    nave = fisica.cria_corpo(screen.dimensoes[0] / 2, screen.dimensoes[1] / 2)
    nave['massa'] = 5

    nave_rotation = 90
    nave_rotation_speed = 360  # Graus por segundo

    pontos = 0
    vidas = 3

    shotspeed = 1

    screen.print_background(tela)
    pygame.display.update()
    menu.menu_game(tela, screen)

    music = [0, 1]

    while 1:

        time_based = clock.tick()
        time_passed_seconds = time_based / 1000.0

        # BG MUSIC
        if music[0] % 25 == 0:
            sounds.fundo_musical(music[1])
            music[1] *= -1

        screen.print_background(tela)
        forca = Vector(0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                highscore.grava_pontos('Vitor', pontos)
                print(highscore.ver_highscore())
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    projeteis.append(projetil.cria_projetil(nave['posicao'], math.radians(nave_rotation)))
                    sounds.tiro_nave()
                    pontos += 1
                    if pontos % 100 == 0:
                        vidas += 1

        keys = pygame.key.get_pressed()

        rotation_direction = 0.

        if keys[pygame.K_LEFT]:
            rotation_direction = +1.0

        if keys[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if keys[pygame.K_UP]:
            forca += fisica.cria_vetor_unitario(math.radians(nave_rotation))
            # faz o foguete aparecer
            personagens.cria_turbina(tela, nave_surface)
            sounds.turbina_nave()
        else:
            pygame.draw.polygon(nave_surface, BLACK, ((13, 17), (0, 13), (13, 9)), 1)

        # asteroid
        if not passos_asteroide:
            passos_asteroide = 90
            asteroides.append(asteroid.cria_arteroide(tela, (100, 100)))
        else:
            passos_asteroide -= 1

        for i in range(len(asteroides)):
            asteroides[i] = asteroid.atualiza_asteroide(asteroides[i])
            tela.blit(asteroides[i]['surface'], asteroides[i]['corpo']['posicao'])

        for i in range(len(projeteis)):
            projeteis[i] = projetil.atualiza_projetil(projeteis[i])
            projetil.mostra_projetil(projeteis[i], tela)

        # asteroid.atualiza_asteroide()

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
        asteroid.remove_asteroide_usados()
        music[0] += 1
