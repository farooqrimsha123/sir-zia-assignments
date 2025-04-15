# python number guessing game 
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guessing = 0
is_running = True

print("python number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guess += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"please select a number between {lowest_num} and {highest_num}")

        else:
            print("Invalid guess")
            print(f"please select a number between {lowest_num} and {highest_num}")