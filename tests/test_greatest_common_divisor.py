import unittest
from greatest_common_divisor import GreatestCommonDivisor

class TestGCD(unittest.TestCase):
    
    def setUp(self):
        self.gcd = GreatestCommonDivisor()

    def test_empty_list(self):
        input_list = []
        self.assertEqual(self.gcd.calculate_gcd(input_list), [])
    
    def test_single_number(self):
        self.assertEqual(self.gcd.calculate_gcd([10]), [10])
    
    def test_basic_numbers(self):
        self.assertEqual(self.gcd.calculate_gcd([10, 8, 2, 5, 25], [10, 2, 8, 2, 2, 1, 5, 5, 25]))

    def test_non_integer_number(self):
        with self.assertRaises(TypeError):
            self.gcd.calculate_gcd([10, 8, 2, "a", 25])
        with self.assertRaises(TypeError):
            self.gcd.calculate_gcd([10, 3.2, 2, 5, 25])

        