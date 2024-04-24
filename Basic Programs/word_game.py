logo = '''
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█ ▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█ ▄

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝'''
import random

# Define the initial number of lives and the list of words to choose from
lives = 2
words = ["apple", "ball", "cat", "dog", "elephant", "tiger", "maroon", "pikachu", "waterbottle", "people", "mouse",
         "Mechanics", "Diamond"]

# Choose a random word from the list and convert it to lowercase
secret_word = random.choice(words).lower()

# Create a string of underscores with the same length as the secret word
blank_spaces = "_" * len(secret_word)

# Initialize the number of lives

# Loop until the player runs out of lives or guesses the word
while lives > 0 and '_' in blank_spaces:
    # Display the current progress (blank spaces representing unguessed letters)
    print(''.join(blank_spaces))

    # Ask the player to guess a letter and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        # If the guessed letter is in the word, reveal it in the blank spaces
        blank_spaces = [guess if secret_word[i] == guess else blank_spaces[i] for i in range(len(secret_word))]
    else:
        # If the guessed letter is not in the word, decrement the number of lives
        lives = lives - 1
        print(f"Wrong guess. You have {lives} lives left.")

    # Check if all letters have been guessed
    if '_' not in blank_spaces:
        # If there are no more blank spaces, the player has guessed all the letters
        print(f"Congratulations! The word was {secret_word}. You won!!!")
        break

# If the player runs out of lives without guessing the word, display the secret word
else:
    print(f"Sorry! You lost. The secret word was {secret_word}")
