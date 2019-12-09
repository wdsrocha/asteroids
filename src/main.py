import math
import random

import pygame

import asteroide
import highscore
import menu
import nave
import personagens
import projetil
import screen
import sounds


def main():
    highscore.cria_tabela()
    pygame.init()
    tela = pygame.display.set_mode((screen.dimensoes[0], screen.dimensoes[1]))
    clock = pygame.time.Clock()
    BLACK = (0, 0, 0)
    QUANTIDADE_ASTEROIDES = 5
    DISTANCIA_MINIMA = 200

    # Projéteis da nave
    projeteis = []

    # Asteróides do espaço
    asteroides = []
    pontuacao_asteroide = [20, 50, 100]

    # Instanciando um jogador (nave) no centro da tela
    jogador = nave.cria_nave((screen.dimensoes[0] / 2, screen.dimensoes[1] / 2))
    jogador["contador"] = 90
    tempo_de_espera = 0

    # Pontuação e quantidade de vidas restantes do jogador
    pontos = 0
    vidas = 3
    vidas_ganhas = 0
    vidas_perdidas = 0

    screen.print_background(tela)
    pygame.display.update()
    menu.menu_game(tela, screen)

    music = [0, 1]

    while 1:

        if vidas <= 0:
            menu.game_over(tela, screen, pontos)

        screen.print_background(tela)

        time_based = clock.tick()
        time_passed_seconds = time_based / 1000.0

        if jogador["corpo"]["posicao"] == (-100, -100):
            tempo_de_espera += 1
        if tempo_de_espera >= 30:
            x = random.randint(0, screen.dimensoes[0])
            y = random.randint(0, screen.dimensoes[1])
            jogador = nave.cria_nave((x, y))
            jogador["contador"] = 90
            tempo_de_espera = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    projeteis.append(
                        projetil.cria_projetil(
                            jogador["corpo"]["posicao"],
                            math.radians(jogador["corpo"]["direcao"]),
                        )
                    )
                    sounds.tiro_nave()
                if event.key == pygame.K_LSHIFT:
                    if jogador["corpo"]["posicao"] != (-100, -100):
                        jogador = nave.cria_nave((-100, -100))
                        tempo_de_espera = 0

        keys = pygame.key.get_pressed()

        rotation_direction = 0.0

        if keys[pygame.K_LEFT]:
            rotation_direction = +1.0

        if keys[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if keys[pygame.K_UP]:
            nave.ativa_propulsao(jogador)
            personagens.cria_turbina(tela, jogador["surface"])
            # sounds.turbina_nave()
        else:
            pygame.draw.polygon(
                jogador["surface"], BLACK, ((13, 17), (0, 13), (13, 9)), 0
            )

        # Asteroides
        # Cria asteróides no começo do jogo ou ao fim de uma onda
        if len(asteroides) == 0:
            candidatos = []
            i0, j0 = jogador["corpo"]["posicao"]
            for i in range(screen.dimensoes[0]):
                for j in range(screen.dimensoes[1]):
                    # Se o pixel está à uma certa distância da
                    # nave, ele é um candidato à conter um asteroide
                    if abs(i0 - i) + abs(j0 - j) > DISTANCIA_MINIMA:
                        candidatos.append((i, j))
            random.shuffle(candidatos)
            for i in range(QUANTIDADE_ASTEROIDES):
                asteroides.append(asteroide.cria_asteroide(candidatos[i], 0))

        # Atualiza e imprime os asteróides na tela
        for asteroide_atual in asteroides:
            asteroide.atualiza_asteroide(asteroide_atual)
            asteroide.mostra_asteroide(asteroide_atual, tela)

        # Projéteis
        for projetil_atual in projeteis:
            projetil.atualiza_projetil(projetil_atual)
            projetil.mostra_projetil(projetil_atual, tela)
            # limite de distancia em que o ponto pode viajar
            if projetil_atual["contador"] > 20:
                projeteis.remove(projetil_atual)

        # Jogador/Nave
        nave.atualiza_nave(jogador, rotation_direction, time_passed_seconds)
        nave.mostra_nave(jogador, tela)

        # Verifica colisão
        proximos_asteroides = []
        for asteroide_atual in asteroides:
            tamanho = asteroide_atual["tamanho"]
            # Verifica se colidiu com projétil
            for projetil_atual in projeteis:
                if screen.tem_colisao([asteroide_atual, projetil_atual]):
                    if tamanho < 2:
                        for i in range(2):
                            proximos_asteroides.append(
                                asteroide.cria_asteroide(
                                    asteroide_atual["corpo"]["posicao"], tamanho + 1
                                )
                            )
                    asteroides.remove(asteroide_atual)
                    projeteis.remove(projetil_atual)
                    pontos += pontuacao_asteroide[tamanho]
            # Se não colidiu com projétil, verifica se colidiu com
            # o jogador (nave)
            if jogador["contador"] >= 90 and screen.tem_colisao(
                [asteroide_atual, jogador]
            ):
                if tamanho < 2:
                    for i in range(2):
                        proximos_asteroides.append(
                            asteroide.cria_asteroide(
                                asteroide_atual["corpo"]["posicao"], tamanho + 1
                            )
                        )
                pontos += pontuacao_asteroide[tamanho]
                asteroides.remove(asteroide_atual)
                sounds.explosao_asteroide_grande()
                origem_x = screen.dimensoes[0] / 2
                origem_y = screen.dimensoes[1] / 2
                jogador = nave.cria_nave((origem_x, origem_y))
                vidas_perdidas += 1
        asteroides += proximos_asteroides

        # Pontuação
        vidas_ganhas = pontos // 1000
        vidas = 3 + vidas_ganhas - vidas_perdidas
        screen.print_tabela(pontos, vidas, tela)

        pygame.display.update()

        # BG MUSIC
        if music[0] % 15 == 0:
            sounds.fundo_musical(music[1])
            music[1] *= -1

        music[0] += 1


if __name__ == "__main__":
    main()
