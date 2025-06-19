from game import *
pygame.init()

# fenêtre
largeur = 500
hauteur = 750
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Flappy bird")

# Modes
mode = Menu(screen, largeur, hauteur)

played = False
clock = pygame.time.Clock()
running_global = True
while running_global:

    if type(mode) == Game:
        if mode.player.game_over:
            all_sprites.empty()
            mode = Menu(screen, largeur, hauteur)
            played = False
            pygame.time.wait(1000)
    mode.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_global = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and played:
                mode.space()

        elif pygame.mouse.get_pressed() == (1, 0, 0) and not played:
            mouse_pos = pygame.mouse.get_pos()
            if mode.button_pressed(mouse_pos):
                mode = Game(screen, largeur, hauteur)
                played = True
                mode.space()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
