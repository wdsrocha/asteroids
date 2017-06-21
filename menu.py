import pygame, highscore, testes
from pygame.locals import *

WHITE = (255, 255, 255)


# menu

def titulo_jogo(tela):
    menu_fonte_titulo = pygame.font.Font("assets/fonts/bitdust1.ttf", 100)
    menu_titulo = menu_fonte_titulo.render("ASTEROIDS", True, (WHITE))
    menu_titulo = tela.blit(menu_titulo, (400 - menu_titulo.get_width() // 2, 150 - menu_titulo.get_height() // 2))
    return menu_titulo


def titulo_game_over(tela):
    menu_fonte_titulo = pygame.font.Font("assets/fonts/bitdust1.ttf", 60)
    menu_titulo = menu_fonte_titulo.render("G A M E   O V E R", True, (WHITE))
    menu_titulo = tela.blit(menu_titulo, (400 - menu_titulo.get_width() // 2, 200 - menu_titulo.get_height() // 2))
    return menu_titulo


def menu(tela):
    menu_fonte_opcoes = pygame.font.Font("assets/fonts/bitdust1.ttf", 28)
    menu_opcoes = (
        menu_fonte_opcoes.render("PLAY GAME", True, (WHITE)),
        menu_fonte_opcoes.render("HIGH SCORES", True, (WHITE)))
    return menu_opcoes

def creditos():
    menu_fonte_creditos = pygame.font.Font("assets/fonts/bitdust1.ttf", 13)
    menu_creditos = menu_fonte_creditos.render("Pai Games Inc", True, (WHITE))

def escreve_texto(texto, tamanho):
    texto_score = pygame.font.Font("assets/fonts/bitdust1.ttf", tamanho)
    texto_score = texto_score.render(texto, True, (WHITE))
    return texto_score

def imprime_highscores(tela, screen):
    scores = highscore.ver_highscore()
    if len(scores) > 10:
        limit = 10
    else:
        limit = len(scores)

    for i in range(limit):
        texto = str(scores[i][1]) + "          " + str(scores[i][2])
        score = escreve_texto(texto.upper(), 26)
        tela.blit(score,
                  (screen.dimensoes[0] / 2 - score.get_width() // 2, 160 + 30 * i))


def imprime_creditos(tela, screen):
    data = ['Universidade do Estado do Amazonas', 'Sistemas de Informação - 2017', 'Prof. Dr. Jucimar Jr']

    alunos = ['Adham Lucas', 'Edson Barros', 'Roberta Cruz', 'Tiago Aranha', 'Vitor Simões', 'Wesley Rocha']

    uea = escreve_texto(data[0].upper(), 28)
    tela.blit(uea, (screen.dimensoes[0] / 2 - uea.get_width() // 2, 110))

    si = escreve_texto(data[1].upper(), 28)
    tela.blit(si, (screen.dimensoes[0] / 2 - si.get_width() // 2, 140))

    jr = escreve_texto(data[2].upper(), 28)
    tela.blit(jr, (screen.dimensoes[0] / 2 - jr.get_width() // 2, 180))

    for i in range(len(alunos)):
        texto = str(alunos[i])
        aluno = escreve_texto(texto.upper(), 26)
        tela.blit(aluno,
                  (screen.dimensoes[0] / 2 - aluno.get_width() // 2, 260 + 30 * i))

def abre_tela_inicial(tela, screen):
    menu_opcoes = (escreve_texto("PLAY GAME", 28), escreve_texto("HIGH SCORES", 28), escreve_texto('NEW GAME', 28),
                   escreve_texto('CRÉDITOS', 28))

    botao_high_scores_voltar = tela.blit(escreve_texto('NEW GAME', 28),
                                         (screen.dimensoes[0] / 2 - menu_opcoes[2].get_width() // 2 + 20, 540))
    screen.print_background(tela)

    titulo_jogo(tela)

    botao_play_game = tela.blit(menu_opcoes[0],
                                (screen.dimensoes[0] / 2 - menu_opcoes[0].get_width() // 2, 300))
    botao_high_scores = tela.blit(menu_opcoes[1],
                                  (screen.dimensoes[0] / 2 - menu_opcoes[1].get_width() // 2, 340))

    botao_creditos = tela.blit(menu_opcoes[3],
                               (screen.dimensoes[0] / 2 - menu_opcoes[3].get_width() // 2, 380))

    pygame.display.update()

    return (botao_play_game, botao_high_scores, menu_opcoes, botao_high_scores_voltar, botao_creditos)


def menu_game(tela, screen):
    menu_ativo = True

    tela_inicial = abre_tela_inicial(tela, screen)

    while menu_ativo:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # posição do mouse e clique do botão
        pos = pygame.mouse.get_pos()
        (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
        # if

        botao_voltar = tela_inicial[3]

        if tela_inicial[1].collidepoint(pos) & pressed1 == 1:
            screen.print_background(tela)
            tela.blit(tela_inicial[2][1],
                      (screen.dimensoes[0] / 2 - tela_inicial[2][1].get_width() // 2, 40))

            texto_botao_voltar = escreve_texto('NEW GAME', 28)

            botao_voltar = tela.blit(escreve_texto('NEW GAME', 28),
                                     (screen.dimensoes[0] / 2 - texto_botao_voltar.get_width() // 2, 540))

            imprime_highscores(tela, screen)
            pygame.display.update()

        if tela_inicial[4].collidepoint(pos) & pressed1 == 1:
            screen.print_background(tela)

            tela.blit(tela_inicial[2][3],
                      (screen.dimensoes[0] / 2 - tela_inicial[2][3].get_width() // 2, 40))

            empresa = escreve_texto('PAI GAME INC.', 28)

            botao_voltar = tela.blit(empresa,
                                     (screen.dimensoes[0] / 2 - empresa.get_width() // 2, 540))

            imprime_creditos(tela, screen)
            pygame.display.update()

        if botao_voltar.collidepoint(pos) & pressed1 == 1:
            screen.print_background(tela)
            abre_tela_inicial(tela, screen)

        if tela_inicial[0].collidepoint(pos) & pressed1 == 1:
            screen.print_background(tela)
            pygame.display.update()
            menu_ativo = False


def game_over(tela, screen, pontos):
    menu_ativo = True

    texto_botao_salvar = escreve_texto('SALVAR', 28)
    botao_salvar = tela.blit(texto_botao_salvar,
                             (screen.dimensoes[0] / 2 - texto_botao_salvar.get_width() // 2, 440))
    screen.print_background(tela)

    titulo_game_over(tela)

    texto_botao_voltar = escreve_texto('NEW GAME', 28)
    botao_voltar = tela.blit(escreve_texto('NEW GAME', 28),
                             (screen.dimensoes[0] / 2 - texto_botao_voltar.get_width() // 2, 540))

    inp = ""
    fonte_texto_nome = pygame.font.Font("assets/fonts/bitdust1.ttf", 30)

    digite_seu_nome = escreve_texto('Digite seu nome:'.upper(), 40)
    tela.blit(digite_seu_nome, (screen.dimensoes[0] / 2 - digite_seu_nome.get_width() // 2, 280))

    pygame.display.update()

    scores = False

    while menu_ativo:

        # posição do mouse e clique do botão
        pos = pygame.mouse.get_pos()
        (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                inp += event.unicode

            # if

            txt = fonte_texto_nome.render(inp, True, (WHITE))

            if inp != "" and not scores:
                tela.blit(txt, (300, 350))
                pygame.display.update()

                texto_botao_salvar = escreve_texto('SALVAR', 28)
                botao_salvar = tela.blit(texto_botao_salvar,
                                         (screen.dimensoes[0] / 2 - texto_botao_salvar.get_width() // 2, 440))

            if botao_salvar.collidepoint(pos) and (event.type == pygame.MOUSEBUTTONUP):
                highscore.grava_pontos(inp, pontos)
                screen.print_background(tela)
                scores = True
                titulo_highscores = escreve_texto("HIGH SCORES", 40)
                tela.blit(titulo_highscores,
                          (screen.dimensoes[0] / 2 - titulo_highscores.get_width() // 2, 80))
                imprime_highscores(tela, screen)

                texto_botao_voltar = escreve_texto('NEW GAME', 28)

                botao_voltar = tela.blit(escreve_texto('NEW GAME', 28),
                                         (screen.dimensoes[0] / 2 - texto_botao_voltar.get_width() // 2, 540))

                pygame.display.update()

        if botao_voltar.collidepoint(pos) & pressed1 == 1:
            testes.main()
