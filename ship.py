import pygame



class Ship():
    '''User`s starship'''

    def __init__(self, ai_settings, screen):
        '''Initializes the ship and sets its starting position.'''
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images\\wingship1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Определяем позицию корабля ниже
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Рисует корабль в текущей позиции."""

        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

