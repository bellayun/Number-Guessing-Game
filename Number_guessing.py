# "Welcome to the Number Guessing Game!"
# "I'm thinking of a number between 1 and 100"
# "Choose a difficulty. Type 'easy' or 'hard': "
# "You have x attempts remaining to guess the number"
# "Make a guess: "

import random
gold_num = random.randint(1,100)
# ask user which difficulty they want in this game
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def difficulty_game(difficulty):
    if difficulty == 'easy':
        attempts = 10
    if difficulty == 'hard':
        attempts = 5
    return attempts
attempts = difficulty_game(difficulty)

while attempts > 0:
    print(f"You have {attempts} attemps remaining to guess the number.")

    # ask user to guess, and every time they guess, compare the number with the number in mind to tell them if they need to go higher or lower.
    guess = int(input("guess the integer number between 0 and 100: "))

    # until the attemps run out, or until the user guess it right, repeatedly ask the user to guess.
    if guess < gold_num:
        print("Go higher!")
    if guess > gold_num:
        print("Go lower!")
    if guess == gold_num:
        print("You guessed it right!")
        break
    print("Guess again.")
    attempts -= 1



########## instructor's code ##########
from random import randint  
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's giess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns reamining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choosing a random number between 1 and 100
    print("Welsome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"Psst, the correct answer is {answer}")


    turns = set_difficulty()
    
    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:   
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Have a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess !=answer:
            print("Guess again!")
    
        
    
game()
