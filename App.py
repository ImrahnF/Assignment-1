'''
This is App.py and is the MAIN file that is considered the backbone of the entire game. This is where it begins and ends.
This file also grabs all the info needed from different Roles, and sends it to Game.py to play a challenge.

print_introduction()
- This is the very beginning. It will print the introduction by welcoming the user and starting the game.

print_header()
- this uses a premade design to print a visually appealing header, taking in a string parameter to use in the header

start_game()
- this simply starts the game and is only ever called once

'''

# variables and imports
import Game   # Import the Game module
import Role1  # Import the Role1 module
import Role2  # Import the Role2 module

# functions
def start_game():
    print_introduction()

    # The following are setting variables to allow the user to pick roles
    role = None
    role_choice = None
    role_choices = ['1', '2'] # 1 and 2 refer to roles 1 and 2

    print_header(f"Input [1] to play as [Jock] who excells at physical challenges\nInput [2] to play as [Smarty Pants] who excells at mind games")
    while role_choice not in role_choices:
        role_choice = input("-- Please input a role -- \n")
        
        if role_choice not in role_choices:
            print("Invalid input. Please select anything from the specified choices.")

    # Get game ready to start. Initialize everything.
    role_choice = int(role_choice) # the choice of the user, used to determine who is being played as

    # initialize the role selected
    if role_choice == 1:
        role = Role1.initialize_role()
    elif role_choice == 2:
        role = Role2.initialize_role()
    print(("You have picked: " + role["name"] + " as your role! May the odds be in your favour.\n"))
    
    # Game logic
    for i in range(1, 4): # This is the game's main loop in which it runs 3 challenges based on the role and challenge #.
        # play the challenge
        Game.play_challenge(role, i)

    # now that the 3 games are complete, we can retrieve the information of the game and updated attributes and determine the win/loss
    total_points = sum(value for key, value in role.items() if key != 'name') # this is the sum all of the attributes in the selected role
    FINAL_RESULT = Game.determine_OVERALL(total_points) # this returns WIN or LOSS depending on what was calculated
    print(f"\n{'─'*30}")
    print(f"YOU {FINAL_RESULT} WITH A TOTAL ATTRIBUTE SUM OF [{total_points}]")
    print(f"{'─'*30}")

def print_header(title):
    print(f"{'─'*30}")
    print(f"{title.upper()}")
    print(f"{'─'*30}\n")

def print_introduction():
    print("""  
            ▒▐█▒▐█▒▐█▀▀▒██░░░▒██░░░▒▐█▀▀█▌ 
            ▒▐████▒▐█▀▀▒██░░░▒██░░░▒▐█▄▒█▌ 
            ▒▐█▒▐█▒▐█▄▄▒██▄▄█▒██▄▄█▒▐██▄█▌

A mad scientist made a rip in the fabric of reality. This sends you across multiple dimensions, meeting different versions of the scientist.
You are to find and defeat the alternate versions of the scientist you meet by completeing all the tasks you have been given.
Each roll has it's own perks and downsides so pick carefully..
The success of your mission is determined by the success of the 3 realities you visit.
- If the sum of all your attributes are greater than 0, then you have won
- If they are less than or equal to 0, you lose.
          
Good luck!
          """)

# begin
start_game()