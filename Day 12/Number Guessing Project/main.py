import art
import random

def start_game():
    play = input("Do u wanna play Magic Number? (y/n):\n").lower()
    if play == "y":
        difficulty = input("Magic Number is a game where u have to guess the number between 1 and 100.\nDo u wanna play in Normal Mode(10 guesses) or Hard Mode(5 guesses)? (n/h):\n" ).lower()
        if difficulty == "n":
            attempts = 10
        elif difficulty == "h":
            attempts = 5
        print("\n" * 20, *art.logo)
        magic_number = random.randint(1, 100)
        win = False
        while attempts > 0:
            guess = int(input("Take a guess:\n"))
            if guess > magic_number:
                print("Too high")
                attempts -= 1
                print(f"Attempts left: {attempts}")
            elif guess < magic_number:
                print("Too low")
                attempts -= 1
                print(f"Attempts left: {attempts}")
            elif guess == magic_number:
                win = True
                print("U WIN!!!")
                break
        print(f"The Magic Number was {magic_number}!")
    else:
        print("Okay ;(")
    new_game = input("Do u wanna play again? (y/n)")
    if new_game == "y":
        start_game()
    else:
        print("Okay ;(")
start_game()

