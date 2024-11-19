suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
deck = []

for suit in suits:
    for rank in ranks:
        card = (rank, suit)
        deck.append(card)

def cards(n):
    selected_card = "".join(deck[n])
    print(selected_card)

if __name__ == "__main__":
    cards(0)
    cards(34)