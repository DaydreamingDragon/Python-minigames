import random
import time

time.sleep(1)

def rockPaperScissors():
    # Intro
    print("Welcome to rock, paper, scissors!")
    time.sleep(1)

    # Generate computer's choice
    computerChoice = random.randint(1, 3)
    if computerChoice == 1:
        computerChoice = "rock"
    elif computerChoice == 2:
        computerChoice = "paper"
    elif computerChoice == 3:
        computerChoice = "scissors"

    # Get player's choice
    while True:
        playerChoice = input("What do you choose, rock, paper, or scissors?: ")    
        if playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
            break
        else:
            print("Please say rock, paper, or scissors!")

    # Generate suspense
    time.sleep(1)
    print("Rock..")
    time.sleep(1)
    print("Paper..")
    time.sleep(1)
    print("Scissors..")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)

    # Evaluate both choices
    if computerChoice == playerChoice:
        print(f"It's a tie! The computer chose: {computerChoice}")
    elif (computerChoice == "rock" and playerChoice == "paper") or (computerChoice == "scissors" and playerChoice == "rock") or (computerChoice == "paper" and playerChoice == "scissors"):
        print(f"You won!  The computer chose: {computerChoice}")
    elif (computerChoice == "rock" and playerChoice == "scissors") or (computerChoice == "scissors" and playerChoice == "paper") or (computerChoice == "paper" and playerChoice == "rock"):
        print(f"You lost!  The computer chose: {computerChoice}")

def numberGuess():
    # Intro
    print("Welcome to number guess!  Guess a number between 1 and 100, inclusive.")
    time.sleep(1)

    # Initialize variables
    number = random.randint(1, 100)
    guesses = 0
    guess = 0

    while True:
        # Get the user's guess
        guess = input("What's your guess?  Please say an integer from 1 to 100, inclusive: ")
        print("Calculating...")
        time.sleep(1)
        try:
            # Evaluate the user's guess
            guessInt = int(guess)
            if guessInt == number:
                print(f"You guessed the number!  It took you {guesses} tries.")
                break
            elif guessInt > number:
                print(f"Incorrect!  Your guess was greater than the number.")
                guesses += 1
            elif guessInt < number:
                print(f"Incorrect!  Your guess was less than the number.")
                guesses += 1
        except ValueError:
            # Make sure they input an integer
            print("Please say an integer from 1 to 100, inclusive!")

def coinFlip():
    # Intro 
    print("Welcome to coinflip!")
    time.sleep(1)

    # Flip the coin and get the outcome
    n = random.randint(1, 2)
    if n == 1:
        flip = "heads"
    elif n == 2:
        flip = "tails"

    # Get the user's guess
    while True:
        guess = input("Heads or tails?: ")
        if guess == "heads" or guess == "tails":
            break
        else:
            print("Please say heads or tails!")
            time.sleep(1)
    
    # Flip messages to add suspense
    time.sleep(1)
    print("Flipping...")
    time.sleep(1)
    print("Flipping...")
    time.sleep(1)
    print("Flipping...")
    time.sleep(1)

    # Evaluate the user's guess
    if flip == guess:
        print(f"Congrats, you guessed correctly!  The coin landed on {flip}.")
    else:
        print(f"Sorry, but you did not guess correctly!  The coin landed on {flip}.")

def memoryGame():
    # Intro
    print("Welcome to memory game!")
    time.sleep(1)
    print("Memorize and repeat the combination of numbers.  Every time you get it right, the combination will be lengthened by 1 number.")
    time.sleep(3)
    print("Starting!")
    time.sleep(2)

    # Initialize list and score
    sequence = []
    score = 0

    # Add a number to the list to start
    sequence.append(str(random.randint(1, 9)))

    while True:
        # Print each number in the list
        for char in sequence:
            print(f"{char}")
            time.sleep(0.85)

        # Print a whole bunch of new lines to clear the sequence
        time.sleep(1)
        for i in range(100):
            print("")

        # Get the user's guess
        guess = input("Repeat the combination.  Remember, no spaces or new lines between new numbers: ")

        # Evaluate the user's guess
        if guess:
            if len(guess) != len(sequence):
                # If the user's input length does not equal length of the list then it's wrong
                print(f"Game over! Score: {score}")
                quit()

            for j in range(len(sequence)):
                # If it doesn't match, end the code and say game over and print the score
                if guess[j] != sequence[j]:
                    print(f"Game over! Score: {score}")
                    quit()

            # If it does, append another color to the list, add 1 to score, and repeat the function
            print("Correct!  Adding 1 number...")
            sequence.append(str(random.randint(1, 9)))
            score += 1
            time.sleep(1)
        # If the user doesn't input anything
        else:
            print(f"Game over!  Please enter an input next time! Score: {score}")
            quit()

def hangman():
    # Intro
    print("Welcome to hangman!")
    time.sleep(1)

    # Initialize variables
    words = ["computer", "coding", "bedsheet", "television", "running", "treadmill", "frisbee", "snake", "lantern", "trapezoid", "pyramid"]
    word = words[random.randint(0, (len(words) - 1))]
    attempts = 6
    guessedLetters = []
                
    while attempts > 0:
        # Print the word
        print("Word: ", end="")
        for char in word:
            if char in guessedLetters:
                print(f"{char}", end=" ")
            else:
                print(f"_", end=" ")
        print("\n")
        
        # Get the user's guess
        while True:
            guess = input("Enter a letter to guess: ").lower()
            try:
                float(guess)
                print("Please enter a letter!")
            except ValueError:
                if len(guess) == 1:
                    if guess not in guessedLetters:
                        break
                    else:
                        print("You already guessed that letter!")
                else:
                    print("Please enter a letter!")

        guessedLetters.append(guess)

        # Add suspense
        print("Evaluating...")
        time.sleep(1)

        if guess not in word:
            attempts -= 1
            print(f"Your letter was not in the word!  You have {attempts} attempts remaining.")
        elif guess in word:
            print("Your guess was in the word!")

        if all(letter in guessedLetters for letter in word):
            print(f"Congrats, you guessed the word!  It was {word}.")
            quit()

    # If user fails to guess the word
    print(f"You failed to guess the word!  The word was {word}.")

hangman()