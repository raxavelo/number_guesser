import random

top_of_range = input("Enter the top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Next time, please enter a positive integer.")
        exit()
else:
    print("Next time, please enter a number.")
    exit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please, next time enter a number.")
        continue

    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < random_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

print(f"You got it in {guesses} guesses.")
