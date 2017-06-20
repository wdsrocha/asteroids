  #Python 3.4.3 with Pygame
import pygame

pygame.init()
pygame.display.set_caption('Crash!')
window = pygame.display.set_mode((300, 300))
running = True

#Draw Once
Rectplace = pygame.draw.rect(window, (255, 0, 0),(100, 100, 100, 100))
pygame.display.update()
#Main Loop
while running:
#mouse position and button clicking
    pos = pygame.mouse.get_pos()
    (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
#if statement
    if Rectplace.collidepoint(pos)& pressed1==1:
        print("You have opened a chest!")
#Quit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False