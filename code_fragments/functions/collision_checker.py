def collision_checker(collision, character):
    if collision:
        for platform in collision:

            # Down Collision
            if character.rect.bottom >= platform.rect.top:
                character.down_collision = True
                character.rect.bottom = platform.rect.top

            # Top Collision
            if character.rect.top <= platform.rect.bottom:
                character.up_collision = True
                character.rect.top = platform.rect.bottom

            # Right Collision
            if character.rect.right >= platform.rect.left:
                character.right_collision = True
                character.rect.right = platform.rect.left

            # Left Collision
            if character.rect.left <= platform.rect.right:
                character.left_collision = True
                character.rect.left = platform.rect.right
