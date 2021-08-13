def LineSpace():
    print('')
    
LineSpace()

import random

name = input("What is you Name?")
congratsMessage = "Congradulations {name} you win!"
loseMessage = "Sorry {name} you lost, please try again!"

LineSpace()

print(f"Welcome {name}! This is the Python 101 Project")

LineSpace()
# Start of Program Dialog Asking if you want to play
def DoYouWantToPlay():
    question = input("Do you want to play a Game of Rock, Paper, Scissors?  ")
    if question.lower() == "yes":
        LineSpace()
        print(f"Great {name} lets Play!")
        LineSpace()
        PlayGame()
    elif question.lower() == "no":
        LineSpace()
        print("Goodbye")
        
    elif question.lower() != "yes" or "no":
        LineSpace()
        print('Sorry please input Yes or No')
        DoYouWantToPlay()


def PlayGame():
    while True:
        player_choice = input("Choose Rock, Paper, or Scissors!  ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_choice = random.choice(possible_actions)
        print(f'{name} you chose {player_choice} and the computer chose {computer_choice}')
    
        if player_choice == computer_choice:
            print(f"{name} you tied with the computer!")
            continue
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print(f"Rock smashes scissors {name} wins!")
            else:
                print(f"Paper covers Rock {name} loses!")
        elif player_choice == "scissors":
            if computer_choice == "paper":
                print(f"Scissors cut Paper {name} Wins!")
            else:
                print(f"Rock smashes Scissors {name} Loses!")
        elif player_choice == "paper":
            if computer_choice == "rock":
                print(f"Paper covers Rock {name} Wins!")
            else:
                print(f"Scissors cut Paper {name} Loses!")
        
        play_again = input("Do you want to play again? (y/n):  ")
        if play_again.lower() != "y":
            break

DoYouWantToPlay() 



# TODO random ********* Done
# TODO while *********  Done
# TODO input ********* in progress
# TODO print formating ********* Done
# TODO comparison operators ********* Done 
# TODO break and continue ********* Done

