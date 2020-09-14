import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Making ship`s weapon class'''
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images\\kisspng.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.rect)
        self.screen.blit(self.image, self.rect)
