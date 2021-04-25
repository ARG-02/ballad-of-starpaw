import os, pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_SPACE
)

from code_fragments.constants import width, height
from code_fragments.Sprites.Characters.Dog.Starpaw import Starpaw
from code_fragments.Sprites.platforms.platform import Platform
from code_fragments.functions.collision_checker import collision_checker

pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Starpaw\'s Level 1')

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
speed = 60
walking_animation_iteration = 0

platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

starpaw = Starpaw(platforms)

platforms_list = [(0, height-150, "assets/textures/Levels/Platforms/Ground.png"),
                  (width/2, height/2-200, "assets/textures/Levels/Platforms/Ground.png")]

for platform in platforms_list:
    p = Platform(*platform)
    all_sprites.add(p)
    platforms.add(p)

all_sprites.add(starpaw)

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                starpaw.jump()

    # Update Starpaw
    all_sprites.update()

    # Collision checking
    if starpaw.vel.y > 0:
        hits = pygame.sprite.spritecollide(starpaw, platforms, False)
        if hits:
            starpaw.pos.y = hits[0].rect.top
            starpaw.vel.y = 0

    if starpaw.rect.centerx >= 3 * width / 4:
        starpaw.pos.x += starpaw.vel.x
        for plat in platforms:
            plat.rect.x += starpaw.vel.y


    # Blitting and setting drawings
    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    screen.blit(starpaw.surf, starpaw.rect)

    # Flip the display
    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
os.system("python3 MainMenu/main.py")
