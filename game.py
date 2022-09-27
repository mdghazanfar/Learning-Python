
import random

print("Hi! Welcome to the guessing game. Please a guess a number between 1 and 100")

guess= int(input("What is your number?: "))
correct_number =random.randint(1,100)

guess_count = 1

while guess != correct_number:
  guess_count += 1
  if guess < correct_number:
    guess =int(input("worng. You need to guess higher. what is your guess?: "))
  else:
    guess =int(input("worng. You need to guess Lower. what is your guess?: "))

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")
    