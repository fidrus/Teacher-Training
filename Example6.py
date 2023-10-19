

import random

def main():
    """Start a music guessing game."""
    print("Guess the music!")

    music = [
        "Rock",
        "Pop",
        "Jazz",
        "Dangdut",
        "Pop",
        "Balada",
        "Blues",
        "Disko",
        "Hip-hop",
        "Pop rock",
        "Slow rock",
        "M-pop",
        "K-pop",
        "J-pop",
        "R&B",
        "Trot",
        "Elektropop",
        "Rapper",
        "Heavy metal",
        "Tradisional",
        ]

    x = random.choice(music)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What music am I thinking of?"))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()