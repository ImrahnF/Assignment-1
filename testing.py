import random

luck = 2
# [2] luck means you start with a card + Ace (value = 11) and know the next card is.
# [1] luck means you start with card + Ace (value = 11)
# [0 to -2] is just regular blackjack

ranks = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

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
    selected_rank = random.choice(list(ranks.keys())) # this is simply visual
    selected_suit = random.choice(suits)
    rank_value = 0

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

def play_blackjack():
    # the dice roll for this specific gamemode
    def toss():
        return random.randint(0, 1) # 0 = hold, 1 = hit

    # starting values
    goal = 40 # traditional blackjack is 21, but this is my own version of blackjack!
    running = True

    # the player and dealer deck
    player_set = []
    dealer_set = []

    # this is a placeholder to allow player to view the next card
    next_card = []

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

    #print(f"Rank: {player_set[0]['Rank']} | Suit: {player_set[0]['Suit']} | Value: {player_set[0]['Value']}")
    
    print(f"{'─'*30}")
    print(f"Welcome to twisted Blackjack! The rules are different here..\nYou have [{luck}] luck points.")
    print(f"{'─'*30}\nHere is your starting deck:")
    print(player_set, "\n")

    # play blackjack!
    while running == True:
        # Summing the third item of each dictionary to get total value of cards
        print(f"You start with [{len(player_set)}] cards that sum up to [{sum(item[2] for item in player_set)}]")
        print(f"Dealer starts with [{len(dealer_set)}] cards that sum up to [{sum(item[2] for item in dealer_set)}]")
        print(f"{'─'*30}\n")

        # deal dealer's card
        roll1 = toss()
        print(f"{'~'*30}")
        if roll1 == 0:
            print(f"Dealer tossed the dice and got a [{roll1}]. He holds...")
        else:
            next = generate__random_card(True) # since he hits, he takes the random card
            print(f"Dealer tossed the dice and got a [{roll1}]. He hits a {next[0]} of {next[1]} and adds it to his deck")
            dealer_set.append(next)
            print(dealer_set)
            print(f"Dealer now has [{len(dealer_set)}] cards that sum up to [{sum(item[2] for item in dealer_set)}]")
        print(f"{'~'*30}\n")

        # deal player's card
        roll2 = toss()
        if roll2 == 0:
            print(f"→ You tossed the dice and got a [{roll2}]. You hold...")
        else:
            next = generate__random_card(False)
            print(f"→ You tossed the dice and got a [{roll2}]!\n")
            if luck >= 2:
                # Player is lucky, they can view the next card
                print(f"I'm feeling lucky!! With your luck points being {luck}, you are able to preview the next card before you hit or hold!")
                print_card(next[0], next[1])

                # player has luck points. they can sabotage the dealer!
                choice = input("You can chose to hit, or add the card to the dealer's deck.\nInput 1 to hold, anything else to give to the dealer: ")
                if choice == "1":
                    # player hits
                    print(f"→ You hit!")
                    player_set.append(next)
                    print(f"You now have [{len(player_set)}] cards that sum up to [{sum(item[2] for item in player_set)}]")
                else:
                    # player gives to dealer
                    print("→ You gave the card to the dealer.\n")
                    dealer_set.append(next)
                    print(f"Dealer now has [{len(dealer_set)}] cards that sum up to [{sum(item[2] for item in dealer_set)}]")
            else:
                # not enough luck, play normally
                print(f"→ You tossed the dice and got a [{roll2}]. You hit.")
                player_set.append(next)
                print(f"You now have [{len(player_set)}] cards that sum up to [{sum(item[2] for item in player_set)}]")
        
        break

play_blackjack()