"""
App Module

This module handles user interactions, prints messages, and orchestrates the overall flow of the adventure game.
It contains functions for starting the game, presenting challenges, and displaying game over messages.

Functions:
- start_game(): Initiates the game and coordinates the overall flow.
- print_message(message): Prints a message to the user.
"""
# variables and imports
import Game   # Import the Game module
import Role1  # Import the Role1 module
import Role2  # Import the Role2 module

import random

# functions
def start_game():
    # This is the very beginning. It will print the introduction by welcoming the user and starting the game.
    print_introduction()

    # User picks role
    role = None
    role_choice = None
    role_choices = ['1', '2'] # 1 and 2 refer to roles 1 and 2

    print("Input [1] to play as [ROLE]\nInput [2] to play as [ROLE]\n")
    while role_choice not in role_choices:
        role_choice = input("-- Please input a role -- \n")
        
        if role_choice not in role_choices:
            print("Invalid input. Please select anything from the specified choices.")

    # Get game ready to start. Initialize everything.
    role_choice = int(role_choice)

    if role_choice == 1:
        role = Role1.initialize_role()
    elif role_choice == 2:
        role = Role2.initialize_role()
    print(("You have picked: " + role["name"] + " as your role! May the odds be in your favour."))

    # Game logic
    for i in range(1, 4): # This is the game's main loop in which it runs a challenge 3 times based on the role and challenge #.
        Game.play_challenge(role, i)

    # Game over message

def print_introduction():
    print("""  
            ▒▐█▒▐█▒▐█▀▀▒██░░░▒██░░░▒▐█▀▀█▌ 
            ▒▐████▒▐█▀▀▒██░░░▒██░░░▒▐█▄▒█▌ 
            ▒▐█▒▐█▒▐█▄▄▒██▄▄█▒██▄▄█▒▐██▄█▌
            
Welcome to the text adventure!
Embark on a thrilling quest where you'll choose your role, each with unique attributes. 
Navigate challenges, roll the dice, and shape your destiny. Will you emerge victorious or succumb to the twists of fate? 
The journey awaits! Choose wisely, and may the odds be in your favor.
          """)

# begin
start_game()