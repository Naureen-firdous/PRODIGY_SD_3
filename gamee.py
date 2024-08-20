import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed = False
    
    while not guessed:
        # Prompt the user for a guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")

# Run the game
if __name__ == "__main__":
    guess_the_number()