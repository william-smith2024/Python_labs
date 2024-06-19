import random
from collections import Counter

# Initialize deck
suits = ["hearts", "diamonds", "spades", "clubs"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
rank_values = {r: i for i, r in enumerate(ranks, 2)}

# Function to evaluate hand strength
def evaluate_hand(cards):
    # Helper function to check for flush
    def is_flush(cards):
        suits = [card.split(' of ')[1] for card in cards]
        return len(set(suits)) == 1
    
    # Helper function to check for straight
    def is_straight(cards):
        card_ranks = sorted([rank_values[card.split(' of ')[0]] for card in cards])
        return card_ranks == list(range(card_ranks[0], card_ranks[0] + 5))
    
    # Get counts of each rank
    ranks_count = Counter([card.split(' of ')[0] for card in cards])
    counts = sorted(ranks_count.values(), reverse=True)
    
    # Determine hand strength
    if is_straight(cards) and is_flush(cards):
        return (8, max(ranks_count, key=rank_values.get))  # Straight flush
    elif counts == [4, 1]:
        return (7, ranks_count.most_common(1)[0][0])  # Four of a kind
    elif counts == [3, 2]:
        return (6, ranks_count.most_common(1)[0][0])  # Full house
    elif is_flush(cards):
        return (5, sorted(ranks_count, key=rank_values.get, reverse=True))  # Flush
    elif is_straight(cards):
        return (4, max(ranks_count, key=rank_values.get))  # Straight
    elif counts == [3, 1, 1]:
        return (3, ranks_count.most_common(1)[0][0])  # Three of a kind
    elif counts == [2, 2, 1]:
        return (2, ranks_count.most_common(2))  # Two pair
    elif counts == [2, 1, 1, 1]:
        return (1, ranks_count.most_common(1)[0][0])  # One pair
    else:
        return (0, sorted(ranks_count, key=rank_values.get, reverse=True))  # High card

# Function to determine the winner
def determine_winner(score1, score2):
    if score1 > score2:
        return "Player 1 wins!"
    elif score1 < score2:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

# Function to display the current state of the game
def display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips):
    print("Player 1's hand:", player1_hand)
    print("Player 2's hand:", player2_hand)
    print("Community cards:", community_cards)
    print(f"Player 1's chips: {player1_chips}")
    print(f"Player 2's chips: {player2_chips}")
    print()

# Function to simulate a simple poker game
def texas_holdem():
    player1_chips = 500
    player2_chips = 500
    total_pot = 0

    # Function to handle wagering
    def wager():
        nonlocal player1_chips, player2_chips, total_pot
        wager_amount = int(input("Enter the wager amount: "))
        player1_chips -= wager_amount
        player2_chips -= wager_amount
        total_pot += wager_amount * 2

    # Prompt Player 1 to initialize deck and shuffle
    input("Press Enter to initialize the deck and shuffle it...")
    deck = [rank + ' of ' + suit for suit in suits for rank in ranks]
    random.shuffle(deck)
    print("Deck shuffled!")

    # Initial wager
    wager()
    display_game_state([], [], [], player1_chips, player2_chips)

    # Prompt Player 1 to deal initial cards
    input("Press Enter to deal two cards to each player and three community cards...")
    player1_hand = [deck.pop(), deck.pop()]
    player2_hand = [deck.pop(), deck.pop()]
    community_cards = [deck.pop() for _ in range(3)]
    print("Initial cards dealt!")
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)

    # Wager after initial deal
    wager()
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)

    # Prompt Player 1 to deal the fourth community card
    input("Press Enter to deal the fourth community card...")
    community_cards.append(deck.pop())
    print("Fourth community card dealt!")
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)

    # Wager after fourth community card
    wager()
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)

    # Prompt Player 1 to deal the fifth community card
    input("Press Enter to deal the fifth community card...")
    community_cards.append(deck.pop())
    print("Fifth community card dealt!")
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)

    # Wager after fifth community card
    wager()
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)

    # Combine player hands with community cards
    player1_combined = player1_hand + community_cards
    player2_combined = player2_hand + community_cards

    # Evaluate hands
    player1_score = evaluate_hand(player1_combined)
    player2_score = evaluate_hand(player2_combined)

    # Determine the winner
    winner = determine_winner(player1_score, player2_score)

    # Update chips based on the winner
    if winner == "Player 1 wins!":
        player1_chips += total_pot
    elif winner == "Player 2 wins!":
        player2_chips += total_pot

    # Display final results
    print("\n--- Final Results ---")
    display_game_state(player1_hand, player2_hand, community_cards, player1_chips, player2_chips)
    print("Player 1's combined hand:", player1_combined)
    print("Player 2's combined hand:", player2_combined)
    print("Winner:", winner)
    print(f"Total pot: {total_pot}")

# Play a game
texas_holdem()