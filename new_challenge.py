def start_game():
    print("Welcome to the Dungeon Adventure!")
    print("You find yourself in a dark dungeon. Your goal is to find the hidden treasure.")
    first_choice()

def first_choice():
    print("\nYou are at a crossroads. Do you want to go left, right, or straight?")
    choice = input("Enter 'left', 'right', or 'straight': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    elif choice == 'straight':
        straight_path()
    else:
        print("Invalid choice. Please enter 'left', 'right', or 'straight'.")
        first_choice()

def left_path():
    print("\nYou walk down the left path and encounter a sleeping dragon!")
    print("Do you want to sneak past the dragon, go back, or take the tunnel?")
    choice = input("Enter 'sneak', 'back', or 'tunnel': ").lower()
    if choice == 'sneak':
        print("\nYou successfully sneak past the dragon and continue on to find the treasure!")
    elif choice == 'back':
        first_choice()
    elif choice == 'tunnel':
        tunnel_path()
    else:
        print("Invalid choice. Please enter 'sneak', 'back', or 'tunnel'.")
        left_path()

def right_path():
    print("\nYou walk down the right path and find a basketball.")
    print("Do you want to take the basketball with you, leave it, or investigate the sound?")
    choice = input("Enter 'take', 'leave', or 'sound': ").lower()
    if choice == 'take':
        print("\nYou take the basketball with you.")
        basketball_scenario(True)
    elif choice == 'leave':
        print("\nYou leave the basketball and continue down the path.")
        basketball_scenario(False)
    elif choice == 'sound':
        sound_path()
    else:
        print("Invalid choice. Please enter 'take', 'leave', or 'sound'.")
        right_path()

def straight_path():
    print("\nYou walk straight ahead and find a mysterious door.")
    print("Do you want to open the door or go back?")
    choice = input("Enter 'open' or 'back': ").lower()
    if choice == 'open':
        door_path()
    elif choice == 'back':
        first_choice()
    else:
        print("Invalid choice. Please enter 'open' or 'back'.")
        straight_path()

def tunnel_path():
    print("\nYou crawl through the tunnel and find a hidden chamber with the treasure!")
    print("Congratulations, you win!")
    play_again()

def sound_path():
    print("\nYou investigate the sound and find a friendly dog that leads you to the treasure!")
    print("Congratulations, you win!")
    play_again()

def door_path():
    print("\nYou open the door and find a room filled with gold!")
    print("Congratulations, you win!")
    play_again()

def basketball_scenario(has_basketball):
    print("\nYou encounter an angry rabbit!")
    if has_basketball:
        print("Do you want to throw the basketball at the rabbit, run away, or try to pet it?")
        choice = input("Enter 'throw', 'run', or 'pet': ").lower()
        if choice == 'throw':
            print("\nYou throw the basketball at the rabbit, and it runs away. You continue your journey and find the treasure! You win!")
        elif choice == 'run':
            print("\nYou run away from the rabbit but get lost in the woods. Game over.")
        elif choice == 'pet':
            print("\nYou pet the rabbit and it becomes your friend, guiding you to the treasure. You win!")
        else:
            print("Invalid choice. Please enter 'throw', 'run', or 'pet'.")
            basketball_scenario(has_basketball)
    else:
        print("Do you want to run away from the rabbit or try to pet it?")
        choice = input("Enter 'run' or 'pet': ").lower()
        if choice == 'run':
            print("\nYou run away from the rabbit but get lost in the woods. Game over.")
        elif choice == 'pet':
            print("\nYou pet the rabbit and it becomes your friend, guiding you to the treasure. You win!")
        else:
            print("Invalid choice. Please enter 'run' or 'pet'.")
            basketball_scenario(False)
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