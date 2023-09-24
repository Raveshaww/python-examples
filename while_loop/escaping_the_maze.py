# This is a solution for the "Maze" puzzle on Reeborg's World

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
    
while not at_goal():
    
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()