from pygame.math import Vector2 as Vector

if __name__ == '__main__':
    import pygame, fisica, math, personagens, random, asteroide
    import projetil, nave, screen, sounds, menu, highscore

    pygame.init()
    tela = pygame.display.set_mode((screen.dimensoes[0], screen.dimensoes[1]))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    QUANTIDADE_ASTEROIDES = 7
    DISTANCIA_MINIMA = 200

    # Projéteis da nave
    projeteis = []

    # Asteróides do espaço
    asteroides = []

    # Instanciando um jogador (nave) no centro da tela
    jogador = nave.cria_nave((screen.dimensoes[0]/2, screen.dimensoes[1]/2))

    # Pontuação e quantidade de vidas restantes do jogador
    pontos = 0
    vidas = 3

    screen.print_background(tela)
    pygame.display.update()
    menu.menu_game(tela, screen)

    music = [0, 1]

    while 1:

        if vidas <= 0:
            menu.game_over(tela, screen, pontos)

        screen.print_background(tela)
        forca = Vector(0, 0)

        time_based = clock.tick()
        time_passed_seconds = time_based / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

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
                        vidas += 1

        keys = pygame.key.get_pressed()

        rotation_direction = 0.

        if keys[pygame.K_LEFT]:
            rotation_direction = +1.0

        if keys[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if keys[pygame.K_UP]:
            nave.ativa_propulsao(jogador)
            personagens.cria_turbina(tela, jogador['surface'])
            # sounds.turbina_nave()
        else:
            pygame.draw.polygon(
                jogador['surface'], BLACK, ((13, 17), (0, 13), (13, 9)), 1)


        # Asteroides
        if len(asteroides) == 0:
            candidatos = []
            i0, j0 = jogador['corpo']['posicao']
            for i in range(screen.dimensoes[0]):
                for j in range(screen.dimensoes[1]):
                    # Se o pixel está à uma certa distância da
                    # nave, ele é um candidato à conter um asteroide
                    if abs(i0-i) + abs(j0-j) > DISTANCIA_MINIMA:
                        candidatos.append((i, j))
            random.shuffle(candidatos)
            for i in range(QUANTIDADE_ASTEROIDES):
                asteroides.append(asteroide.cria_asteroide(candidatos[i], 0))

        for asteroide_atual in asteroides:
            asteroide.atualiza_asteroide(asteroide_atual)
            asteroide.mostra_asteroide(asteroide_atual, tela)


        # Projéteis
        for projetil_atual in projeteis:
            projetil.atualiza_projetil(projetil_atual)
            projetil.mostra_projetil(projetil_atual, tela)


        # Jogador/Nave
        nave.atualiza_nave(
            jogador,
            rotation_direction,
            time_passed_seconds)
        nave.mostra_nave(jogador, tela)


        # Verifica colisão
        for asteroide_atual in asteroides:
            if screen.tem_colisao([asteroide_atual, jogador]):
                sounds.explosao_asteroide_grande()
                origem_x = screen.dimensoes[0]/2
                origem_y = screen.dimensoes[1]/2
                jogador = nave.cria_nave((origem_x, origem_y))
                vidas -= 1
                pontos += 20

        # Pontuação
        screen.print_tabela(pontos, vidas, tela)

        pygame.display.update()

        # BG MUSIC
        if music[0] % 15 == 0:
            sounds.fundo_musical(music[1])
            music[1] *= -1

        music[0] += 1
