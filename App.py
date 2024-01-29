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
import Role3  # Import SPECIAL RANDOM ROLE module

import random

# functions
def start_game():
    # This is the very beginning. It will print the introduction by welcoming the user and starting the game.
    print_introduction()


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