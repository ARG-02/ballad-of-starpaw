import pygame
from pygame.locals import (
    K_UP, K_w,
    K_LEFT, K_a,
    K_RIGHT, K_d
)

from code_fragments.constants import width, height, gravity, vertical_velocity, starpaw_walking_list


class Starpaw(pygame.sprite.Sprite):
    def __init__(self):
        super(Starpaw, self).__init__()
        self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/idle.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.up_collision = False
        self.left_collision = False
        self.right_collision = False
        self.down_collision = False
        self.is_left = False
        self.walking_animation_iteration = 0

        self.vertical_velocity = vertical_velocity

    def update(self, keys):
        pass

        # global vertical_velocity
        #
        # if (keys[K_LEFT] or keys[K_a]) and not self.left_collision:
        #     self.is_left = True
        #
        #     self.rect.move_ip(-5, 0)
        #
        #     if self.down_collision:
        #         self.surf = pygame.image.load(f"assets/textures/characters/dogs/starpaw/walking/frame_{self.walking_animation_iteration+1}.png").convert()
        #         self.walking_animation_iteration = self.walking_animation_iteration + 1 if self.walking_animation_iteration+2 < len(starpaw_walking_list) else 0
        #
        #     if self.rect.left < 0:
        #         self.rect.left = 0
        #         self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/idle.png")
        #
        # if (keys[K_RIGHT] or keys[K_d]) and not self.right_collision:
        #     self.is_left = False
        #
        #     self.rect.move_ip(5, 0)
        #
        #     if self.down_collision:
        #         self.surf = pygame.image.load(f"assets/textures/characters/dogs/starpaw/walking/frame_{self.walking_animation_iteration+1}.png").convert()
        #         self.walking_animation_iteration = self.walking_animation_iteration + 1 if self.walking_animation_iteration+2 < len(starpaw_walking_list) else 0
        #
        #     if self.rect.right > width:
        #         self.rect.right = width
        #         self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/idle.png")
        #
        # if self.right_collision:
        #     self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/idle.png")
        #
        # if self.left_collision:
        #     self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/idle.png")
        #
        # if (keys[K_UP] or keys[K_w]) and self.down_collision:
        #     self.vertical_velocity = vertical_velocity
        #     self.rect.move_ip(0, self.vertical_velocity)
        #
        # elif self.down_collision:
        #     self.vertical_velocity = 0
        #
        # if self.up_collision:
        #     self.vertical_velocity = -vertical_velocity
        #
        # if not self.down_collision:
        #     self.rect.move_ip(0, self.vertical_velocity)
        #
        #     self.vertical_velocity += gravity
        #
        #     if vertical_velocity > 0:
        #         self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/jumping.png")
        #
        #     elif vertical_velocity <= 0:
        #         self.surf = pygame.image.load("assets/textures/characters/dogs/starpaw/falling.png")
        #
        #     if self.rect.top <= 0:
        #         self.rect.top = 0
        #
        # if self.is_left:
        #     self.surf = pygame.transform.flip(self.surf, True, False)
        #
        # self.surf.set_colorkey((0, 0, 0))
