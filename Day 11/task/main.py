import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    while True:  # Loop para continuar o jogo
        start = input("Do u wanna play BlackJack? (y/n):\n").lower()
        if start == "y":
            print(art.logo)
            hand = random.choices(cards, k=2)
            computer_hand = random.choices(cards, k=2)
            print(f"Your card hand is: {hand}, total: {sum(hand)}")
            print(f"Computer's hand is: {computer_hand}, total: {sum(computer_hand)}")

            # Perguntar se o jogador quer mais cartas
            another_card = input("Do you want another card? (y/n):\n")
            if another_card == "y":
                new_card = random.choice(cards)
                hand.append(new_card)
                print(f"You drew: {new_card}")
                print(f"Your final hand: {hand}, total: {sum(hand)}")

                if sum(hand) > 21:
                    print("You went over. You lose 😭")
                else:
                    if sum(hand) > sum(computer_hand):
                        print("You win 😁")
                    elif sum(hand) == sum(computer_hand):
                        print("It's a draw 🙃")
                    else:
                        print("You lose 😭")
            else:
                print(f"Your final hand: {hand}, total: {sum(hand)}")

            # Agora o computador decide se vai pegar outra carta
            if sum(computer_hand) < 17:
                computer_new_card = random.choice(cards)
                computer_hand.append(computer_new_card)
                print(f"Computer drew: {computer_new_card}")
                print(f"Computer's final hand: {computer_hand}, total: {sum(computer_hand)}")
            else:
                print(f"Computer stands with: {computer_hand}, total: {sum(computer_hand)}")

            # Comparar quem ganhou
            if sum(hand) > 21:
                print("You lose 😭")
            elif sum(hand) > sum(computer_hand):
                print("You win 😁")
            elif sum(hand) == sum(computer_hand):
                print("It's a draw 🙃")
            else:
                print("You lose 😭")

        else:
            print("Thanks for playing! 👋")
            break  # Sai do loop e termina o jogo


start_game()
