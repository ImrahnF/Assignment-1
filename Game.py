'''
This is Game.py which handles all the games/challenges and it's logic. This is where most of the work happens in the entire program.
There are many functions here that work together and are very modular, so adding and removing things are simple.

play_challenge()
- this takes in 2 parameters pass through the App.py, which passes the selected roll and the round number and uses "global stats" as a placeholder
- it then updates whatever stat is used in the game

challenge1(), challenge2(), challenge3()
- these simply play the selected challege and pass through the challenge number and the newly updated "stats" varaible. This returns a value to update the attribute

print_attributes()
- this is a premade header that simply displays the current values of each attribute

continue_header()
- just a random header that is an input used to allow the player to continue on their own pace

determine_OVERALL()
- used to calculate whether the player wins or loses at the end

determine_outcome1(), determine_outcome2(), determine_outcome3()
- these determine the outcome of each challenge and return what kind of win and how many attribute points to reward

print_header()
- this is a premade header used to display visually appealing text

print_list()
- this is a premade header used to display visually appealing listed text

outcome_header()
- used to print out the outcome of each challenge and the reward

roll_dice()
- simply rolls a dice and returns the number

print_card()
- this displays a nice visual of an actual card with the number and suit

generate__random_card()
- this uses the predefined suits and ranks to generate a random card. It takes in a parameter to determine if it is a player or the program taking the card
- if its a player, if they pick an Ace, then they are able to pick if it has a value of 1 or 11. if its the program its random
- it then returns the card information [selected_rank, selected_suit, rank_value]

toss()
- a special dice roll for only the third challenge. it's range is only 0-1

show_sets()
- this displays the sets the player and dealer have, and allows for them to see the total value of their cards (which is important)
'''
import random
ATTRIBUTE_RESULT = [-2, -1, 1, 2] # attribute points added or removed: crit loss, loss, win, crit win

# this is a placeholder for the "Role" selected back in App.py
global stats

############################# PLAY CHALLENGE #############################

def play_challenge(role, challenge_number):
    stats = role # placeholder role
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

def determine_OVERALL(sum):
    if sum >= 0:
        return "WIN"
    else:
        return "LOSE"

# This is the first [strength] challenge
def determine_outcome1(value):
    if value <= -8:
        return ["critical win", ATTRIBUTE_RESULT[3]]
    elif -8 < value <= 0:
        return ["win", ATTRIBUTE_RESULT[2]]
    elif 1 <= value < 8:
        return ["loss", ATTRIBUTE_RESULT[1]]
    elif value >= 8:
        return ["critical loss", ATTRIBUTE_RESULT[0]]
    else:
        return "Outside specified ranges"    
# This is the second [dexterity/intelligence] challenge
def determine_outcome2(encrypted_message, decrypted_message):
    inp = input("\t→ Decode the message:") # this allows the user to move at their own pace

    # Count the number of correct characters
    correct_characters = sum(char1 == char2 for char1, char2 in zip(inp, decrypted_message))

    # Calculate the percentage of correct characters
    total_characters = len(decrypted_message) 
    accuracy_percentage = int((correct_characters / total_characters) * 100)

    # Display the result as a percentage
    print(f"Correct Characters: {correct_characters}/{total_characters} ({accuracy_percentage}%)\n")

    if accuracy_percentage >= 75:
        return ["critical win", ATTRIBUTE_RESULT[3]]
    elif 75 > accuracy_percentage >= 50:
        return ["win", ATTRIBUTE_RESULT[2]]
    elif 50 > accuracy_percentage >= 25:
        return ["loss", ATTRIBUTE_RESULT[1]]
    elif accuracy_percentage < 25:
        return ["critical loss", ATTRIBUTE_RESULT[0]]
    else:
        return "Outside specified ranges"

def determine_outcome3(goal, player_set, dealer_set):
    # determine if it's a win, loss, tie, or continue playing.
    # here we determine the difference. closer to the goal is a win, but over is a lose
    player_points = abs(goal - sum(item[2] for item in player_set))
    dealer_points = abs(goal - sum(item[2] for item in dealer_set))
        
    # Determine who is closer to the goal
    if player_points < dealer_points:
         print(f"You are closer to the goal by [{player_points}] points.")
         if player_points <= 5:
             # difference is 5 or less, therefore critical win
            return ["critical win", ATTRIBUTE_RESULT[3]]
         else:
             # difference is greater than 5, therefore regular win
             return ["win", ATTRIBUTE_RESULT[2]]
    elif dealer_points < player_points:
        print(f"Dealer is closer to the goal by {dealer_points} points.")
        if dealer_points <= 5:
            # dealer is 5 or less away from goal, therefore ciritical loss
            return ["critical loss", ATTRIBUTE_RESULT[0]]
        else:
            # over 5 points away, regular loss
            return ["loss", ATTRIBUTE_RESULT[1]]
    else:
        print("Both are equally close to the goal.")
        return ["tie", 0] # if it's a tie, just leave as is

