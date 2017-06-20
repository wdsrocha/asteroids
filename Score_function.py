#função que conta score ao longo do jogo de acordo com o tipo de colisão
import pygame

def score_counter(cgrande,cmedia,cnave,cpatrulha):
    score= 0
    if cgrande == True or cpatrulha == True:
        score+=10
    if cmedia ==True:
        score+=20
    if cnave == True:
        score+=20


    return score

def print_score(score):
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_score = pygame.font.SysFont(font, 30)
