# função que conta score ao longo do jogo de acordo com o tipo de colisão
import pygame


def score_counter(cgrande, cmedia, cpeq, cnave, cpatrulhagrande, cpatrulhapq):
    score = 0
    if cgrande == True:
        score += 20
    if cmedia == True:
        score += 50
    if cpeq == True:
        score += 100
    if cnave == True:
        score += 20
    if cpatrulhagrande == True:
        score += 200
    if cpatrulhapq == True:
        score += 1000

    return score


def print_score(score):
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_score = pygame.font.SysFont(font, 30)
    font_score.render("Score", score, 1, (255, 255, 255))
