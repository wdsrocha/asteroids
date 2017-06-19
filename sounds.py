# biblioteca de efeitos sonoros

import  pygame

def tiro_nave():
    pygame.mixer.music.load('assets/sounds/fire.wav')
    # pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

def turbina_nave():
    pygame.mixer.music.load('assets/sounds/thrust.wav')
    # pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()