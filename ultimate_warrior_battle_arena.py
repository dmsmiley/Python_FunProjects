#write a simple turn-based style game
#both the computer and player should start out at the same amount of health
#choose between three different moves
#first is low hp attack with high chance of hitting
#second is a high hp attack with low chance of hitting
#third move is a healing move
#after each move a message should pop up saying what happened and current health of the user and computer
#once either reaches zero, the game should end
#when computer's health reaches 35%, increase chance to cast heal
#give each a name

import random as rd
import time
import sys


villain_names = ['Task Rabbit', 'Omega', 'Patch Galactic', 'Misfit', 'Night Caller', 'Atomic', 'Patches', 'Voodoo', 'Aberation', 'Transonic', 'Nocturne', 'Overkill', 'Crossfire', 'Red Wolf', 'Dark Horse', 'Pyro', 'Slicer']
  
class player:
  def __init__(self, health, damage, name):
    self.health = health
    self.damage = damage
    self.name = name

class villain:
  def __init__(self, health, damage):
    self.health = health
    self.damage = damage

class round_num:
  def __init__(self, rnd):
    self.rnd = rnd

player.health = 100
villain.health = 100

player.damage = 0
villain.damage = 0
round_num.rnd = 1

def power_two():
  print(f"\nYou won round {round_num.rnd}!!!")
  round_num.rnd += 1
  time.sleep(2)
  print(f"\nBefore moving on to round {round_num.rnd}, you must first choose a power-up.")
  time.sleep(1)
  choice = True
  while choice == True:
    power = int(input("1) Increased health or 2) Increased attack damage: "))
    if power == 1:
      print("\nYour health has increased!")
      print("\nBut beware. The other fighters have become stronger as well.")
      time.sleep(3)
      player.health += 50
      villain.damage += 30
      main()
    elif power == 2:
      print("\nYour attack damage has increased!")
      print("\nBut beware. The other fighters have become stronger as well.")
      time.sleep(3)
      player.damage += 50
      villain.health += 30
      main()
    else:
      print("\nIncorrect input.\nPlease select a valid number.")

def power_one():
  if round_num.rnd == 2:
    power_two()
  print(f"\nYou won round {round_num.rnd}!!!")
  round_num.rnd += 1
  time.sleep(2)
  print(f"\nBefore moving on to round {round_num.rnd}, you must first choose a power-up.")
  time.sleep(1)
  choice = True
  while choice == True:
    power = int(input("1) Increased health or 2) Increased attack damage: "))
    if power == 1:
      print("\nYour health has increased!")
      print("\nBut beware. The other fighters have become stronger as well.")
      time.sleep(3)
      player.health += 50
      villain.damage += 30
      main()
    elif power == 2:
      print("\nYour attack damage has increased!")
      print("\nBut beware. The other fighters have become stronger as well.")
      time.sleep(3)
      player.damage += 50
      villain.health += 30
      main()
    else:
      print("\nIncorrect input.\nPlease select a valid number.")

def coin_toss():
  '''
  This function is for the coin tosses before each battle.
  '''
  hort = ["Heads", "Tails"]
  coin_toss = input("Choose heads or tails by typing 'Heads' or 'Tails': ")
  coin_toss = coin_toss.capitalize()
  gofirst = rd.choice(hort)
  if gofirst == coin_toss:
    print("\nYou have chosen wisely.")
    return True
  else:
    print("\nYou have chosen poorly.")
    return False

