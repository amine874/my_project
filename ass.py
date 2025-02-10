import random

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def calculate_hand_value(hand):
    value = sum(card_values[card] for card in hand)
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(player, hand):
    print(f"{player} hand: {' '.join(hand)} - Total: {calculate_hand_value(hand)}")

def blackjack():
    deck = list(card_values.keys()) * 4
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    display_hand("Player", player_hand)
    print(f"Dealer's hand: {dealer_hand[0]} ?")

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to hit (h) or stand (s)? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            display_hand("Player", player_hand)
        elif action == 's':
            break
    
    if calculate_hand_value(player_hand) > 21:
        print("Player busts! You lose!")
        return

    print(f"\nDealer's hand: {' '.join(dealer_hand)} - Total: {calculate_hand_value(dealer_hand)}")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand("Dealer", dealer_hand)
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if dealer_value > 21:
        print("Dealer busts! You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie! (Push)")

blackjack()
