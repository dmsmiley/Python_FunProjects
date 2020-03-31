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

class Person:
  def __init__(self, health, damage, name):
    self.health = health
    self.damage = damage
    self.name = name

class Player(Person):
  def __init__(self, health, damage, name):
    Person.__init__(self, health, damage, name)

class Villain(Person):
  def __init__(self, health, damage, name):
    Person.__init__(self, health, damage, name)

class Round:
  def __init__(self, rnd):
    self.rnd = rnd

villain_names = ['Task Rabbit', 'Omega', 'Patch Galactic', 'Misfit', 'Night Caller', 'Atomic', 'Patches', 'Voodoo', 'Aberation', 'Transonic', 'Nocturne', 'Overkill', 'Crossfire', 'Red Wolf', 'Dark Horse', 'Pyro', 'Slicer']

reset_names = ['Task Rabbit', 'Omega', 'Patch Galactic', 'Misfit', 'Night Caller', 'Atomic', 'Patches', 'Voodoo', 'Aberation', 'Transonic', 'Nocturne', 'Overkill', 'Crossfire', 'Red Wolf', 'Dark Horse', 'Pyro', 'Slicer']

def fin():
  print('\nCongrats! You\'ve defeated the fiercest fighters in the galaxy!')
  again = input("\nWould you like to play again (y/n)? ")
  if again == "y":
    #reset all class values to original state
    Player.health, Player.damage = 100, 0
    Villain.health, Villain.damage = 100, 0 
    Round.rnd = 1
    #if there are too few villains for the next playthrough
    #return back to original list without duplicates
    if len(villain_names) <= 3:
      villain_names.extend(x for x in reset_names if x not in villain_names)
    main()
  else:
    print("\nGoodbye!")
    time.sleep(2)
    sys.exit()

def power_up():
  if Round.rnd == 3:
    fin()
  print(f"\nYou won round {Round.rnd}!!!")
  Round.rnd += 1
  time.sleep(2)
  print(f"\nBefore moving on to round {Round.rnd}, you must first choose a power-up.")
  time.sleep(1)
  choice = True
  while choice == True:
    power = int(input("1) Increased health or 2) Increased attack damage: "))
    if power == 1:
      print("\nYour health has increased!")
      print("\nBut beware. The other fighters have become stronger as well.")
      time.sleep(3)
      Player.health += 50
      Villain.damage += 30
      main()
    elif power == 2:
      print("\nYour attack damage has increased!")
      print("\nBut beware. The other fighters have become stronger as well.")
      time.sleep(3)
      Player.damage += 50
      Villain.health += 30
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
  Villain.name = rd.choice(villain_names)
  villain_names.remove(Villain.name)
  print(f"\nWelcome to round {Round.rnd}, {Player.name}!")
  #time.sleep(2) 
  print(f"Your opponent today is {Villain.name}.\n")
  #time.sleep(4)
  print("We will flip a coin to see who goes first.")
  player_turn = coin_toss()

  begin_player_health = Player.health
  begin_villain_health = Villain.health

  game = True

  while game:
    while (Player.health > 0 or Villain.health > 0):
      while player_turn == True:
        #time.sleep(2)
        print(f"\n{Player.name}'s HP is {Player.health}")
        print(f"{Villain.name}'s HP is {Villain.health}")
        print(f"\nIt is {Player.name}'s turn.")
        move = int(input("Please pick either the Fiery Jab (1), the Preeminent Throat Punch (2), or Heal (3): "))
        if move == 1:
          chance_1 = rd.randint(1,100)
          if chance_1 > 80:
            print("\nThe attack has missed")
            player_turn = False
          else:
            damage1 = rd.randint(10,25)
            damage1 += Player.damage
            Villain.health -= damage1
            print(f"\nYou dealt {damage1}HP of damage")
            player_turn = False
            if (Villain.health <= 0):
              print(f"\n{Villain.name}'s HP is 0!")
              Player.health = begin_player_health
              Villain.health = begin_villain_health
              time.sleep(2)
              power_up()
        elif move == 2:
          chance2 = rd.randint(1,100)
          if chance2 > 55:
            print("\nThe attack has missed")
            player_turn = False
          else:
            damage2 = rd.randint(30,50)
            Villain.health -= damage2
            print(f"\nYou dealt {damage2}HP of damage")
            player_turn = False
            if (Villain.health <= 0):
              print(f"\n{Villain.name}'s HP is 0!")
              Player.health = begin_player_health
              Villain.health = begin_villain_health
              time.sleep(2)
              power_up()
        elif move == 3:
          if Player.health >= begin_player_health:
            print("You are already at full health")
            player_turn = True
            break
          chance3 = rd.randint(1,100)
          if chance3 > 70:
            print("\nUnable to heal")
            player_turn = False
          else:
            heal = rd.randint(25,40)
            Player.health += heal
            print(f"\nYou were healed by {heal}HP")
            player_turn = False
        else:
          print("\nPlease pick a valid move: either 1, 2, or 3")

      else:  
        time.sleep(2)
        print(f"\n{Player.name}'s HP is {Player.health}")
        print(f"{Villain.name}'s HP is {Villain.health}")
        print(f"\n{Villain.name} will decide his move.")
        time.sleep(2)
        
        crit_health_moves = [1,2,3,3]
        
        if (Villain.health < 35): 
          move = rd.choice(crit_health_moves)
        elif (Villain.health >= begin_villain_health):
          move = rd.randint(1,2)
        else:
          move = rd.randint(1,3)
        if move == 1:
          print(f"\n{Villain.name} has thrown a Fiery Jab!")
          time.sleep(2)
          chance1 = rd.randint(1,100)
          if chance1 > 80:
            print("\nThe attack has missed")
            player_turn = True
          else:
            damage1 = rd.randint(10,25)
            Player.health -= damage1
            print(f"\n{Villain.name} dealt {damage1}HP of damage")
            if (Player.health <= 0):
              print(f"\n{Player.name}'s HP is 0!")
              time.sleep(2)
              player_lose()
              break
            else:
              player_turn = True
        if move == 2:
          print(f"\n{Villain.name} has thrown the Preeminent Throat Punch of Near Certain Death!")
          chance2 = rd.randint(1,100)
          time.sleep(2)
          if chance2 > 55:
            print("\nThe attack has missed")
            player_turn = True
          else:
            damage2 = rd.randint(30,50)
            Player.health -= damage2
            print(f"\n{Villain.name} dealt {damage2}HP of damage")
            if (Player.health <= 0):
              print(f"\n{Player.name}'s HP is 0!")
              time.sleep(2)
              player_lose()
              break
            else:
              player_turn = True
        if move == 3:
          chance3 = rd.randint(1,100)
          if chance3 > 70:
            print(f"\n{Villain.name} was unable to heal")
            player_turn = True
          else:
            heal = rd.randint(25,40)
            Villain.health += heal
            print(f"\n{Villain.name} healed by {heal}HP")
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
    print("\nThanks for playing!")
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
  Player.health, Player.damage = 100, 0
  Villain.health, Villain.damage = 100, 0
  Player.name = input("What is your name? ")
  Round.rnd = 1
  main()

if __name__ == "__main__":
  intro()
