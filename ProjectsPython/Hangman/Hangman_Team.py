import random
from colorama import Fore
from colorama import Style

# Access the file for the Game
with open("countries-and-capitals.txt") as places:
    lines = places.readlines()
    list_places = []

    # Cleaning the list more readable
    for place in lines:
        words = place.split(' | ' or ',')
        list_places.append(words[0])
        list_places.append(words[1])

    place_list = []

    for place in list_places:
        place_list.append(place.strip())

    # Creating Difficulty
    easy = []
    medium = []
    hard = []

    for place in place_list:
        if len(place) < 5:
            easy.append(place)

        elif len(place) >= 5 and len(place) <= 7:
            medium.append(place)

        elif len(place) >= 7:
            hard.append(place)


    # Create Random Word
    def create_random_word(place__list):
        word = random.choice(place__list)
        return word


    # Make the Random Word Blank
    def blank_random_word(place_list):
        word = create_random_word(place_list)
        spaced_word = " ".join(list(word))
        blank_word = spaced_word
        for character in blank_word:
            if character != " " and character != "-":
                blank_word = blank_word.replace(character, "_")
        print("{: ^150s}".format("\n", "Your Word to guess:\n   ", blank_word, "\n"))
        return blank_word, spaced_word, word


    print(" ")
    print("{: ^150s}".format("Welcome to HANGMAN!"))
    print(" ")
    print("{: ^150s}".format("Let's Play!"))
    print(" ")
    print("{: ^150s}".format("What's your desired dificulty level?   Choose between: EASY, MEDIUM and HARD\n"))


    # Choose the Difficulty Level
    def difficulty_level():
        invalid_difficulty_choice = True
        while invalid_difficulty_choice:

            difficulty = input("{: ^150s}".format("Your chosen difficulty:\n ")).upper()
            print("\n")

            if difficulty == "EASY":
                invalid_difficulty_choice = False
                life = 7
                print("{: ^150s}".format(f"You have {life} lives"))
                secret = blank_random_word(easy)
                return life, secret[0], secret[1], secret[2]

            elif difficulty == "MEDIUM":
                invalid_difficulty_choice = False
                life = 5
                print("{: ^150s}".format(f"You have {life} lives"))
                secret = blank_random_word(medium)
                return life, secret[0], secret[1], secret[2]

            elif difficulty == "HARD":
                invalid_difficulty_choice = False
                life = 4
                print("{: ^150s}".format(f"You have {life} lives"))
                secret = blank_random_word(hard)
                return life, secret[0], secret[1], secret[2]

            else:
                invalid_difficulty_choice is True
                print("{: ^150s}".format("Not a valid difficulty level. Choose again between: EASY, MEDIUM or HARD."))


    correct_letters = set()
    incorrect_letters = set()


    # Creating the Ascii Hangman depending on levels

    def easy_lives_left():
        if len(incorrect_letters) == 1:
            h = ["""
                --------
                |      |
                |   
                |    
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 2:
            h = ["""
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 3:
            h = ["""
                --------
                |      |
                |      O
                |      |
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 4:
            h = ["""
                --------
                |      |
                |      O
                |     (|
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 5:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 6:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |     /
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 7:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |     / L
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
            print(f"Too bad... You lost! The word was {Fore.GREEN}{word}{Style.RESET_ALL}")
            print("GAME OVER")
            hangman0 = [
                '''
            __   _____  _   _   _     ___  ____ _____ _ 
            \ \ / / _ \| | | | | |   / _ \/ ___|_   _| |
             \ V / | | | | | | | |  | | | \___ \ | | | |
              | || |_| | |_| | | |__| |_| |___) || | |_|
              |_| \___/ \___/  |_____\___/|____/ |_| (_)

                '''
            ]

            for drawing in hangman0:
                print(f"{Fore.CYAN}{drawing}{Style.RESET_ALL}")
            exit()


    def medium_lives_left():
        if len(incorrect_letters) == 1:
            h = ["""
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 2:
            h = ["""
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 3:
            h = ["""
                --------
                |      |
                |      O
                |      |
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 4:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 5:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |     / L
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
            print(f"Too bad... You lost! The word was {Fore.GREEN}{word}{Style.RESET_ALL}")
            print("GAME OVER")
            hangman0 = [
                '''
            __   _____  _   _   _     ___  ____ _____ _ 
            \ \ / / _ \| | | | | |   / _ \/ ___|_   _| |
             \ V / | | | | | | | |  | | | \___ \ | | | |
              | || |_| | |_| | | |__| |_| |___) || | |_|
              |_| \___/ \___/  |_____\___/|____/ |_| (_)

                '''
            ]

            for drawing in hangman0:
                print(f"{Fore.CYAN}{drawing}{Style.RESET_ALL}")
            exit()


    def hard_lives_left():
        if len(incorrect_letters) == 1:
            h = ["""
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 2:
            h = ["""
                --------
                |      |
                |      O
                |      |
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 3:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |      
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
        elif len(incorrect_letters) == 4:
            h = ["""
                --------
                |      |
                |      O
                |     (|)
                |     / L
                |     
                -
                """
                 ]
            for drawing in h:
                print(f"{Fore.GREEN}{drawing}{Style.RESET_ALL}")
            print(f"Too bad... You lost! The word was {Fore.GREEN}{word}{Style.RESET_ALL}")
            print("GAME OVER")
            hangman0 = [
                '''
            __   _____  _   _   _     ___  ____ _____ _ 
            \ \ / / _ \| | | | | |   / _ \/ ___|_   _| |
             \ V / | | | | | | | |  | | | \___ \ | | | |
              | || |_| | |_| | | |__| |_| |___) || | |_|
              |_| \___/ \___/  |_____\___/|____/ |_| (_)

                '''
            ]

            for drawing in hangman0:
                print(f"{Fore.CYAN}{drawing}{Style.RESET_ALL}")
            exit()


    # Ask for letter Input and check & The showing of the letter
    def ask_letter_input(blank_word):
        quit = "quit"
        print("\n", "   Your Word to guess:     ", blank_word, "\n")
        while True:
            print("Time to guess a letter!")
            letter = input("Your letter is: ").upper()
            small_letter = letter.lower()
            if letter == quit.upper() or letter == quit.lower():
                print("GoodBye!")
                hangman0 = [
                    '''
                 _____ _   _  _____   _____ _   _______ 
                |_   _| | | ||  ___| |  ___| \ | |  _  |
                  | | |  _  ||  __|  |  __|| . ` | | | |
                  | | | | | || |___  | |___| |\  | |/ / 
                  \_/ \_| |_/\____/  \____/\_| \_/___/  
                    '''
                ]

                for drawing in hangman0:
                    print(f"{Fore.MAGENTA}{drawing}{Style.RESET_ALL}")

                exit()
            elif len(letter) != 1:
                print("{: ^150s}".format("Please try to type a single letter!"))
            elif letter in correct_letters or small_letter in correct_letters:
                print("{: ^150s}".format('You have already guessed that letter. Choose again.'))
            elif letter in incorrect_letters or small_letter in incorrect_letters:
                print("{: ^150s}".format("You tried this letter before and it is not in your word. Choose again."))
            elif not letter.isalpha():
                print("{: ^150s}".format('Please enter a Letter'))
            elif letter in word:
                correct_letters.add(letter)
                word_as_list = list(blank_word)
                indices = [i for i, character in enumerate(spaced_word) if character == letter]
                for index in indices:
                    word_as_list[index] = letter
                blank_word = "".join(word_as_list)
                print("\n", "   Your Word to guess:     ", blank_word, "\n")
                print(F"Correct letters guessed {Fore.BLUE}{correct_letters}{Style.RESET_ALL}")
                print(f"Incorrect letters guessed {Fore.RED}{incorrect_letters}{Style.RESET_ALL} ""\n", "\n")
                if "_" not in blank_word:
                    print("CONGRATULATIONS")
                    win = [
                        '''

                    __   _____  _   _  __        _____  _   _   _____ _   _ _____    ____    _    __  __ _____ _ 
                    \ \ / / _ \| | | | \ \      / / _ \| \ | | |_   _| | | | ____|  / ___|  / \  |  \/  | ____| |
                     \ V / | | | | | |  \ \ /\ / / | | |  \| |   | | | |_| |  _|   | |  _  / _ \ | |\/| |  _| | |
                      | || |_| | |_| |   \ V  V /| |_| | |\  |   | | |  _  | |___  | |_| |/ ___ \| |  | | |___|_|
                      |_| \___/ \___/     \_/\_/  \___/|_| \_|   |_| |_| |_|_____|  \____/_/   \_\_|  |_|_____(_)
                        '''
                    ]

                    for drawing in win:
                        print(f"{Fore.YELLOW}{drawing}{Style.RESET_ALL}")
                    exit()

            elif small_letter in word:
                correct_letters.add(small_letter)
                word_as_list = list(blank_word)
                indices = [i for i, character in enumerate(spaced_word) if character == small_letter]
                for index in indices:
                    word_as_list[index] = letter.lower()
                blank_word = "".join(word_as_list)
                print("\n", "   Your Word to guess:     ", blank_word, "\n")
                print(f"Correct letters guessed {Fore.BLUE}{correct_letters}{Style.RESET_ALL}")
                print(f"Incorrect letters guessed {Fore.RED}{incorrect_letters}{Style.RESET_ALL}" "\n", "\n")
                if "_" not in blank_word:
                    print("CONGRATULATIONS")
                    win = [
                        '''

                    __   _____  _   _  __        _____  _   _   _____ _   _ _____    ____    _    __  __ _____ _ 
                    \ \ / / _ \| | | | \ \      / / _ \| \ | | |_   _| | | | ____|  / ___|  / \  |  \/  | ____| |
                     \ V / | | | | | |  \ \ /\ / / | | |  \| |   | | | |_| |  _|   | |  _  / _ \ | |\/| |  _| | |
                      | || |_| | |_| |   \ V  V /| |_| | |\  |   | | |  _  | |___  | |_| |/ ___ \| |  | | |___|_|
                      |_| \___/ \___/     \_/\_/  \___/|_| \_|   |_| |_| |_|_____|  \____/_/   \_\_|  |_|_____(_)
                        '''
                    ]

                    for drawing in win:
                        print(f"{Fore.YELLOW}{drawing}{Style.RESET_ALL}")
                    exit()
            else:
                incorrect_letters.add(letter)
                print(f"The letter {letter} is not in your word.\n")
                print(f"Correct letters guessed {Fore.BLUE}{correct_letters}{Style.RESET_ALL}")
                print(f"Incorrect letters {Fore.RED}{incorrect_letters}{Style.RESET_ALL}""\n", "\n")
                print("\n", "Your Word to guess:   ", blank_word, "\n")
                if life == 7:
                    easy_lives_left()
                elif life == 5:
                    medium_lives_left()
                elif life == 4:
                    hard_lives_left()


    life, blank_word, spaced_word, word = difficulty_level()
    letter = ask_letter_input(blank_word)
