enemies = 1


def increase_enemies():
    '''Using global variables inside function(def/define)'''
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")