import pygame
pygame.init()

# fenêtre
largeur = 500
hauteur = 750
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Flappy bird")

# couleurs
blanc = pygame.Color(255, 255, 255)
rouge = pygame.Color(255, 255, 255)

running_global = True
while running_global:
    screen.fill(blanc)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_global = False

    pygame.display.flip()

pygame.quit()
