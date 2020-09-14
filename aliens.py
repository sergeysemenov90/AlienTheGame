import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''Opponent`s class'''

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images\\spaceship.png')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # print(screen_rect.right)
        # print(self.rect.right)
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''Alien position changing'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)

