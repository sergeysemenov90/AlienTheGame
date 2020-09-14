import pygame
from pygame.sprite import Sprite


class Settings():
    '''Main class with game settings'''

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Bullet_settings
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 8
        # fleet_direction = 1 movement to the right; -1 - movement to the left.
        self.fleet_direction = 1

