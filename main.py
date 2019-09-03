from random import *
import os

def enemy_score_gen():
    enemy_score = randint(1,21)
    return enemy_score

def random_card_picker():
    card_value = randint(1, 11)
    return card_value

def game_starting():
    global decision
    print("Hello in blackjack! Your goal in blackjack is to get higher score then computer and don't pass 21 points. Do you want to draw a card")
    print("1. Yes!")
    print("2. No")
    decision = input()

card = 0
crossing_point = False

game_starting()
if decision == "1":
    os.system("cls")
    while True:
        print(f"Your score is {card}")
        print("Do you want to draw a card?")
        print("1. Yes!")
        print("2. No")
        in_game_decision = input()
        if in_game_decision == "1":
            os.system("cls")
            card = card + random_card_picker()
        else:
            break
        
        if card > 21:
            print(f"Your points: {card}")
            print("You accrosed 21 point. You lost!")
            crossing_point = True
            break
              
    #Resultats
    if crossing_point == False:
        if card > enemy_score_gen():
            print(f"Your score: {card}")
            print(f"Enemy score: {enemy_score_gen()}")
            print("You won congratulation!")

        elif enemy_score_gen() > card:
            print(f"Your score: {card}")
            print(f"Enemy score: {enemy_score_gen()}")
            print("You lost. Try again!")

        elif enemy_score_gen() == card:
            print(f"Your score: {card}")
            print(f"Enemy score: {enemy_score_gen()}")
            print("Tie! Try again!")
    else:
        exit
    


elif decision == "2":
    exit
