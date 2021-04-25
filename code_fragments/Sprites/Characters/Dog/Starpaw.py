import pygame
from pygame.locals import (
    K_UP, K_w,
    K_LEFT, K_a,
    K_RIGHT, K_d
)

from code_fragments.constants import width, height, horizontal_acceleration, horizontal_friction, vec, gravity


class Starpaw(pygame.sprite.Sprite):
    def __init__(self, platforms):
        super(Starpaw, self).__init__()
        self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/idle.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.platforms = platforms

        self.pos = vec(width/2, height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        keys = pygame.key.get_pressed()

        self.acc = vec(0, gravity)

        if keys[K_LEFT] or keys[K_a]:
            self.acc.x = -horizontal_acceleration

        if keys[K_RIGHT] or keys[K_d]:
            self.acc.x = horizontal_acceleration

        self.acc.x += self.vel.x * horizontal_friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
