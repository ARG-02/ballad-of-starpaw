import pygame
from pygame.locals import (
    RLEACCEL
)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Platform, self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
