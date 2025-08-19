import random

options =["rock","paper","scissors"]
selection = random.choice(options)
print("""===================
Rock Paper Scissors
===================""")
user = input(
"""1) ✊
2) ✋
3) ✌️
Pick a number: """)

try:
    user_choice = int(user)
    if user_choice in [1,2,3]:
        user_choice_indexed = options[user_choice - 1]
        print(f"you chose:{user_choice_indexed}")
        print(f"computer chose:{selection}")

        if user_choice_indexed == selection:
            print("it was a tie")
        elif (user_choice_indexed == "rock" and selection == "scissors") or \
        (user_choice_indexed == "paper" and selection == "rock") or \
        (user_choice_indexed == "scissors" and selection == "paper"):
            print("You Win!!!")
        else:
            print("You lose")
    else:
        print("please enter a number from 1-3")
except ValueError:
    print("please enter a valid number from 1-3")