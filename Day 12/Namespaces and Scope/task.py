#def is_prime(num):
#    if num <= 1:
#        return False
#    for i in range(2, int(num ** 0.5) + 1):
#        if num % i == 0:
#            return False
#    return True


#print(is_prime(73))
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

