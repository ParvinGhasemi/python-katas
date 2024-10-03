import unittest
from caesar_cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = CaesarCipher()
    def test_basic_shift(self):
        self.assertEqual(self.cipher.caesar_cipher_encryption("BCD!", 1), "CDE!")
        self.assertEqual(self.cipher.caesar_cipher_encryption("BCD!", -1), "ABC!")

    def test_shift_with_wraparound(self):
        self.assertEqual(self.cipher.caesar_cipher_encryption("XYZ", 3), "ABC")
        self.assertEqual(self.cipher.caesar_cipher_encryption("xyz", 3), "abc")
        
    def test_shift_with_large_number(self):
        self.assertEqual(self.cipher.caesar_cipher_encryption("Hello, World!", 52), "Hello, World!")

    def test_empty_string(self):
        self.assertEqual(self.cipher.caesar_cipher_encryption("", 5), "")

    def test_non_alpha_characters(self):
        self.assertEqual(self.cipher.caesar_cipher_encryption("1234!@#$", 4), "1234!@#$")

    def test_mixed_case_and_symbols(self):
        text = "Hello, World!"
        shift = 3
        expected = "Khoor, Zruog!"
        self.assertEqual(self.cipher.caesar_cipher_encryption(text, shift), expected)

if __name__ == '__main__':
    unittest.main()