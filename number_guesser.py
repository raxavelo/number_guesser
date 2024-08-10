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

while True:
    user_guess = input("Guess a number between 0 and " + str(top_of_range))
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
