import pygame
from game import *
pygame.init()

# fenêtre
largeur = 500
hauteur = 750
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Flappy bird")

# Modes
M_menu = Menu(screen, largeur, hauteur)

clock = pygame.time.Clock()
running_global = True
while running_global:

    M_menu.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_global = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
