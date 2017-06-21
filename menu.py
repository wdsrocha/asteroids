import pygame

WHITE = (255, 255, 255)

# menu

def titulo_jogo(tela):
    menu_fonte_titulo = pygame.font.Font("assets/fonts/bitdust1.ttf", 100)
    menu_titulo = menu_fonte_titulo.render("ASTEROIDS", True, (WHITE))
    menu_titulo = tela.blit(menu_titulo, (400 - menu_titulo.get_width() // 2, 150 - menu_titulo.get_height() // 2))
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

def score():
    menu_fonte_creditos = pygame.font.Font("assets/fonts/bitdust1.ttf", 13)
    menu_creditos = menu_fonte_creditos.render("Pai Games Inc", True, (WHITE))



def menu_game(tela,screen):
    menu_ativo = True

    menu_titulo = titulo_jogo(tela)
    menu_opcoes = menu(tela)

    botao_play_game = tela.blit(menu_opcoes[0], (screen.dimensoes[0] / 2 - menu_opcoes[0].get_width() // 2, 300))
    botao_high_scores = tela.blit(menu_opcoes[1], (screen.dimensoes[0] / 2 - menu_opcoes[1].get_width() // 2, 340))

    # highscores = highscore.ver_highscore()
    # print(highscores)

    pygame.display.update()

    while menu_ativo:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # posição do mouse e clique do botão
        pos = pygame.mouse.get_pos()
        (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
        # if
        if botao_play_game.collidepoint(pos) & pressed1 == 1:
            screen.print_background(tela)
            pygame.display.update()
            menu_ativo = False
