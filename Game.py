"""
Game Module

This module contains the game logic for the adventure game. It includes functions for playing challenges, determining outcomes, and managing role attributes.

Functions:
- play_challenge(role, challenge_number, print_function): Executes a challenge for the given role and prints relevant information.
- determine_outcome(roll_value, attribute_value): Determines the outcome based on the roll value and role attribute.
- update_attributes(role, outcome): Updates role attributes based on the outcome of a challenge.
"""
import random
ATTRIBUTE_RESULT = [-2, -1, 1, 2] # attribute points added or removed: crit loss, loss, win, crit win

# Challenge 1 winning criteria
W1 = [-8, 0] # W[0] and below is Crit win, and between [0] and [1] is a win
L1 = [1, 8] # L[1] and above is Crit loss, and between [0] and [1] is a loss

# Challenge 2 winning criteria
W2 = [100, 75] # W[1] and above is Crit win, and between [0] and [1] is a win
L2 = [50, 25] # L[1] and below is loss, and between [0] and [1] is a loss

# Challenge 3 winning criteria

# stats
global stats

############################# PLAY CHALLENGE #############################

def play_challenge(role, challenge_number):
    stats = role
    # challenge 1 is strength based
    if challenge_number == 1:
        stats["strength"] += challenge1(challenge_number, stats)
        print_attributes(stats)
        continue_header()
        
    if challenge_number == 2:
        result = challenge2(challenge_number, stats)
        stats["dexterity"] += result
        stats["intelligence"] += result
        print_attributes(stats)
        continue_header()
    
    if challenge_number == 3:
        stats["luck"] += challenge3(challenge_number, stats)
        print_attributes(stats)
        continue_header()

############################# Outcomes #############################

def determine_OVERALL():
    return "WIN"

# This is the first [strength] challenge
def determine_outcome1(value):
    if value <= W1[0]:
        return ["critical win", ATTRIBUTE_RESULT[3]]
    elif W1[0] < value <= W1[1]:
        return ["win", ATTRIBUTE_RESULT[2]]
    elif L1[0] <= value < L1[1]:
        return ["loss", ATTRIBUTE_RESULT[1]]
    elif value >= L1[1]:
        return ["critical loss", ATTRIBUTE_RESULT[0]]
    else:
        return "Outside specified ranges"
    
# This is the second [dexterity/intelligence] challenge
def determine_outcome2(encrypted_message, decrypted_message):
    inp = input("\t→ Decode the message:")

    # Count the number of correct characters
    correct_characters = sum(char1 == char2 for char1, char2 in zip(inp, decrypted_message))

    # Calculate the percentage of correct characters
    total_characters = len(decrypted_message) 
    accuracy_percentage = int((correct_characters / total_characters) * 100)

    # Display the result as a percentage
    print(f"Correct Characters: {correct_characters}/{total_characters} ({accuracy_percentage}%)\n")

    if accuracy_percentage >= W2[1]:
        return ["critical win", ATTRIBUTE_RESULT[3]]
    elif W2[1] > accuracy_percentage >= L2[0]:
        return ["win", ATTRIBUTE_RESULT[2]]
    elif L2[0] > accuracy_percentage >= L2[1]:
        return ["loss", ATTRIBUTE_RESULT[1]]
    elif accuracy_percentage < L2[1]:
        return ["critical loss", ATTRIBUTE_RESULT[0]]
    else:
        return "Outside specified ranges"

def determine_outcome3():
    pass

