from cards import Card, Deck
import unittest


class Testing(unittest.TestCase):
    def setUp(self):
        self.player = Card('Hearts', 'A')
        self.playerone = Deck()

    def test_suit(self):
        self.assertEqual(self.player.suit, 'Hearts')

    def test_suit_value(self):
        self.assertEqual(self.player.value, 'A')

    def test_represent_card(self):
        self.assertEqual(repr(self.player), 'A of Hearts')

    def test_tot_cards(self):
        self.assertEqual(len(self.playerone.cards), 52)

    def test_represent_deck(self):
        self.assertEqual(repr(self.playerone), 'Deck of 52 cards')

    def test_count(self):
        self.assertEqual(self.playerone.count(), 52)

    def test_shuffle(self):
        self.assertEqual(len(self.playerone.shuffle()), 52)
        self.assertNotEqual(self.playerone.cards[0:4], self.playerone.shuffle()[0:4])

    def test_deal_card(self):
        popped = self.playerone.cards[-1]
        dealt = self.playerone.deal_card()
        self.assertEqual(dealt, popped)
        self.assertEqual(self.playerone.count(), 51)

    def test_deal_hand(self):
        popped = self.playerone.cards[-1:-11:-1]
        dealt = self.playerone.deal_hand(10)
        self.assertEqual(dealt, popped)
        self.assertEqual(self.playerone.count(), 42)

    def test_add_card_removal(self):
        with self.assertRaises(ValueError):
            self.playerone.deal_hand(52)
            self.playerone.deal_card()

    def test_full_deck_shuffle(self):
        with self.assertRaises(ValueError):
            self.playerone.deal_card()
            self.playerone.shuffle()


if __name__ == "__main__":
    unittest.main()
