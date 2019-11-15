#creating a pythagorean triple checker: a**2 + b**2 = c**2
#main goal is to see if the user's input for the three sides is a pythagorean triangle
#remember c is always the longest side
#loop the program
import time
import sys

def end_game():
    print("\nThank you for playing!")
    print("Good bye!")
    print(input("Press ENTER to exit"))
    sys.exit()

def game_active():
  game = True
  while game == True:
    a = int(input("\nHow long is side a? "))
    b = int(input("How long is side b? "))
    c = int(input("How long is side c? "))
    if a > c:
      print("Error: C must be the largest number")
      game = True
    elif b > c:
      print("Error: C must be the largest number")
      game = True
    elif (a**2 + b**2 == c**2):
      print("That's a pythagorean triangle!")
      reply = input("Would you like to check another one?: ")
      reply = reply.lower()
      if reply == "yes":
        game = True
      elif reply == "y":
        game = True
      else:
        game = False
    else:
      print("Sorry, that's not a pythagorean triangle.")
      reply = input("Would you like to check another one?: ")
      reply = reply.lower()
      if reply == "yes":
        game = True
      elif reply == "y":
        game = True
      else:
        game = False

def game_intro():
  print("Welcome to the Great Pythagorean Triple Checker!")
  time.sleep(4)
  print("\nTwo things to remember:")
  time.sleep(3)
  print("\nNumber 1: A Pythagorean Triple is when\nthe square of Side A plus the square of Side B \nequals the square of Side C, or a*2 + b*2 = c*2.")
  time.sleep(6)
  print("\nNumber 2: Side C is ALWAYS the largest number!")
  time.sleep(3)
  print("\nAlright, let's get started!")

game_intro()
game_active()
end_game()
