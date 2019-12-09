# biblioteca de efeitos sonoros

import pygame

pygame.init()


def tiro_nave():
    pygame.mixer.music.load("assets/sounds/fire.wav")
    pygame.mixer.music.play()


def turbina_nave():
    pygame.mixer.music.load("assets/sounds/thrust.wav")
    pygame.mixer.music.play()


def tiro_patrulha_grande():
    pygame.mixer.music.load("assets/sounds/saucerBig.wav")
    pygame.mixer.music.play()


def tiro_patrulha_pequena():
    pygame.mixer.music.load("assets/sounds/saucerSmall.wav")
    pygame.mixer.music.play()


def explosao_asteroide_grande():
    pygame.mixer.music.load("assets/sounds/bangLarge.wav")
    pygame.mixer.music.play()


def explosao_asteroide_medio():
    pygame.mixer.music.load("assets/sounds/bangmedium.wav")
    pygame.mixer.music.play()


def explosao_asteroide_pequeno():
    pygame.mixer.music.load("assets/sounds/bangSmall.wav")
    pygame.mixer.music.play()


def fundo_musical(numero):
    pygame.mixer.music.load("assets/sounds/beat" + str(numero) + ".wav")
    pygame.mixer.music.play()
