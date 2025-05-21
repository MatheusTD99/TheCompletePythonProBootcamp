import art
import random
from game_data import data

# formata as contas nas variaveis
def format_acc(acc):
    name = acc['name']
    desc = acc['description']
    country = acc['country']
    return f"{name}, {desc}, from {country}"

# verifica resposta
def verify_response(response, acc_a, acc_b):
    followers_a = acc_a['follower_count']
    followers_b = acc_b['follower_count']
    if followers_a > followers_b:
        return response == "A"
    else:
        return response == "B"

# começa o jogo
def start_game():
    print(art.logo)
    score = 0
    game_continue = True
    choice1 = random.choice(data)
    choice2 = random.choice(data)
    while choice1 == choice2:
        choice2 = random.choice(data)

    while game_continue:
            print(f"Compare A: {format_acc(choice1)}")
            print(art.vs)
            print(f"Compare B: {format_acc(choice2)}")

            response = str(input(f"Who has more followers, A or B?\n")).upper()
            is_correct = verify_response(response, choice1, choice2)

            if is_correct:
                score += 1
                print(f"You're right! Current score: {score}")

                # Se A era maior, mantem A, e escolhe outro B
                if choice1['follower_count'] > choice2['follower_count']:
                    # mantém choice1
                    choice2 = random.choice(data)
                    while choice1 == choice2:
                        choice2 = random.choice(data)
                else:
                    # troca: B vira o novo A
                    choice1 = choice2
                    choice2 = random.choice(data)
                    while choice1 == choice2:
                        choice2 = random.choice(data)
            else:
                print(f"Game Over! :(\nFinal Score: {score}")
                game_continue = False


start_game()

