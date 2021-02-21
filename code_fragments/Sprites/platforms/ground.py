import pygame
from pygame.locals import (
    RLEACCEL
)

from code_fragments.constants import height


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Ground, self).__init__()
        self.surf = pygame.image.load("assets/textures/Levels/Platforms/Ground.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
