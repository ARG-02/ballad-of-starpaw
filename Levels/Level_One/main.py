import os, pygame
from pygame.locals import (
    QUIT
)

from code_fragments.constants import width, height
from code_fragments.Sprites.Characters.Dog.Starpaw import Starpaw
from code_fragments.Sprites.platforms.ground import Ground
from code_fragments.functions.collision_checker import collision_checker

pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Starpaw\'s Level 1')

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
speed = 60
walking_animation_iteration = 0

starpaw = Starpaw()
ground = Ground(0, 0)
ground.rect.y = height-ground.rect.height
platform_test = Ground(width/2, 250)

platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(starpaw)
all_sprites.add(ground)
all_sprites.add(platform_test)

platforms.add(ground)
platforms.add(platform_test)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((135, 206, 250))

    # Collision check

    starpaw.right_collision, starpaw.down_collision, starpaw.up_collision, starpaw.left_collision = False, False, False, False

    collision = pygame.sprite.spritecollide(starpaw, platforms, False)

    collision_checker(collision, starpaw)

    # Update the character

    pressed_keys = pygame.key.get_pressed()
    starpaw.update(pressed_keys)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
os.system("python3 MainMenu/main.py")
