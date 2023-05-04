import os.path

MAX_TRIES = 6
def welcome():
    """
    Prints a welcome message for the Hangman game along with the maximum number of tries allowed.
    """
    print("Welcome to the game Hangman")
    print("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
    print("The maximum number of tries allowed:", MAX_TRIES)


HANGMAN_PHOTOS = {1: """    x-------x""",
                  2: """    x-------x
    |
    |
    |
    |
    |
""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |
""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
def print_hangman(num_of_tries):
    """
    Prints the hangman graphic based on the number of failed tries.
    :param num_of_tries: The number of tries the player has made.
    :type num_of_tries: int
    """
    print(HANGMAN_PHOTOS[num_of_tries + 1])

def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player has won the game.
    :param secret_word: The secret word the player needs to guess.
    :param old_letters_guessed: A list of letters the player has guessed.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if the player has won, False otherwise.
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    Displays the current state of the secret word, with guessed letters revealed and unguessed letters as underscores.
    :param secret_word: The secret word the player needs to guess.
    :param old_letters_guessed: A list of letters the player has guessed.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: The current state of the secret word as a string.
    :rtype: str
    """
    shown_string = ""
    for letter in secret_word:
        if letter not in old_letters_guessed:
            shown_string += "_"
        else:
            shown_string += letter
    shown_string = " ".join(list(shown_string))
    return shown_string

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the input letter is valid.
    :param letter_guessed: The letter the player has guessed.
    :param old_letters_guessed: A list of letters the player has guessed.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the input is valid, False otherwise.
    :rtype: bool
    """
    if len(letter_guessed) >= 2 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Tries to update the list of guessed letters with the input letter if it is valid.
    :param letter_guessed: The letter the player has guessed.
    :param old_letters_guessed: A list of letters the player has guessed.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the list was updated, False otherwise.
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    if len(old_letters_guessed) > 0:
        print(" -> ".join(sorted(old_letters_guessed)))
    return False

def choose_word(file_path, index):
    """
    Chooses a secret word from a given file based on the provided index.
    :param file_path: The path to the file containing the words.
    :param index: The index of the word to choose from the file.
    :type file_path: str
    :type index: int
    :return: The chosen secret word.
    :rtype: str
    """
    words_file = open(file_path, 'r')
    words_data = words_file.read()
    words_file.close()
    words_list = words_data.split(' ')
    if index > len(words_list):
        index = index % len(words_list)
    secret_word = words_list[index - 1]
    return secret_word

def handle_initial_input():
    """
    Handles the initial input of file path and index for the game.
    :return: A tuple containing the file path and index.
    :rtype: tuple
    """
    # Only small letters for the words in the file
    file_path = input("\nEnter file path: ")
    # Loop until receiving a valid file path
    while not os.path.exists(file_path):
        file_path = input("File path doesn't exist, Enter new file path: ")
    index = input("Enter index: ")
    # Loop until receiving a valid index
    while not index.isnumeric() or int(index) <= 0:
        index = input("Index not valid, try again: ")
    index = int(index)
    return file_path, index

def hangman(secret_word):
    """
    The Hangman game function, handles the flow of the game
    :param secret_word: The secret word the player needs to guess.
    :type secret_word: str
    """
    # Set starting values
    old_letters_guessed = []
    num_of_tries = 0

    # Show starting messages and status
    print("\nLet's start!\n")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed) + '\n')

    # Game loop, continues as long as the game is played (no win or loss)
    while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:
        letter_guess = input("Guess a letter: ").lower()
        # Loop until receiving a valid guess (letter and wasn't guessed before)
        while not try_update_letter_guessed(letter_guess, old_letters_guessed):
            letter_guess = input("Guess a letter: ").lower()
        if letter_guess not in secret_word:
            # Handle wrong guess (increase the failed tries, inform user, print the hanged man state)
            num_of_tries += 1
            print(":(\n")
            print_hangman(num_of_tries)
        # Print the current word status
        print(show_hidden_word(secret_word, old_letters_guessed))

    # Check weather the game has ended with a win or loss
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
        return
    print("LOSE")

def main():
    # Show open screen
    welcome()
    # Receive the file path and index, then and get the secret word
    file_path, index = handle_initial_input()
    secret_word = choose_word(file_path, index)
    # Start the game
    hangman(secret_word)

if __name__ == '__main__':
    main()