############################# Challenges #############################
def challenge1(challenge_number, stats):
    # starting variables
    hp = 20
    current_roll = 0
    
    # introduction
    print_header(f"challenge #{challenge_number} - Gladiator Goblin")
    print("Ahh! You meet a slimey goblin. In order to proceed you must defeat this monster! Here is how:")
    print_list(["The damange you deal = (number you roll * strength)", "[0] strength adds/removes nothing", "[-1], [-2] strength lessens that much damage done to the goblin" ,"You have 3 rolls"])

    # design of goblin introduction
    print(f"+{'-' * 30}+")
    print(f"Enemy: Goblin\nHealth: {hp}")
    print(f"+{'-' * 30}+")     

    # handle gameplay
    for i in range(1, 4):
        input("\t→ Input anything to roll: ")

        # calculate damage to deal
        current_roll = roll_dice()
        print(("You rolled a ["+str(current_roll)+"]"))
        print(("Your strength scaling adds/removes ["+str(stats["strength"])+"]\n"))
        deal_damage = (current_roll + stats["strength"])
        hp -= deal_damage

        # visualize damage
        print(f"+{'=' * 30}+")
        print(f"~Roll #{i} - {deal_damage} dmg done~")
        print(f"→Goblin Health is now: {hp}")
        print(f"+{'=' * 30}+\n")

    # win/loss system
    outcomes = determine_outcome1(hp)
    outcome = f"{outcomes[0]} ~ [{outcomes[1]}] strength attribute point(s)"
    outcome_header(outcome)

    # return the attribute value to reweard or penalize player
    return outcomes[1]

def challenge2(challenge_number, stats):
    # Define character sets
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    symbols = "~ #^*_/<>|`"

    # introduction
    print_header(f"challenge #{challenge_number} - [Cryptic Conundrum]")
    print("You stumble upon an ancient script, seemingly a coded message. Your intelligence and dexterity will aid in deciphering it.")
    print_list(["There is a series of characters and symbols, you must give me the message without the symbols",
                "# of symbols scale off of dexterity | # of characters scale off of intelligence",
                "Your job is to input every NUMBER (0-9) and LETTER (Aa-Zz) you see IN ORDER. Do this correctly and you win!",
                "Do NOT input any symbols (~ #^*_/<>|`).",
                "Spaces do not count as a character.\n"])

    input("Input anything to roll the dice and generate the message: ")
    roll = roll_dice()

    # calculate number of characters based off of intelligence attribute
    num_characters = (roll - stats["intelligence"]) + 4

    # calculate number of symbols based off of dexterity attribute
    if stats["dexterity"] < 0: 
        num_symbols = (roll * abs(stats["dexterity"])) + 4
    else: 
        num_symbols = (roll - abs(stats["dexterity"])*2) + 4

    # Generate encrypted message
    encrypted_message = ''.join(random.choice(chars) for _ in range(num_characters))
    encrypted_message += ''.join(random.choice(symbols) for _ in range(num_symbols))

    # Shuffle the encrypted message
    encrypted_message_list = list(encrypted_message)
    random.shuffle(encrypted_message_list)
    encrypted_message = ''.join(encrypted_message_list)

    # Decrypt message by removing symbols
    decrypted_message = encrypted_message.translate(str.maketrans("", "", symbols))

    # design of challenge introduction
    print(f"+{'-' * 30}+")
    print(f"You have rolled a [{roll}]. Here is the message:\n")
    print(f"Chars: {num_characters}|Symbols: {num_symbols}")
    print("Message:", encrypted_message)
    print(f"+{'-' * 30}+\n")  

    # win/loss system
    outcomes = determine_outcome2(encrypted_message, decrypted_message)
    outcome = f"{outcomes[0]} ~ [{outcomes[1]}] dexterity/intelligence attribute point(s)"
    outcome_header(outcome)

    # return the attribute value to reweard or penalize player
    return outcomes[1]
        
def challenge3(challenge_number, stats):
    return 5

############################# Dice Roll #############################
def roll_dice():
    roll = (random.randint(1, 10))
    return roll

############################# Headers and Lines #############################
def continue_header():
    input("\t→ Input anything to continue:")

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
    print(f"Luck: [{s["luck"]}]")
    print(f"{'─'*30}\n")

def outcome_header(title):
    print(f"{'!'*40}")
    print(f"{title.upper()}")
    print(f"{'!'*40}\n")

def print_list(choices):
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