########################################################### CHALLENGE 1 ###########################################################
def challenge1(challenge_number, stats):
    # starting variables
    hp = 20
    current_roll = 0
    
    # introduction
    print_header(f"challenge #{challenge_number} - Gladiator Goblin")
    print("Ahh! You meet a slimey goblin. In order to proceed you must defeat this monster! Here is how:")
    print_list(["The damange you deal = (number you roll * strength)", "[0] strength adds/removes nothing", 
                "[-1], [-2] strength lessens that much damage done to the goblin" ,
                "You have 3 rolls, each roll can be within a range of 1-10"])

    # handle gameplay
    for i in range(1, 4):
        input("\t→ Input anything to roll: ")

        # calculate damage to deal
        current_roll = roll_dice()
        print(("You rolled a ["+str(current_roll)+"]"))
        print(("Your strength scaling adds/removes ["+str(stats["strength"])+"]\n"))

        # calculate damage to deal and deal it
        deal_damage = (current_roll + stats["strength"])
        hp -= deal_damage

        # visualize damage
        print(f"+{'=' * 30}+")
        print(f"~Roll #{i} - {deal_damage} dmg done~")
        print(f"→Goblin Health is now: {hp}")
        print(f"+{'=' * 30}+\n")

    # win/loss system
    outcomes = determine_outcome1(hp) # this returns the outcome (eg. "critical win") and attribute points to be rewarded
    outcome = f"{outcomes[0]} ~ [{outcomes[1]}] strength attribute point(s)"
    outcome_header(outcome)

    # return the attribute value to reweard or penalize player
    return outcomes[1]
########################################################### CHALLENGE 2 ###########################################################
def challenge2(challenge_number, stats):
    # Define character sets to be used
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    symbols = "~ #^*_/<>|`"

    # introduction
    print_header(f"challenge #{challenge_number} - [Cryptic Conundrum]")
    print("You stumble upon an ancient script, seemingly a coded message. Your intelligence and dexterity will aid in deciphering it.")
    print_list(["There is a series of characters and symbols, you must give me the message without the symbols",
                "Each roll can be wihtin the range of 1-11",
                "# of symbols scale off of dexterity and roll# | # of characters scale off of intelligence and roll#",
                "Your job is to input every NUMBER (0-9) and LETTER (Aa-Zz) you see IN ORDER. Do this correctly and you win!",
                "Do NOT input any symbols (~ #^*_/<>|`).",
                "Spaces do not count as a character.\n"])

    input("Input anything to roll the dice and generate the message: ")
    roll = roll_dice() # rolls the dice

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
########################################################### CHALLENGE 3 ###########################################################
# card ranks
ranks = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# card suits, simply used for the visuals
suits = ['♠', '♥', '♦', '♣']

def print_card(rank, suit):
    print("+------+") 
    print(f"| {suit}  {rank} |")
    print("|      |")
    print(f"|   {rank}  |")
    print("|      |")
    print(f"| {rank}  {suit} |")
    print("+------+")

def generate__random_card(dealer): # dealer == False means its a player and we allow player to chose. If it's True, just pick either 1 or 11
    selected_rank = random.choice(list(ranks.keys())) # selects random rank
    selected_suit = random.choice(suits) # selects random suit
    rank_value = 0 # a placeholder value for the selected card's value

    # If the selected rank is 'J', 'Q', 'K', or 'A', print the corresponding value
    if selected_rank in ['J', 'Q', 'K', 'A']:
        # allow the Ace to be an 11 or 1 if its a player's card
        if selected_rank == 'A':
            if dealer == False:
                choice = input("\nYou picked up an Ace! Input 1 to use as a [1] | Input anything else to use as an [11]: ")
                if choice == "1":
                    print("You picked a [1]")
                    #print("Rank value: 1")
                    rank_value = 1
                else:
                    print("You picked an [11]")
                    #print("Rank value: 11")
                    rank_value = 11
            else:
                # it's the dealer's card so they pick a random value for Ace
                x = random.randint(0, 1)
                if x == 0:
                    rank_value = 1
                else:
                    rank_value = 11

        # if it's not an Ace, proceed normally
        else:
            #print(f"Rank value: {ranks[selected_rank]}")
            rank_value = ranks[selected_rank]
    # for every numerical card
    else:
        #print(f"Rank value: {selected_rank}")
        rank_value = ranks[selected_rank]
    
    # print_card(selected_rank, selected_suit)
    return [selected_rank, selected_suit, rank_value]

