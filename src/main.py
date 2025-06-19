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

played = False
clock = pygame.time.Clock()
running_global = True
while running_global:

    mode.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_global = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and played:
                M_game.space()

        elif pygame.mouse.get_pressed() == (1, 0, 0) and not played:
            mouse_pos = pygame.mouse.get_pos()
            if M_menu.button_pressed(mouse_pos):
                mode = M_game
                played = True
                M_game.space()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
