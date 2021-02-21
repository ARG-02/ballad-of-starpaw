# Check to see if the position is inside the 2 corners

def position_in_tuple(position, top_left, bottom_right_add):
    if top_left[0] < position[0] < bottom_right_add[0]+top_left[0]:
        if top_left[1] < position[1] < bottom_right_add[1]+top_left[1]:
            return True

    return False