def challenge3(challenge_number, stats):
    # starting values
    goal = 40 # traditional blackjack is 21, but this is my own version of blackjack!
    turns = 5 # the amount of turns to be played
    current_turn = 1 # the current turn
    luck = stats["luck"] # grab the luck attribute and make it its own variable for easy access

    running = True # determines if the game should continue or not

    # the player and dealer deck
    player_set = []
    dealer_set = []

    # the dice roll for this specific gamemode
    def toss():
        return random.randint(0, 1) # 0 = hold, 1 = hit
    
    def show_sets():
        print(f"{'─'*40}")
        print(f"→ You have [{len(player_set)}] cards that sum up to [{sum(item[2] for item in player_set)}].")
        print(f"→ Dealer has [{len(dealer_set)}] cards that sum up to [{sum(item[2] for item in dealer_set)}].")
        print(f"{'─'*40}\n")

    # introduction
    print_header(f"challenge #{challenge_number} - [Mystical Forty]")
    print("You have been trapped by a renown trickster. You are tasks with competing against him in his very own version of Blackjack! Here are the rules:")
    print_list(["Both you and the trickster (dealer) have cards that add up to 40", 
                "K, Q, J are valued at 10 points, the Ace card is valued at your choice of 1 or 11 points." ,
                "You both start with 2 cards and play 5 rounds",
                "The person at the end of the 5 rounds closer to 40 wins!",
                "Your dice roll is ranged from 0-1. If someone rolls a [1], they hit (take the next card). If a [0] is rolled, then you hold on to your deck",
                "[1+] luck gives you a lucky Ace to start off with. You can pick to have it value at 1 or 11",
                "[2+] luck allows for the previous, as well as 'cheating' in which you are able to peek the next card and chose to keep it or give it to the dealer."])

    # initialize the game before playing
    if luck >= 1:
       # if luck is 1+, simply add bonus card + random card. (2+ allows higher chance to 'peek' the next card)
       player_set.append(['A', '♠', 11])
       player_set.append(generate__random_card(False))
    else:
        # any other amount generates a random starting set of 2
        player_set.append(generate__random_card(False))
        player_set.append(generate__random_card(False))

    # add the 2 cards for the dealer's deck
    dealer_set.append(generate__random_card(True))
    dealer_set.append(generate__random_card(True))
    
    print(f"{'─'*30}")
    print(f"Welcome to twisted Blackjack! The rules are different here..\nYou have [{luck}] luck points.")
    print(f"{'─'*30}")

    # Summing the third item of each dictionary to get total value of cards
    print(f"→ You start with [{len(player_set)}] cards that sum up to [{sum(item[2] for item in player_set)}]")
    print(f"Dealer starts with [{len(dealer_set)}] cards that sum up to [{sum(item[2] for item in dealer_set)}]")
    print(f"{'─'*30}\n")

    input("\t→ Input anything to start: ")

    # play blackjack!
    while running == True:
        current_turn += 1

        # deal dealer's card
        roll1 = toss()
        print(f"{'❖'*30}")
        if roll1 == 0:
            print(f"Dealer tossed the dice and got a [{roll1}]. He holds...")
        else:
            next = generate__random_card(True) # since he hits, he takes the NEXT random card
            print(f"Dealer tossed the dice and got a [{roll1}]. He hits a {next[0]} of {next[1]} and adds it to his deck")
            dealer_set.append(next)
            show_sets()
        print(f"{'❖'*30}\n")

        # deal player's card
        roll2 = toss()
        input("\t→ Input anything to toss your dice: ")
        print(f"{'❖'*30}")
        if roll2 == 0:
            print(f"→ You tossed the dice and got a [{roll2}]. You hold...")
        else:
            next = generate__random_card(False) # generate a random card, allows the user to view it provided they have enough luck points
            print(f"→ You tossed the dice and got a [{roll2}]!\n")
            if luck >= 2:
                # Player is lucky, they can view the next card
                print(f"I'm feeling lucky!! With your luck points being {luck}, you are able to preview the next card before you hit or hold!")
                print_card(next[0], next[1])

                # player has luck points. they can sabotage the dealer!
                choice = input("You can chose to hit, or add the card to the dealer's deck.\nInput 1 to hit, anything else to give to the dealer: ")
                if choice == "1":
                    # player hits
                    print(f"→ You hit!")
                    player_set.append(next)
                else:
                    # player gives to dealer
                    print("→ You gave the card to the dealer.\n")
                    dealer_set.append(next)
            else:
                # not enough luck, play normally
                print(f"→ You tossed the dice and got a [{roll2}]. You hit a {next[0]} of {next[1]} and add it to your deck")
                player_set.append(next)
        print(f"{'❖'*30}\n")

        if current_turn < turns:
            # we have more turns, loop back
            print(f"{'─'*30}")
            print(f"~~~~ End of turn #{current_turn} ~~~~")
            show_sets()
            input(f"\t→ Input anything to proceed to turn #{(current_turn+1)}\n")
        else:
            running = False # essentially closes the challenge

    # win/loss system
    outcomes = determine_outcome3(goal, player_set, dealer_set)
    outcome = f"{outcomes[0]} ~ [{outcomes[1]}] luck attribute point(s)"
    outcome_header(outcome)

    # return the attribute value to reweard or penalize player
    return outcomes[1]
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
