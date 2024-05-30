import random

def guess_the_number():
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    guess = None

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 10.")
    
    while guess != number_to_guess:
        # Ask the user to guess the number
        guess = int(input("Please enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            
# Run the game
guess_the_number()

