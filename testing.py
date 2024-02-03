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

def generate__random_card(start):
    selected_rank = random.choice(list(ranks.keys()))
    selected_suit = random.choice(suits)
    rank_value = 0

    # If the selected rank is 'J', 'Q', 'K', or 'A', print the corresponding value
    if selected_rank in ['J', 'Q', 'K', 'A']:
        # allow the Ace to be an 11 or 1
        if selected_rank == 'A':
            choice = input("Input 1 to use as a [1] | Input anything else to use as an [11]: ")
            if choice == "1":
                print("You picked a [1]")
                #print("Rank value: 1")
                rank_value = 1
            else:
                print("You picked an [11]")
                #print("Rank value: 11")
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
    
items = generate__random_card(luck)
print(f"Rank: {[items[0]]} || Suit: {items[1]} || Value: {items[2]}")

def play_blackjack():
    running = True
    player_set = [{'A': 11}]
    next_card = []

    # if luck is 2, keep playerset + show next card
    # if luck is 1, keep playerset
    # if luck is 0 to -2, clear playerset + add random cards

    '''
    # Print the information of the first card
    first_card = player_set[0]
    for rank, value in first_card.items():
        print(f"First Card: {rank} - Value: {value}")
    '''


play_blackjack()