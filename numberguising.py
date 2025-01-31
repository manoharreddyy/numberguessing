import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Number of attempts
    attempts = 0
    
    while True:
        # Ask the user for their guess
        user_guess = input("Make a guess: ")
        
        # Check if the input is a valid number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        # Compare the guess to the random number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the right number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
number_guessing_game()
