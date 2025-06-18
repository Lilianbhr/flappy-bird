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
        self.rect.centery = round(self.hauteur / 3)

        self.vitesse_vertical = 0
        self.angle = 0
        self.game_over = False

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

    def flap(self):
        self.vitesse_vertical = jump
        self.image = pygame.image.load("../assets/img/yellowbird-downflap.png").convert_alpha()
        self.angle = 0