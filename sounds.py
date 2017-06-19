# biblioteca de efeitos sonoros

import pygame


def tiro_nave():
    pygame.mixer.music.load('assets/sounds/fire.wav')
    pygame.mixer.music.play()

def turbina_nave():
    pygame.mixer.music.load('assets/sounds/thrust.wav')
    pygame.mixer.music.play()

def tiro_patrulha_grande():
    pygame.mixer.music.load('assets/sounds/saucerBig.wav')
    pygame.mixer.music.play()

def tiro_patrulha_pequena():
    pygame.mixer.music.load('assets/sounds/saucerSmall.wav')
    pygame.mixer.music.play()

def explosao_asteroide_grande():
    pygame.mixer.music.load('assets/sounds/bangLarge.wav')
    pygame.mixer.music.play()

def explosao_asteroide_medio():
    pygame.mixer.music.load('assets/sounds/bangmedium.wav')
    pygame.mixer.music.play()

def explosao_asteroide_pequeno():
    pygame.mixer.music.load('assets/sounds/bangSmall.wav')
    pygame.mixer.music.play()

def tiro_patrulha_grande():
    pygame.mixer.music.load('assets/sounds/saucerBig.wav')
    pygame.mixer.music.play()


def tiro_patrulha_grande():
    pygame.mixer.music.load('assets/sounds/saucerBig.wav')
    pygame.mixer.music.play()


def fundo_musical():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.mixer.music.load('assets/sounds/beat.wav')
    pygame.mixer.music.play(-1)