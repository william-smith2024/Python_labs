def start_game():
    print("Welcome to the Dungeon Adventure!")
    print("You find yourself in a dark dungeon. Your goal is to find the hidden treasure.")
    first_choice()
def first_choice():
    print("\nYou are at a crossroads. Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        first_choice()
def left_path():
    print("\nYou walk down the left path and encounter a sleeping dragon!")
    print("Do you want to sneak past the dragon or go back?")
    choice = input("Enter 'sneak' or 'back': ").lower()
    if choice == 'sneak':
        print("\nYou successfully sneak past the dragon and find the treasure! You win!")
    elif choice == 'back':
        first_choice()
    else:
        print("Invalid choice. Please enter 'sneak' or 'back'.")
        left_path()
def right_path():
    print("\nYou walk down the right path and fall into a trap! Game over.")
    play_again()
def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()
# Start the game
start_game()