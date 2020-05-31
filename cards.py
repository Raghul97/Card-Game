import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for value in values for suit in suits]

    def __repr__(self):
        return 'Deck of {} cards'.format(len(self.cards))

    def count(self):
        return len(self.cards)

    def _deal(self, remove):
        counts = self.count()
        actual = min(counts, remove)
        dealing =[]
        n = 0
        if counts == 0:
            raise ValueError('All cards have been dealt')
        else:
            while n < actual:
                dealing.append(self.cards.pop())
                n += 1
            return dealing

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError('Only full decks can be shuffled')
        return self.cards

    def deal_card(self):
        cards = self._deal(1)[0]
        return cards

    def deal_hand(self, remove):
        cards = self._deal(remove)
        return cards


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    card = deck.deal_card()
    print(card)
    hand = deck.deal_hand(45)
    print(hand)
    card = deck.deal_card()
