#creating a coin estimator by weight
#allows users to input the total weight of each type of coin
#then print how many coins they have
#then print how many of each type of wrapper is needed
#then print the estimated total value of all the money

#coins
#penny = 2.5grams or .0055 lbs
#nickel = 5grams or .011 lbs
#dime = 2.27grams or .005 lbs
#quarter = 5.67 grams or .0125 lbs

#wrappers
#penny = 50 count, $0.50, and 125grams or .275578lbs 
#nickel = 40 count, $2.00, and 200grams or .44lbs
#dime = 50 count, $5.00, and 113.4grams or .25lbs
#quarter = 40 count, $10.00, and 226.8grams or .50lbs
import math
import time
import sys

def end_game():
    print("\nThank you for playing!")
    print("Good bye!")
    print(input("Press ENTER to exit"))
    sys.exit()

def pounds():
  p = float(input("\nHow many pounds of pennies do you have? "))
  n = float(input("How many pounds of nickels do you have? "))
  d = float(input("How many pounds of dimes do you have? "))
  q = float(input("How many pounds of quarters do you have? "))

  #weight to 2 decimal places
  p = round(p, 2)
  n = round(n, 2)
  d = round(d, 2)
  q = round(q, 2)

  #adding value of coins with pounds, thus the multiplication
  pv = (p / .00551156) * .01
  pv = "%.2f" % round(pv, 2) 
  print(f"\nYou have approx. ${pv} in pennies")
  nv = (n / .011) * .05
  nv =  "%.2f" % round(nv, 2)
  print(f"You have approx. ${nv} in nickels")
  dv = (d / .005) * .1
  dv = "%.2f" % round(dv, 2)
  print(f"You have approx. ${dv} in dimes")
  qv = (q / .0125) * .25
  qv = "%.2f" % round(qv, 2)
  print(f"You have approx. ${qv} in quarters")


  #estimating the number of wrappers by coin count in lbs
  #p = .275578 I need to convert to number of pennies. if i have .275578lbs, I know I have 50 pennies, which is .00551156
  pc = (p / .00551156) / 50
  pc = math.floor(pc)
  nc = (n / .011) / 40
  nc = math.floor(nc)
  dc = (d / .005) / 50
  dc = math.floor(dc)
  qc = (q / .0125) / 40
  qc = math.floor(qc)
  if pc == 1:
    print(f"\nYou can fill {pc} wrapper of pennies.")
  elif pc == 0:
    print(f"\nYou can fill no wrappers of pennies.")
  else:
    print(f"\nYou can fill {pc} wrappers of pennies.")
  if nc == 1:
    print(f"You can fill {nc} wrapper of nickels.")
  elif nc == 0:
    print(f"You can fill no wrappers of nickels.")
  else:
    print(f"You can fill {nc} wrappers of nickels.")
  if dc == 1:
    print(f"You can fill {dc} wrapper of dimes.")
  elif dc == 0:
    print(f"You can fill no wrappers of dimes.")
  else:
    print(f"You can fill {dc} wrappers of dimes.")
  if qc == 1:
    print(f"You can fill {qc} wrapper of quarters.")
  elif qc == 0:
    print(f"You can fill no wrappers of quarters.")
  else:
    print(f"You can fill {qc} wrappers of quarters.")
  again = input("\nWould you like to weigh again?: ")
  again = again.lower()
  if again == "yes":
    game()
  elif again == "y":
    game()
  else:
    end_game()

def grams():
  p = float(input("\nHow many grams of pennies do you have? "))
  n = float(input("How many grams of nickels do you have? "))
  d = float(input("How many grams of dimes do you have? "))
  q = float(input("How many grams of quarters do you have? "))

  #weight to 2 decimal places
  p = round(p, 2)
  n = round(n, 2)
  d = round(d, 2)
  q = round(q, 2)

  #adding value of coins with grams, thus the multiplication
  pv = (p / 2.50) * .01
  pv = "%.2f" % round(pv, 2) 
  print(f"\nYou have approx. ${pv} in pennies")
  nv = (n / 5.00) * .05
  nv =  "%.2f" % round(nv, 2)
  print(f"You have approx. ${nv} in nickels")
  dv = (d / 2.268) * .1
  dv = "%.2f" % round(dv, 2)
  print(f"You have approx. ${dv} in dimes")
  qv = (q / 5.67) * .25
  qv = "%.2f" % round(qv, 2)
  print(f"You have approx. ${qv} in quarters")

  #estimating the number of wrappers by coin count
  #p = 125 I need to convert to number of pennies. if i have 125 pennies, I know I have 50 pennies, which is 2.5
  pc = (p / 2.5) / 50
  pc = math.floor(pc)
  nc = (n / 5) / 40
  nc = math.floor(nc)
  dc = (d / 2.268) / 50
  dc = math.floor(dc)
  qc = (q / 5.67) / 40
  qc = math.floor(qc)
  if pc == 1:
    print(f"\nYou can fill {pc} wrapper of pennies.")
  elif pc == 0:
    print(f"\nYou can fill no wrappers of pennies.")
  else:
    print(f"\nYou can fill {pc} wrappers of pennies.")
  if nc == 1:
    print(f"You can fill {nc} wrapper of nickels.")
  elif nc == 0:
    print(f"You can fill no wrappers of nickels.")
  else:
    print(f"You can fill {nc} wrappers of nickels.")
  if dc == 1:
    print(f"You can fill {dc} wrapper of dimes.")
  elif dc == 0:
    print(f"You can fill no wrappers of dimes.")
  else:
    print(f"You can fill {dc} wrappers of dimes.")
  if qc == 1:
    print(f"You can fill {qc} wrapper of quarters.")
  elif qc == 0:
    print(f"You can fill no wrappers of quarters.")
  else:
    print(f"You can fill {qc} wrappers of quarters.")
  again = input("\nWould you like to weigh again?: ")
  again = again.lower()
  if again == "yes":
    game()
  elif again == "y":
    game()
  else:
    end_game()

def game():
  game = True
  while game == True:
    ans = int(input("\nPress 1 for weight in grams. Press 2 for weight in lbs. "))
    if ans == 1:
      grams()
    elif ans == 2:
      pounds()
    else:
      sure = input("\nPlease press either 1 or 2. Other else...")
      if sure == 1:
        grams()
      elif sure == 2:
        pounds()
      else:
        end_game()


def game_intro():
  print("Welcome to the Coin Weight Estimator!")
  time.sleep(1)
  print("\nIn this app you will weigh your coins by pennies, nickels, dimes, and quarters, and I will return the approximate value for each, how many wrappers your will need to roll them, and how much dough you have!")
  time.sleep(1)

game_intro()
game()
end_game()
