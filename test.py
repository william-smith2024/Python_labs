import random

# The game will prompt the user to guess a number between 1 and 10, providing feedback on whether the guess is too high, too low, or correct. Use random. "import random"

# Generate a random number between 1 and 10

randomnumber = random.randint(1, 10)
print(randomnumber)
while randomnumber  > 0:
    if randomnumber % 10 == 0:
        print(randomnumber)
    else:
        print(randomnumber)


