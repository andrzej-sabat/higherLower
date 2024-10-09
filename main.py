import random
from game_data import data
from art import logo, vs

def check_guess(answer,a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return answer == 'a'
    else:
        return answer == 'b'

print(logo)

def game():
    score = 0
    choiceA = random.choice(data)
    choiceB = random.choice(data)

    while True:
        choiceA = choiceB
        choiceB = random.choice(data)

        while choiceA == choiceB:
            choiceB = random.choice(data)

        print(f"Compare A:   {choiceA['name']}, a   {choiceA['description']}, from  {choiceA['country']}")
        print(vs)
        print(f"Against B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = choiceA['follower_count']
        b_follower_count = choiceB['follower_count']

        is_correct = check_guess(answer,a_follower_count,b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break
game()




