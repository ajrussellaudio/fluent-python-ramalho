import unittest
from FrenchDeck import FrenchDeck, Card

class FrenchDeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = FrenchDeck()

    def test_can_get_length(self):
        self.assertEqual(52, len(self.deck))

    def test_can_get_card_at_position(self):
        self.assertEqual(Card('2', 'spades'), self.deck[0])

if __name__ == '__main__':
    unittest.main()
