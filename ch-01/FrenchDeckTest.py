import unittest
from FrenchDeck import FrenchDeck

class FrenchDeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = FrenchDeck()

    def test_can_get_length(self):
        self.assertEqual(52, len(self.deck))

if __name__ == '__main__':
    unittest.main()
