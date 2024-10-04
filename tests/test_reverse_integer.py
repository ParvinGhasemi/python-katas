import unittest
from reverse_integer import ReverseInteger

class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.reverse = ReverseInteger()

    def test_positive_integer(self):
        self.assertEqual(self.reverse.reverse_integer(12), 21)
        self.assertEqual(self.reverse.reverse_integer(135), 531)

    def test_reversed_with_zeroes(self):
        self.assertEqual(self.reverse.reverse_integer(9000), 9)
        self.assertEqual(self.reverse.reverse_integer(-9000), -9)
        self.assertEqual(self.reverse.reverse_integer(0), 0)


    def test_negative_integer(self):
        self.assertEqual(self.reverse.reverse_integer(-12), -21)
        self.assertEqual(self.reverse.reverse_integer(-135), -531)

    def test_bigger_than_contraints(self):
        self.assertEqual(self.reverse.reverse_integer(1534236469), 0)
        self.assertEqual(self.reverse.reverse_integer(-1534236469), 0)

        
    