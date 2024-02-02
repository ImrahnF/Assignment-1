"""
Game Module

This module contains the game logic for the adventure game. It includes functions for playing challenges, determining outcomes, and managing role attributes.

Functions:
- play_challenge(role, challenge_number, print_function): Executes a challenge for the given role and prints relevant information.
- determine_outcome(roll_value, attribute_value): Determines the outcome based on the roll value and role attribute.
- update_attributes(role, outcome): Updates role attributes based on the outcome of a challenge.
"""
import random

def play_challenge(role, challenge_number):
    #print(("Role: " + role["name"] + " || Challenge #" + str(challenge_number)))
    if role["name"] == "Role1":
        if challenge_number == 1:
            role1_challenge1(challenge_number, role)
        elif challenge_number == 2:
            role1_challenge2(challenge_number)
        elif challenge_number == 3:
            role1_challenge3(challenge_number)
    elif role["name"] == "Role2":
        if challenge_number == 1:
            role2_challenge1(challenge_number)
        elif challenge_number == 2:
            role2_challenge2(challenge_number)
        elif challenge_number == 3:
            role2_challenge3(challenge_number)

def roll_dice():
    roll = (random.randint(1, 12))
    return roll

def print_header(title):
    print(f"{'='*30}")
    print(f"{title.upper()}")
    print(f"{'='*30}\n")

def print_header2(title):
    print(f"{'!'*30}")
    print(f"{title.upper()}")
    print(f"{'!'*30}\n")

def print_choices(choices):
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

############################# Challenges #############################
def role1_challenge1(challenge_number, role):
    # starting variables
    hp = 20
    current_roll = 0
    
    # introduction
    print_header(f"challenge #{challenge_number} - goblin fight")
    print("Ahh! You meet a slimey goblin. In order to proceed you must defeat this monster! Here is how:")
    print_choices(["The damange you deal = (number you roll * strength)", "0 strength adds/removes nothing", "-1, -2 strength lessens that much damage done to the goblin" ,"You have 3 rolls"])

    # design of goblin introduction
    print(f"+{'-' * 30}+")
    print(f"Enemy: Goblin\nHealth: {hp}")
    print(f"+{'-' * 30}+")     

    # handle gameplay
    for i in range(1, 4):
        input("Input anything to roll: ")

        # calculate damage to deal
        current_roll = roll_dice()
        print(current_roll)
        print(role["strength"])
        deal_damage = (current_roll + role["strength"])
        hp -= deal_damage

        # visualize damage
        print(f"+{'=' * 30}+")
        print(f"Roll #{i} - {deal_damage} dmg done")
        print(f"Goblin Health is now: {hp}")
        print(f"+{'=' * 30}+")

    # win/loss system
    if hp <= 0:
        print_header2("winner")
    else:
        print_header2("loser")


def role1_challenge2(challenge_number):
    pass

def role1_challenge3(challenge_number):
    pass

def role2_challenge1(challenge_number):
    pass

def role2_challenge2(challenge_number):
    pass

def role2_challenge3(challenge_number):
    pass