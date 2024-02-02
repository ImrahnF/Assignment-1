"""
Game Module

This module contains the game logic for the adventure game. It includes functions for playing challenges, determining outcomes, and managing role attributes.

Functions:
- play_challenge(role, challenge_number, print_function): Executes a challenge for the given role and prints relevant information.
- determine_outcome(roll_value, attribute_value): Determines the outcome based on the roll value and role attribute.
- update_attributes(role, outcome): Updates role attributes based on the outcome of a challenge.
"""
import random

# Challenge 1 winning criteria
W1 = [-8, 0] # W[0] and below is Crit win, and between [0] and [1] is a win
L1 = [1, 8] # L[1] and above is Crit loss, and between [0] and [1] is a loss
C1_RESULT = [-2, -1, 1, 2] # attribute points added or removed: crit loss, loss, win, crit win

# Challenge 2 winning criteria
W2 = []
L2 = []
C2_RESULT = []

# Challenge 3 winning criteria
W3 = []
L3 = []
C3_RESULT = []

# stats
global stats

############################# PLAY CHALLENGE #############################

def play_challenge(role, challenge_number):
    stats = role
    if role["name"] == "Barbarian":
        # challenge 1 is strength based
        if challenge_number == 1:
            stats["strength"] += role1_challenge1(challenge_number, role)
            print_attributes(stats)
        if challenge_number == 2:
            role1_challenge2(challenge_number, role)
            print_attributes(stats)

############################# Dice Roll #############################
def roll_dice():
    roll = (random.randint(1, 10))
    return roll

############################# Headers and Lines #############################
def print_header(title):
    print(f"{'─'*30}", end=f"\n{'='*30}\n")
    print(f"{title.upper()}")
    print(f"{'='*30}", end=f"\n{'─'*30}\n\n")

def print_attributes(s):
    print(f"{'─'*30}")
    print("~ UPDATED ATTRIBUTES ~")
    print(f"Name: [{s["name"]}]")
    print(f"Strength: [{s["strength"]}]")
    print(f"Dexterity: [{s["dexterity"]}]")
    print(f"Intelligence: [{s["intelligence"]}]")
    print(f"{'─'*30}\n")

def outcome_header(title):
    print(f"{'!'*40}")
    print(f"{title.upper()}")
    print(f"{'!'*40}\n")

def print_list(choices):
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

############################# Outcomes #############################
        
# This is the first [strength] challenge for both roles. Same criteria but different challenges

def determine_outcome1(value):
    if value <= W1[0]:
        return ["critical win", C1_RESULT[3]]
    elif W1[0] < value <= W1[1]:
        return ["win", C1_RESULT[2]]
    elif L1[0] <= value < L1[1]:
        return ["loss", C1_RESULT[1]]
    elif value >= L1[1]:
        return ["critical loss", C1_RESULT[0]]
    else:
        return "Outside specified ranges"

def determine_outcome2():
    pass

def determine_outcome3():
    pass

############################# Challenges #############################
def role1_challenge1(challenge_number, role):
    # starting variables
    hp = 20
    current_roll = 0
    
    # introduction
    print_header(f"challenge #{challenge_number} - goblin fight")
    print("Ahh! You meet a slimey goblin. In order to proceed you must defeat this monster! Here is how:")
    print_list(["The damange you deal = (number you roll * strength)", "[0] strength adds/removes nothing", "[-1], [-2] strength lessens that much damage done to the goblin" ,"You have 3 rolls"])

    # design of goblin introduction
    print(f"+{'-' * 30}+")
    print(f"Enemy: Goblin\nHealth: {hp}")
    print(f"+{'-' * 30}+")     

    # handle gameplay
    for i in range(1, 4):
        input("Input anything to roll: ")

        # calculate damage to deal
        current_roll = roll_dice()
        print(("You rolled a ["+str(current_roll)+"]"))
        print(("Your strength scaling adds/removes ["+str(role["strength"])+"]"))
        deal_damage = (current_roll + role["strength"])
        hp -= deal_damage

        # visualize damage
        print(f"+{'=' * 30}+")
        print(f"~Roll #{i} - {deal_damage} dmg done~")
        print(f"Goblin Health is now: {hp}")
        print(f"+{'=' * 30}+")

    # win/loss system
    outcomes = determine_outcome1(hp)
    outcome = f"{outcomes[0]} ~ [{outcomes[1]}] strength attribute point(s)"
    outcome_header(outcome)

    # return the attribute value to reweard or penalize player
    return outcomes[1]

def role1_challenge2(challenge_number, role):
    num = 100

    # introduction
    print_header(f"challenge #{challenge_number} - [CHALLENGE NAME]]")
    print("Introduction")
    print_list(["Rule", "rule", "rule"])

    # design of challenge introduction
    print(f"+{'-' * 30}+")
    print(f"Target: \nSTAT: {num}")
    print(f"+{'-' * 30}+")     

def role1_challenge3(challenge_number):
    pass

def role2_challenge1(challenge_number):
    pass

def role2_challenge2(challenge_number):
    pass

def role2_challenge3(challenge_number):
    pass