def main():
  opponent = "brad"
  print(f"\nWelcome to round {round_num.rnd}, {player.name}!")
  #time.sleep(2) 
  print(f"Your opponent today is {opponent}.\n")
  #time.sleep(4)
  print("We will flip a coin to see who goes first.")
  player_turn = coin_toss()

  begin_player_health = player.health
  begin_villain_health = villain.health

  game = True

  while game:
    while (player.health > 0 or villain.health > 0):
      while player_turn == True:
        #time.sleep(2)
        print(f"\n{player.name}'s HP is {player.health}")
        print(f"{opponent}'s HP is {villain.health}")
        print(f"\nIt is {player.name}'s turn.")
        move = int(input("Please pick either the Fiery Jab (1), the Preeminent Throat Punch (2), or Heal (3): "))
        if move == 1:
          chance_1 = rd.randint(1,100)
          if chance_1 > 80:
            print("\nThe attack has missed")
            player_turn = False
          else:
            damage1 = rd.randint(10,25)
            damage1 += player.damage
            villain.health -= damage1
            print(f"\nYou dealt {damage1}HP of damage")
            player_turn = False
            if (villain.health <= 0):
              print(f"\n{opponent}'s HP is 0!")
              player.health = begin_player_health
              villain.health = begin_villain_health
              time.sleep(2)
              power_one()
        elif move == 2:
          chance2 = rd.randint(1,100)
          if chance2 > 55:
            print("\nThe attack has missed")
            player_turn = False
          else:
            damage2 = rd.randint(30,50)
            villain.health -= damage2
            print(f"\nYou dealt {damage2}HP of damage")
            player_turn = False
            if (villain.health <= 0):
              print(f"\n{opponent}'s HP is 0!")
              player.health = begin_player_health
              villain.health = begin_villain_health
              time.sleep(2)
              power_one()
        elif move == 3:
          chance3 = rd.randint(1,100)
          if chance3 > 70:
            print("\nUnable to heal")
            player_turn = False
          else:
            heal = rd.randint(25,40)
            player.health += heal
            print(f"\nYou were healed by {heal}HP")
            player_turn = False
        else:
          print("\nPlease pick a valid move: either 1, 2, or 3")

      else:  
        time.sleep(2)
        print(f"\n{player.name}'s HP is {player.health}")
        print(f"{opponent}'s HP is {villain.health}")
        print(f"\n{opponent} will decide his move.")
        time.sleep(2)
        
        crit_health_moves = [1,2,3,3]
        
        if (villain.health < 35):
          move = rd.choice(crit_health_moves)
        else:
          move = rd.randint(1,3)
        if move == 1:
          print(f"\n{opponent} has thrown a Fiery Jab!")
          time.sleep(2)
          chance1 = rd.randint(1,100)
          if chance1 > 80:
            print("\nThe attack has missed")
            player_turn = True
          else:
            damage1 = rd.randint(10,25)
            player.health -= damage1
            print(f"\n{opponent} dealt {damage1}HP of damage")
            if (player.health <= 0):
              print(f"\n{player.name}'s HP is 0!")
              time.sleep(2)
              player_lose()
              break
            else:
              player_turn = True
        if move == 2:
          print(f"\n{opponent} has thrown the Preeminent Throat Punch of Near Certain Death!")
          chance2 = rd.randint(1,100)
          time.sleep(2)
          if chance2 > 55:
            print("\nThe attack has missed")
            player_turn = True
          else:
            damage2 = rd.randint(30,50)
            player.health -= damage2
            print(f"\n{opponent} dealt {damage2}HP of damage")
            if (player.health <= 0):
              print(f"\n{player.name}'s HP is 0!")
              time.sleep(2)
              player_lose()
              break
            else:
              player_turn = True
        if move == 3:
          chance3 = rd.randint(1,100)
          if chance3 > 70:
            print(f"\n{opponent} was unable to heal")
            player_turn = True
          else:
            heal = rd.randint(25,40)
            villain.health += heal
            print(f"\n{opponent} healed by {heal}HP")
            player_turn = True

def player_win():
  print("\nYou won!!!!")
  print("\nAll fighters have been destroyed!")
  again = input("\nWould you like to play again (y/n)? ")
  if again == "y":
    main()
  else:
    print("Goodbye!")
    time.sleep(2)
    sys.exit()

def player_lose():
  print("\nYou have been dealt the killing blow")
  time.sleep(2)
  print("\nBetter luck next time")
  again = input("\nWould you like to play again (y/n)? ")
  if again == "y":
    main()
  else:
    print("\nGoodbye!")
    time.sleep(2)
    sys.exit()
    
def intro():
  print("\nWelcome to the Ultimate Warrior Battle Arena!\n")
  time.sleep(3.5)
  print("This turn based game will have you fighting the deadliest, most ruthless, and fiercest opponents in the galaxy!\n")
  time.sleep(5.5)
  print("Here's how you play:")
  time.sleep(3)
  print("You will be facing a fighter of my choosing, and you will fight to the death.\n")
  time.sleep(5.5)
  print("There are three rounds of fighting, and each round gets harder and harder.\n")
  time.sleep(5.5)
  print("You will be allowed three different moves.\n")
  time.sleep(5.5)
  print("The first is the quick and accurate Fiery Jab which will deal a moderate amount of damage.\n")
  time.sleep(5.5)
  print("The second is the strong and less accurate Preeminent Throat Punch of Near Certain Death, which when it hits will deal a crazy amount of damage.\n")
  time.sleep(9)
  print("Finally there is a move to Heal.\n")
  time.sleep(2.5)
  print("Let's get down to business.\n")
  time.sleep(2)
  player.name = input("What is your name? ")
  main()

if __name__ == "__main__":
  intro()

