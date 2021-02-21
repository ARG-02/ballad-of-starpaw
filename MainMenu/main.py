import os
import pygame

from code_fragments.functions.position_in_tuple import position_in_tuple
from code_fragments.constants import width, height

pygame.mixer.init()
pygame.init()

pygame.display.set_caption('StarPaw\'s Title Screen')
screen = pygame.display.set_mode((width, height))

# Load In Images

background = pygame.image.load("assets/textures/main_menu/background.png")
title = pygame.image.load("assets/textures/main_menu/title.png")

play_button = pygame.image.load("assets/textures/main_menu/play_button.png")
configure_cam_button = pygame.image.load("assets/textures/main_menu/configure_cam_button.png")
story_button = pygame.image.load("assets/textures/main_menu/story_button.png")
credits_button = pygame.image.load("assets/textures/main_menu/credits_button.png")
controls_button = pygame.image.load("assets/textures/main_menu/controls_button.png")

# Load In Sound(s)

pygame.mixer.music.load("assets/sounds/main_menu/background_music.mp3")

title_sound = pygame.mixer.Sound("assets/sounds/main_menu/title_sound.mp3")

# Define the widths and height for the later placed buttons

button_width = width/2-play_button.get_width()/2
initial_button_height = height/2-(play_button.get_height()/2*3)

# Play Sounds

pygame.mixer.music.play(loops=-1)

# Create the title event

TITLESTART = pygame.USEREVENT + 1
pygame.time.set_timer(TITLESTART, 1500)
title_started = False

# Game Loop

open_play = False
open_configure_cam = False
open_story = False
open_credits = False
open_controls = False

running = True
while running:
    # Test For Clicking

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            # Tells where the mouse clicked

            click_position = event.pos

            # If the user clicks the button, then this loop breaks and sets its corresponding
            # Boolean value is set to True

            if title_started and position_in_tuple(click_position, (int(button_width), int(initial_button_height + play_button.get_height())), (play_button.get_width(), play_button.get_height())):
                running = False
                open_play = True

            elif title_started and position_in_tuple(click_position, (int(button_width), int(initial_button_height + configure_cam_button.get_height() * 2+13)), (configure_cam_button.get_width(), configure_cam_button.get_height())):
                running = False
                open_configure_cam = True

            elif title_started and position_in_tuple(click_position, (int(button_width), int(initial_button_height + story_button.get_height() * 3+13*2)), (story_button.get_width(), story_button.get_height())):
                running = False
                open_story = True

            elif title_started and position_in_tuple(click_position, (int(button_width), int(initial_button_height + credits_button.get_height() * 4+13*3)), (credits_button.get_width(), credits_button.get_height())):
                running = False
                open_credits = True

            elif title_started and position_in_tuple(click_position, (int(button_width), int(initial_button_height + controls_button.get_height()* 5+13*4)), (controls_button.get_width(), controls_button.get_height())):
                running = False
                open_controls = True

        elif event.type == TITLESTART and (not title_started):
            title_started = True
            title_sound.play()

        elif event.type == pygame.QUIT:
            running = False

    # Place the images

    screen.fill((255, 255, 255))

    screen.blit(background, (0, 0))

    screen.blit(play_button, (button_width, initial_button_height + play_button.get_height()))
    screen.blit(configure_cam_button, (button_width, initial_button_height + play_button.get_height() * 2+13))
    screen.blit(story_button, (button_width, initial_button_height + play_button.get_height() * 3+13*2))
    screen.blit(credits_button, (button_width, initial_button_height + play_button.get_height() * 4+13*3))
    screen.blit(controls_button, (button_width, initial_button_height + play_button.get_height() * 5+13*4))

    # If the title is on, display it

    if title_started:
        screen.blit(title, (0, 0))

    # Flip the display

    pygame.display.flip()


# Check which button is pressed, and then the corresponding file will open

if open_play:
    pygame.quit()
    os.system("python3 Levels/Level_One/main.py")

elif open_configure_cam:
    pygame.quit()
    os.system("python3 Configure_Cam/main.py")

elif open_story:
    pygame.quit()
    os.system("python3 Story/main.py")

elif open_credits:
    pygame.quit()
    os.system("python3 Credits/main.py")

elif open_controls:
    pygame.quit()
    os.system("python3 Controls_Screen/main.py")
