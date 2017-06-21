from pygame.math import Vector2 as Vector

if __name__ == '__main__':
    import pygame, fisica, math, personagens, random, screen, sounds, menu, highscore, asteroid
    import projetil, nave

    pygame.init()
    tela = pygame.display.set_mode((screen.dimensoes[0], screen.dimensoes[1]))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Projéteis da nave
    projeteis = []

    passos_asteroide = 90
    asteroides = []

    # Instanciando um jogador (nave) no centro da tela
    jogador = nave.cria_nave((screen.dimensoes[0]/2, screen.dimensoes[1]/2))

    nave_rotation_speed = 360  # Graus por segundo

    asteroide = asteroid.cria_arteroide(tela, (100, 100))

    pontos = 0
    vidas = 3

    shotspeed = 1

    screen.print_background(tela)
    pygame.display.update()
    menu.menu_game(tela, screen)

    while 1:

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
                    projeteis.append(projetil.cria_projetil(
                        jogador['corpo']['posicao'],
                        math.radians(jogador['corpo']['direcao'])))
                    sounds.tiro_nave()
                    pontos += 1
                    if pontos % 100 == 0:
                        vidas += git

        keys = pygame.key.get_pressed()

        rotation_direction = 0.

        if keys[pygame.K_LEFT]:
            rotation_direction = +1.0

        if keys[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if keys[pygame.K_UP]:
            jogador = nave.ativa_propulsao(jogador)
            # faz o foguete aparecer
            personagens.cria_turbina(tela, jogador['surface'])
            sounds.turbina_nave()
        else:
            pygame.draw.polygon(
                jogador['surface'], BLACK, ((13, 17), (0, 13), (13, 9)), 1)

        time_based = clock.tick()
        time_passed_seconds = time_based / 1000.0

        # asteroid
        if not passos_asteroide:
            passos_asteroide = 90
            asteroides.append(asteroid.cria_arteroide(tela, (100, 100)))
        else:
            passos_asteroide -= 1

        for asteroide_atual in asteroides:
            asteroid.atualiza_asteroide(asteroide_atual)
            tela.blit(asteroide_atual['surface'], asteroide_atual['corpo']['posicao'])

        for projetil_atual in projeteis:
            projetil.atualiza_projetil(projetil_atual)
            projetil.mostra_projetil(projetil_atual, tela)

        screen.print_tabela(pontos, vidas, tela)

        nave.atualiza_nave(
            jogador,
            rotation_direction,
            time_passed_seconds)
        nave.mostra_nave(jogador, tela)

        pygame.display.update()
        asteroid.remove_asteroide_usados()
