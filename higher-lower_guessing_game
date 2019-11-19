#creating guessing game from 1-100. computer tells user if the num is higher or lower. congrats message when correct guess. print out num of guesses. allow users to restart

import random
import sys

def end_game():
    print("\nThank you for playing!")
    print("Good bye!")
    print(input("Press ENTER to exit"))
    sys.exit()

def main_game():
  guess = True
  a = random.randint(1,101)
  count = 0
  while guess == True:
    b = int(input("What number am I thinking? "))
    count += 1
    if a == b:
      print("That's right!")
      print(f"It took you {count} guesses")
      go_again()
    elif a < b:
      print("Lower")
    else:
      print("Higher")

def go_again():
  reply = input("Would you like to play again?: ")
  reply = reply.lower()
  if reply == "yes":
    main_game()
  elif reply == "y":
    main_game()
  else:
    end_game()

main_game()
