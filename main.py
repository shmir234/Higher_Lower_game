from game_data import data
from art import logo
from art import vs
import random


def get_A(data):
    number = random.randint(0,49)
    name_a = data[number]['name']
    description_a = data[number]['description']
    country_a = data[number]['country']
    target_a = data[number]['follower_count']
    return name_a, description_a, country_a, target_a

def get_B(data):
    number = random.randint(0,49)
    name_b = data[number]['name']
    description_b = data[number]['description']
    country_b = data[number]['country']
    target_b = data[number]['follower_count']
    return name_b, description_b, country_b, target_b

def check(target_A, target_B, user_guess, current_score):
    if target_A > target_B and user_guess == 'A':
        print(f"You're right! Current score")
        counter = 1
        return counter
    elif target_A < target_B and user_guess == 'A':
        print(f"Sorry, that's wrong. Final score: {current_score}")
    elif target_B < target_A and user_guess == 'B':
        print(f"Sorry, that's wrong. Final score: {current_score}")
    elif target_B > target_A and user_guess == 'B':
        print(f"You're right! Current score")



name_A, description_A, country_A, target_A = get_A(data)
name_B, description_B, country_B, target_B = get_A(data)
current_score = 0
print(logo)

should_continue = True

while should_continue:
    print(f"Compare A: {name_A}, a {description_A}, from {country_A}.")
    print(vs)
    print(f"Compare B: {name_B}, a {description_B}, from {country_B}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    if target_A > target_B and user_guess == 'A':
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        name_A, description_A, country_A, target_A = name_B, description_B, country_B, target_B
        name_B, description_B, country_B, target_B = get_A(data)
    elif target_A < target_B and user_guess == 'A':
        print(f"Sorry, that's wrong. Final score: {current_score}")
        should_continue = False
    elif target_B < target_A and user_guess == 'B':
        print(f"Sorry, that's wrong. Final score: {current_score}")
        should_continue = False
    elif target_B > target_A and user_guess == 'B':
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        name_A, description_A, country_A, target_A = name_B, description_B, country_B, target_B
        name_B, description_B, country_B, target_B = get_A(data)


