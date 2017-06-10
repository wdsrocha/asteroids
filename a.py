from pygame.math import Vector2 as Vector
import personagens

VELOCIDADE_MAXIMA = 2


def aplica_forca(corpo, forca):
    corpo['aceleracao'] = forca / corpo['massa']
    return corpo


def limita_vetor(u, lim):
    if Vector.length(u) > lim ** 2:
        u = Vector.normalize(u) * lim
    return u


def atualiza(corpo):
    corpo['velocidade'] += corpo['aceleracao']
    corpo['velocidade'] = limita_vetor(corpo['velocidade'], VELOCIDADE_MAXIMA)

    if corpo['posicao'][0] > 800:
        corpo['posicao'][0] = 0
    if corpo['posicao'][0] < 0:
        corpo['posicao'][0] = 800

    if corpo['posicao'][1] > 400:
        corpo['posicao'][1] = 0
    if corpo['posicao'][1] < 0:
        corpo['posicao'][1] = 400

    corpo['posicao'] += corpo['velocidade']

    corpo['aceleracao'] = 0
    return corpo


def cria_corpo():
    '''Retorna um dicionário com as características de um corpo
    físico'''
    corpo = {}
    corpo['velocidade'] = Vector()
    corpo['aceleracao'] = Vector()
    corpo['posicao'] = Vector(400, 200)
    corpo['massa'] = 1
    corpo['angulo'] = 0
    return corpo


if __name__ == '__main__':
    import pygame, fisica, math

    pygame.init()
    w = 800
    h = 400
    tela = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ROTACAO = 90
    # nave_surface = pygame.image.load('./assets/images/jogador.png')

    nave_surface = personagens.cria_nave(tela, (400, 200))

    nave_surface = pygame.transform.rotozoom(nave_surface, -90, 1)
    nave = fisica.cria_corpo()

    nave_pos = Vector(200, 150)
    nave_speed = 1000
    nave_rotation = 0
    nave_rotation_speed = 10000  # Graus por segundo

    while 1:

        background = pygame.image.load('./assets/images/space.jpg').convert()
        tela.blit(background, (0, 0))

        clock.tick(60)

        forca = Vector(0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        rotation_direction = 0.

        if keys[pygame.K_LEFT]:
            rotation_direction = +1.0
        if keys[pygame.K_RIGHT]:
            rotation_direction = -1.0

        if keys[pygame.K_UP]:
            teta = math.radians(nave_rotation)
            x = math.cos(teta)
            y = math.sin(teta)
            forca += Vector(x, -y)

        rotated_sprit = pygame.transform.rotate(nave_surface, nave_rotation )
        w, h = rotated_sprit.get_size()

        sprite_draw_pos = Vector(nave_pos.x - w / 2, nave_pos.y - w / 2)

        time_based = clock.tick()
        time_passed_seconds = time_based / 500.0

        nave_rotation += rotation_direction * nave_rotation_speed * time_passed_seconds

        heading_x = math.sin(rotation_direction * math.pi / 180.0)
        heading_y = math.cos(rotation_direction * math.pi / 180.0)
        heading = Vector(heading_x, heading_y)

        nave_pos += heading * nave_speed * time_passed_seconds

        nave = aplica_forca(nave, forca)
        nave = atualiza(nave)
        tela.blit(rotated_sprit, nave['posicao'])
        pygame.display.update()
