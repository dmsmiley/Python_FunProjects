# creating a magic 8 ball generator
# list = the 20 responses on an 8 ball
import random
import time
import sys

list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
        "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
list2 = ["Let me think about it.", "Aww, that's a great question!",
         "...I wouldn't have asked that."]


def end_game():
    print("Thank you for playing!")
    print("Good bye!")
    print(input("Press ENTER to exit"))
    sys.exit()


def game_active():
    game = True
    while game == True:
        input("Please ask me a yes or no question: ")

        print(random.choice(list2))
        print(". . . .")
        time.sleep(3)
        print(random.choice(list))

        reply = input("Would you like to ask another question?: ")
        if reply == "yes":
            game = True
        elif reply == "Y":
            game = True
        elif reply == "YES":
            game = True
        elif reply == "Yes":
            game = True
        elif reply == "y":
            game = True
        else:
            end_game()


print("Welcome to the Magic 8 Ball!")
game_active()
