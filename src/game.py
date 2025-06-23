import pygame.image

from classes import *
from random import choice
pygame.init()

# Couleurs
blanc = pygame.Color(255, 255, 255)
noir = pygame.Color(0, 0, 0)

# Variables globales
gap = 150
pos_gap = (200, 300, 400)
meilleur_score = 0
count = 0
count_bis = 0
menu = True
speed = 5

def add_pipes(pos_vertical_du_trou, largeur_screen, taille_gap, speed):
    global count
    pipe = Pipes(pos_vertical_du_trou, largeur_screen, 0, taille_gap, speed)
    if menu :
        pipe.rect.centerx = largeur_screen/ 5 * 4
    all_sprites.add(pipe)
    pipe = Pipes(pos_vertical_du_trou, largeur_screen, 180, taille_gap, speed)
    if menu :
        pipe.rect.centerx = largeur_screen / 5 * 4
    all_sprites.add(pipe)
    count = pipe.rect.x

class Menu():
    def __init__(self, screen, largeur_screen, hauteur_screen):
        global speed
        global menu
        global count_bis
        global  count
        menu = True

        self.screen = screen
        self.largeur = largeur_screen
        self.hauteur = hauteur_screen

        self.background = pygame.image.load("../assets/img/background-day.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))

        self.sol = pygame.image.load("../assets/img/base.png").convert_alpha()
        self.sol = pygame.transform.scale(self.sol, (self.largeur, round(self.largeur / 3)))
        self.sol_pos = self.sol.get_rect(x = 0, bottom = self.hauteur)

        self.logo = pygame.image.load("../assets/img/Flappy_Logo.png").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (round(self.largeur * 0.8), round(self.hauteur * 0.2)))

        self.sprite = pygame.image.load("../assets/img/yellowbird-midflap.png").convert_alpha()
        self.sprite_rect = self.sprite.get_rect(centerx=round(self.largeur/3), centery=round(self.hauteur/2))

        self.button = pygame.image.load("../assets/img/bouton-play.png").convert_alpha()
        self.button = pygame.transform.scale(self.button, (190, 75))
        self.button_rect = self.button.get_rect(centerx=round( self.largeur / 2), centery = round(self.hauteur * 0.9))

        self.best_score_img = pygame.image.load("../assets/img/feu.png").convert_alpha()
        self.best_score_img = pygame.transform.scale(self.best_score_img, (70, 70))
        self.best_score_pos = self.best_score_img.get_rect(centerx=round(self.largeur/2), top=round(self.hauteur/3))
        self.font = pygame.font.Font("../assets/font/Jersey15-Regular.ttf", 50)
        self.texte = self.font.render(f"{meilleur_score}", True, blanc)
        self.texte_pos = self.texte.get_rect(centerx=self.best_score_pos.centerx, bottom=self.best_score_pos.bottom+5)

        add_pipes(self.hauteur/2, self.largeur, gap, speed)
        count_bis = count + 70

    def run(self):
        self.screen.blit(self.background, (0, 0))
        all_sprites.draw(self.screen)
        self.screen.blit(self.sol, self.sol_pos)
        self.screen.blit(self.logo, (round(self.largeur * 0.1), round(self.hauteur * 0.1)))
        self.screen.blit(self.sprite, self.sprite_rect)
        self.screen.blit(self.button, self.button_rect)
        self.screen.blit(self.best_score_img, self.best_score_pos)
        self.screen.blit(self.texte, self.texte_pos)

    def button_pressed(self, mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            return True



class Game():
    def __init__(self, screen, largeur_screen, hauteur_screen):

        global menu
        menu = False

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

        self.font = pygame.font.Font("../assets/font/Jersey15-Regular.ttf", 50)

        self.player = Player(self.largeur, self.hauteur)
        all_sprites.add(self.player)

    def run(self):
        global count
        global pos_gap
        global speed
        global count_bis
        global meilleur_score

        self.screen.blit(self.background, (0, 0))

        count -= speed
        count_bis -= speed

        if count <= self.player.rect.right:
            pos = choice(pos_gap)
            add_pipes(pos, self.largeur, gap, speed)
        all_sprites.update()
        all_sprites.draw(self.screen)

        if count_bis <= self.player.rect.x :
            self.player.score += 1
            count_bis = count + 70

        self.screen.blit(self.sol, self.sol_pos)
        self.texte = self.font.render(f"{self.player.score}", True, blanc)
        self.texte_pos = self.texte.get_rect(centerx=round(self.largeur / 2), centery=round(self.hauteur / 5))
        self.screen.blit(self.texte, self.texte_pos)

        if self.player.score > meilleur_score :
            meilleur_score = self.player.score

    def space(self):
        self.player.flap()


class Game_over():
    def __init__(self, screen, largeur, hauteur, score):
        self.screen = screen
        self.largeur = largeur
        self.hauteur = hauteur
        self.score = score

        self.image = pygame.image.load("../assets/img/game-over.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 130))
        self.img_pos = self.image.get_rect(centerx=round(self.largeur/2), centery=round(self.hauteur/3))

        self.font = pygame.font.Font("../assets/font/Jersey15-Regular.ttf", 100)
        self.texte = self.font.render(f"{self.score}", True, blanc)
        self.txt_pos = self.texte.get_rect(centerx=round(self.largeur/2), centery=round(self.hauteur*2/3))

    def run(self):
        self.screen.fill(noir)
        self.screen.blit(self.image, self.img_pos)
        self.screen.blit(self.texte, self.txt_pos)
        pygame.display.flip()
        pygame.time.wait(3000)
