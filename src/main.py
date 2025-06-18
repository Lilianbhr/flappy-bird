from game import *
pygame.init()

# fenêtre
largeur = 500
hauteur = 750
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Flappy bird")

# Modes
M_menu = Menu(screen, largeur, hauteur)
M_game = Game(screen, largeur, hauteur)
mode = M_menu

clock = pygame.time.Clock()
running_global = True
while running_global:

    mode.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_global = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                mode = M_game

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
