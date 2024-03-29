import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """"Класс для пришельца"""

    def __init__(self, ai_game):
        """"Задает пришельцу начальную позицию и инициализирует его"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохраняем горизонтальную позицию пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """True, если пришелец с краю экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Пришелец перемещается вправо или влево"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
