from classes import *
pygame.init()

# Couleurs
blanc = pygame.Color(255, 255, 255)
noir = pygame.Color(0, 0, 0)
marron = pygame.Color(175, 110, 0)

# Variables globales
gap_ver_tuyaux = 150
pos_gap = (150, 300, 450)

class Menu():
    def __init__(self, screen, largeur_screen, hauteur_screen):

        self.screen = screen
        self.largeur = largeur_screen
        self.hauteur = hauteur_screen

        self.background = pygame.image.load("../assets/img/background-day.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))

        self.tuyau_img = pygame.image.load("../assets/img/pipe-green.png").convert_alpha()
        self.tuyau_img = pygame.transform.scale(self.tuyau_img, (70, 600))

        self.sol = pygame.image.load("../assets/img/base.png").convert_alpha()
        self.sol = pygame.transform.scale(self.sol, (self.largeur, round(self.largeur / 3)))
        self.sol_pos = self.sol.get_rect(x = 0, bottom = self.hauteur)

        self.logo = pygame.image.load("../assets/img/Flappy_Logo.png").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (round(self.largeur * 0.8), round(self.hauteur * 0.2)))

        self.sprite = pygame.image.load("../assets/img/yellowbird-midflap.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (50, 35))

        self.font = pygame.font.Font("../assets/font/Jersey15-Regular.ttf", 20)
        self.texte = self.font.render("appuyez sur la barre espace pour commencer à jouer", True, marron)
        self.txt_pos = self.texte.get_rect(centerx = round(self.largeur / 2), centery = round(self.hauteur * 0.9))

    def run(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_pipes(300, 100)
        self.draw_pipes(450, 400)
        self.screen.blit(self.sol, self.sol_pos)
        self.screen.blit(self.logo, (round(self.largeur * 0.1), round(self.hauteur * 0.1)))
        self.screen.blit(self.sprite, (round(self.largeur * 0.5 - 25), round(self.hauteur * 0.5 - 25)))
        self.screen.blit(self.texte, self.txt_pos)

    def draw_pipes(self, gap_pos, pos_x):
        nb1 = pygame.transform.rotate(self.tuyau_img, 180)
        nb2 = self.tuyau_img

        nb1_pos = nb1.get_rect(centerx = pos_x, bottom = gap_pos - 75)
        nb2_pos = nb2.get_rect(centerx = pos_x, top = gap_pos + 75)
        self.screen.blit(nb1, nb1_pos)
        self.screen.blit(nb2, nb2_pos)



class Game():
    def __init__(self, screen, largeur_screen, hauteur_screen):

        self.screen = screen
        self.largeur = largeur_screen
        self.hauteur = hauteur_screen

        self.background = pygame.image.load("../assets/img/background-day.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))

        self.tuyau_img = pygame.image.load("../assets/img/pipe-green.png").convert_alpha()
        self.tuyau_img = pygame.transform.scale(self.tuyau_img, (70, 600))

        self.sol = pygame.image.load("../assets/img/base.png").convert_alpha()
        self.sol = pygame.transform.scale(self.sol, (self.largeur, round(self.largeur / 3)))
        self.sol_pos = self.sol.get_rect(x=0, bottom=self.hauteur)

        self.score = 0
        self.font = pygame.font.Font("../assets/font/Jersey15-Regular.ttf", 50)

        self.player = Player(self.largeur, self.hauteur)
        all_sprites.add(self.player)

    def run(self):
        self.screen.blit(self.background, (0, 0))

        self.player.update()
        all_sprites.draw(self.screen)

        self.screen.blit(self.sol, self.sol_pos)
        self.texte = self.font.render(f"{self.score}", True, blanc)
        self.texte_pos = self.texte.get_rect(centerx=round(self.largeur / 2), centery=round(self.hauteur / 5))
        self.screen.blit(self.texte, self.texte_pos)

    def space(self):
        self.player.flap()
