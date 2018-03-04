class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, card):
        return self.rank == card.rank and self.suit == card.suit
