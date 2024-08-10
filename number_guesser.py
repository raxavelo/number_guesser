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
