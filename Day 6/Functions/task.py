def my_function():
    print("Hello")
    print("Bye")


my_function()

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# def jump():
#    turn_left()
#    while wall_on_right():
#        move()
#    turn_right()
#    move()
#    turn_right()
#    while front_is_clear():
#        move()
#    turn_left()