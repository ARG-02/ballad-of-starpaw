import os

width = 1280
height = 720

gravity = 5
vertical_velocity = -50

starpaw_walking_list = [name for name in os.listdir('assets/textures/characters/dogs/starpaw/walking') if os.path.isfile(os.path.join('assets/textures/characters/dogs/starpaw/walking', name))]
