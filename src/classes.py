import pygame
pygame.init()

all_sprites = pygame.sprite.Group()
gravity = 0.8
jump = -10

class Player(pygame.sprite.Sprite):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

        self.image = pygame.image.load("../assets/img/yellowbird-midflap.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(self.largeur / 3)
        self.rect.centery = round(self.hauteur / 2)

        self.vitesse_vertical = 0
        self.angle = 0
        self.game_over = False
        self.score = 0

    def update(self):
        self.vitesse_vertical += gravity
        self.rect.y += self.vitesse_vertical

        if -1 < self.vitesse_vertical < 1 :
            self.image = pygame.image.load("../assets/img/yellowbird-midflap.png").convert_alpha()

        elif self.vitesse_vertical >= 1 :
            self.image = pygame.image.load("../assets/img/yellowbird-upflap.png").convert_alpha()
            self.angle -= 1
            if self.angle < -30 :
                self.angle = -30
            self.image = pygame.transform.rotate(self.image, self.angle)

        if self.rect.y < 0 :
            self.rect.y = 0
            self.vitesse_vertical = 0

        elif self.rect.y + 30 > round(self.hauteur - (self.largeur / 3)):
            self.flap()

        for elt in pygame.sprite.spritecollide(self, all_sprites, False):
            if type(elt) == Pipes :
                self.game_over = True

    def flap(self):
        self.vitesse_vertical = jump
        self.image = pygame.image.load("../assets/img/yellowbird-downflap.png").convert_alpha()
        self.angle = 0


class Pipes(pygame.sprite.Sprite):
    def __init__(self, pos_vertical_du_trou, largeur_screen, angle, taille_gap, speed):
        super().__init__()
        self.trou = pos_vertical_du_trou
        self.largeur = largeur_screen
        self.demi_gap = taille_gap/2

        self.image = pygame.image.load("../assets/img/pipe-green.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 600))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(x=self.largeur)
        if angle == 0:
            self.rect.top = self.trou+self.demi_gap
        elif angle == 180:
            self.rect.bottom = self.trou-self.demi_gap

        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right <= 0:
            self.kill()
