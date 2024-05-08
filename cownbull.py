import random

def generate_secret_number():
    return random.sample(range(0, 10), 4)

def evaluate_guess(secret, guess):
    cows = sum((1 for i, j in zip(secret, guess) if i == j))
    bulls = sum((1 for i in secret if i in guess)) - cows
    return cows, bulls

def play_cow_bull_game():
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter your guess (a 4-digit number): ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        guess = [int(d) for d in guess]
        cows, bulls = evaluate_guess(secret_number, guess)
        attempts += 1

        if cows == 4:
            print(f"Congratulations! You've guessed the number '{''.join(map(str, secret_number))}' correctly in {attempts} attempts.")
            break
        else:
            print(f"Result: {cows} cows, {bulls} bulls. Try again!")

if __name__ == "__main__":
    print("Welcome to the Cow and Bull Game!")
    play_cow_bull_game()