import random
import time

time.sleep(1)

def rockPaperScissors():
    computerChoice = random.randint(1, 3)
    if computerChoice == 1:
        computerChoice = "rock"
    elif computerChoice == 2:
        computerChoice = "paper"
    elif computerChoice == 3:
        computerChoice = "scissors"
    print("Welcome to rock, paper, scissors!")
    time.sleep(1)
    while True:
        playerChoice = input("What do you choose, rock, paper, or scissors?: ")    
        if playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
            break
        else:
            print("Please say rock, paper, or scissors!")

    time.sleep(1)
    print("Rock..")
    time.sleep(1)
    print("Paper..")
    time.sleep(1)
    print("Scissors..")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)

    if computerChoice == playerChoice:
        print(f"It's a tie! The computer chose: {computerChoice}")
    elif (computerChoice == "rock" and playerChoice == "paper") or (computerChoice == "scissors" and playerChoice == "rock") or (computerChoice == "paper" and playerChoice == "scissors"):
        print(f"You won!  The computer chose: {computerChoice}")
    elif (computerChoice == "rock" and playerChoice == "scissors") or (computerChoice == "scissors" and playerChoice == "paper") or (computerChoice == "paper" and playerChoice == "rock"):
        print(f"You lost!  The computer chose: {computerChoice}")

def numberGuess():
    number = random.randint(1, 100)
    guesses = 0
    guess = 0
    print("Welcome to number guess!  Guess a number between 1 and 100, inclusive.")
    time.sleep(1)

    while True:
        guess = input("What's your guess?  Please say an integer from 1 to 100, inclusive: ")
        print("Calculating...")
        time.sleep(1)
        try:
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
            print("Please say an integer from 1 to 100, inclusive!")

numberGuess()