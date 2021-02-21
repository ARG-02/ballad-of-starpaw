import pygame
from pygame import RLEACCEL


class Nightsoul(pygame.sprite.Sprite):
    def __init__(self):
        super(Nightsoul, self).__init__()
        self.surf = pygame.image.load("assets/textures/characters/dogs/nightsoul/idle.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
