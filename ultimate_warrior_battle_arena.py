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


def player_win():
  print("You won!!!!")
  again = input("Would you like to play again? ")
  if again == "y":
    intro()
  else:
    print("Goodbye!")

def player_lose():
  print("Better luck next time")
  again = input("Would you like to play again? ")
  if again == "y":
    intro()
  else:
    print("Goodbye!")


villain_names = ['Task Rabbit', 'Omega', 'Patch Galactic', 'Misfit', 'Night Caller', 'Atomic', 'Patches', 'Voodoo', 'Aberation', 'Transonic', 'Nocturne', 'Overkill', 'Crossfire', 'Red Wolf', 'Dark Horse', 'Pyro', 'Slicer']


def main():
  print("\nWelcome to the Ultimate Warrior Battle Arena!\n")
  time.sleep(3.5)
  print("This turn based game will have you fighting the deadliest, most ruthless, and fiercest opponents in the galaxy!\n")
  time.sleep(5.5)
  print("Here's how you play:")
  time.sleep(3)
  print("You will be facing a fighter of my choosing, and you will fight to the death.\n")
  time.sleep(5.5)
  print("Each fighter will start with 100HP and be allowed three different moves.\n")
  time.sleep(5.5)
  print("The first is the quick and accurate Fiery Jab which will deal a moderate amount of damage.\n")
  time.sleep(5.5)
  print("The second is the strong and less accurate Preeminent Throat Punch of Almost Certain Death, which when it hits will deal a crazy amount of damage.\n")
  time.sleep(9)
  print("Finally there is a move to Heal.\n")
  time.sleep(2.5)
  print("Let's get down to business.\n")
  time.sleep(2)
  opponent = rd.choice(villain_names)
  name = input("What is your name? ")
  print(f"Welcome, {name}!")
  time.sleep(2) 
  print(f"Your opponent today is {opponent}.\n")
  time.sleep(4)
  print("We will flip a coin to see who goes first.")
  hort = ["Heads", "Tails"]
  coin_toss = input("Choose Heads or Tails: ")
  gofirst = rd.choice(hort)
  if gofirst == coin_toss:
    print("\nYou have choosen wisely.")
    player_turn = True
  else:
    print("\nYou have choosen poorly.")
    player_turn = False

  game = True

  while game:
    player_health = 100
    opp_health = 100

    while (player_health > 0 or opp_health > 0):
      while player_turn:
        time.sleep(2)
        print(f"\n{name}'s HP is {player_health}")
        print(f"{opponent}'s HP is {opp_health}")
        print(f"\nIt is {name}'s turn.")
        move = int(input("Please pick either the Fiery Jab (1), the Preeminent Throat Punch (2), or Heal (3): "))
        if move == 1:
          chance1 = rd.randint(1,100)
          if chance1 > 80:
            print("\nThe attack has missed")
            player_turn = False
            break
          else:
            damage1 = rd.randint(10,25)
            opp_health -= damage1
            print(f"\nYou dealt {damage1}HP of damage")
            player_turn = False
            if (opp_health <= 0):
              player_win()
              break
            else:
              break
        if move == 2:
          chance2 = rd.randint(1,100)
          if chance2 > 40:
            print("\nThe attack has missed")
            player_turn = False
            break
          else:
            damage2 = rd.randint(30,60)
            opp_health -= damage2
            print(f"\nYou dealt {damage2}HP of damage")
            player_turn = False
            if (opp_health <= 0):
              player_win()
              break
            else:
              break
        if move == 3:
          chance3 = rd.randint(1,100)
          if chance3 > 50:
            print("\nUnable to heal")
            player_turn = False
            break
          else:
            heal = rd.randint(25,40)
            player_health += heal
            print(f"\nYou were healed by {heal}HP")
            player_turn = False
            break
        else:
          print("\nPlease pick a valid move")

      else:  
        time.sleep(2)
        print(f"\n{name}'s HP is {player_health}")
        print(f"{opponent}'s HP is {opp_health}")
        print(f"\n{opponent} will decide his move.")
        time.sleep(2)
        move = rd.randint(1,3)
        if move == 1:
          chance1 = rd.randint(1,100)
          if chance1 > 80:
            print("\nThe attack has missed")
            player_turn = True
          else:
            damage1 = rd.randint(10,25)
            player_health -= damage1
            print(f"\n{opponent} dealt {damage1}HP of damage")
            if (player_health <= 0):
              player_lose()
              break
            else:
              player_turn = True
        if move == 2:
          chance2 = rd.randint(1,100)
          if chance2 > 40:
            print("\nThe attack has missed")
            player_turn = True
          else:
            damage2 = rd.randint(30,60)
            player_health -= damage2
            print(f"\n{opponent} dealt {damage2}HP of damage")
            if (player_health <= 0):
              player_lose()
              break
            else:
              player_turn = True
        if move == 3:
          chance3 = rd.randint(1,100)
          if chance3 > 50:
            print(f"\n{opponent} unable to heal")
            player_turn = True
          else:
            heal = rd.randint(25,40)
            opp_health += heal
            print(f"\n{opponent} healed by {heal}HP")
            player_turn = True

main()

