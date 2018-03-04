import unittest
from Card import Card

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card('A', 'spades')

    def test_get_rank(self):
        self.assertEqual('A', self.card.rank)

    def test_get_suit(self):
        self.assertEqual('spades', self.card.suit)

    def test_equality(self):
        self.assertEqual(Card('A', 'spades'), self.card)

if __name__ == '__main__':
    unittest.main()
