import random

intelligence = 2
luck = 2

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

def generate_card():
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
    
    print_card(selected_rank, selected_suit)
    return [selected_rank, selected_suit, rank_value]
    
items = generate_card()
print(f"Rank: {[items[0]]} || Suit: {items[1]} || Value: {items[2]}")
