import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_basic_shift(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_cipher("BCD!", 1), "CDE!")
        self.assertEqual(caesar_cipher("BCD!", -1), "ABC!")



    def test_shift_with_wraparound(self):
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        

    def test_shift_with_large_number(self):
        self.assertEqual(caesar_cipher("Hello, World!", 52), "Hello, World!")

    def test_empty_string(self):
        self.assertEqual(caesar_cipher("", 5), "")

    def test_non_alpha_characters(self):
        self.assertEqual(caesar_cipher("1234!@#$", 4), "1234!@#$")

if __name__ == '__main__':
    unittest.main()