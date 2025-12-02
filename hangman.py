# creating hangman game which is basically word finding game. Players make a guess which is limitted and try to find the exact word.
# After Each wrong guesses, drawing a man shape which seems like hanging the man part by part.
# Let's start the game and you will figure it out better.

print("Welcome to Hangman !!")
print("lets start the game !")

words = ["hamburg", "strawberry", "jaguar" , "rosemary" , "fridge" , "rihanna" , "apocalypse" , "seagull", "dates"]

import random

secret_word = random.choice(words)
hidden_word = ["_"] * len(secret_word)
hangman_pictures = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

wrong_guesses = 0
max_wrong = 6

print(f"Secret word has {len(secret_word)} letters!")

while "_" in hidden_word and wrong_guesses < max_wrong:
    print(hangman_pictures[wrong_guesses])
    print("Word to guess: " + " ".join(hidden_word))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")

    guess = input(" Guess a letter : ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print(" Please enter just one letter!")
        continue
    if guess in secret_word:
        print(f" Well Done! '{guess}' is in the word!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        print(f" Sorry, '{guess}' is not in the word.")
        wrong_guesses += 1

print(hangman_pictures[wrong_guesses])

if "_" not in hidden_word:
    print("Nailed it! The word was: " + secret_word)

else:
    print(" GAME OVER! The word was: " + secret_word)
    print(" try again!")

print("\nThanks for playing! ")





