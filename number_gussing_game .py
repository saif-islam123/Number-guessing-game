
import random
from number_gussing_art import logo

print(logo)

def begin():
    """Prints the welcome message and the range of numbers."""
    print("Welcome to the Number Gussing Game! ")
    print("I am thinking of a number between 1 and 100.")

def check_guess(secret_number):
    try:
        guess = int(input("Make a guess: "))
        if guess == secret_number:
            print(f"You got it,the answer was {secret_number}.")
            return True
        elif guess > secret_number:
            print("Too High")
            print("Guess again.")
        elif guess < secret_number:
            print("Too Low")
            print("Guess again")
    except ValueError:
         print("Invalid Input.")
    return False

def play_game():
    """Starts and manages the number guessing game."""
    begin()
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
    secret_number = random.randint(1, 100) 
    if difficulty.lower() == 'hard':
        attempts = 5
        print("You have 5 attempts remaning to guess the number.") 
    elif difficulty.lower() == 'easy':
        attempts = 10
        print("You have 10 attempts remaning to guess the number.") 
    for attempt_number in range(attempts):
        if check_guess(secret_number):
            break
    else:
            print(f"You have run out of guesses,the number was {secret_number}.")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()

# Start the game
play_game()



















