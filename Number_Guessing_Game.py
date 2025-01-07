from random import randint
import art
import os

def clear():
   if os.name == 'nt':  # For Windows
     os.system('cls')
   else:  # For macOS/Linux
     os.system('clear')

def check_answer(player_guess, answer, turns):
  if player_guess > answer:
    print("Too high")
    return turns - 1
  elif player_guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You guess right. The answer was {answer}")

easy_level = 10
hard_level = 5

def set_difficulty():
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty_level == "easy":
    return easy_level
  else:
    return hard_level
  
def game():
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  
  turns = set_difficulty()
  
  player_guess = 0
  while player_guess != answer:
    print(f"You have {turns} attempts remaining.")
    player_guess = int(input("Make a guess: "))
    turns = check_answer(player_guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return     
game()
while True:
  repet = input("What to play again? 'y' or 'n' ")
  if repet == "y":
    clear()
    game()
  else:
    break
