import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def adjust_for_ace(hand):
    """Substitui 11 por 1 enquanto a soma da mão for maior que 21"""
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

def start_game():
    while True:
        start = input("Do u wanna play BlackJack? (y/n):\n").lower()
        if start == "y":
            print(art.logo)
            hand = random.choices(cards, k=2)
            computer_hand = random.choices(cards, k=2)
            adjust_for_ace(hand)
            print(f"Your card hand is: {hand}, total: {sum(hand)}")
            print(f"Computer's hand is: {computer_hand}, total: {sum(computer_hand)}")

            another_card = input("Do you want another card? (y/n):\n")
            if another_card == "y":
                new_card = random.choice(cards)
                hand.append(new_card)
                adjust_for_ace(hand)
                print(f"You drew: {new_card}")
                print(f"Your final hand: {hand}, total: {sum(hand)}")

                if sum(hand) > 21:
                    print("You went over. You lose 😭")
                    continue  # pula para próxima rodada
                elif sum(hand) == 21 and len(hand) == 2:
                    print("Blackjack! You win 😎")
                    continue
            else:
                print(f"Your final hand: {hand}, total: {sum(hand)}")

            if sum(computer_hand) < 17:
                computer_new_card = random.choice(cards)
                computer_hand.append(computer_new_card)
                adjust_for_ace(computer_hand)
                print(f"Computer drew: {computer_new_card}")
            print(f"Computer's final hand: {computer_hand}, total: {sum(computer_hand)}")

            # Comparação final
            if sum(hand) > 21:
                print("You lose 😭")
            elif sum(computer_hand) > 21 or sum(hand) > sum(computer_hand):
                print("You win 😁")
            elif sum(hand) == sum(computer_hand):
                print("It's a draw 🙃")
            else:
                print("You lose 😭")

        else:
            print("Thanks for playing! 👋")
            break

start_game()