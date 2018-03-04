import unittest
from Vector import Vector

class VectorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_addition(self):
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)
        self.assertEqual(Vector(4, 5), v1 + v2)

if __name__ == '__main__':
    unittest.main()