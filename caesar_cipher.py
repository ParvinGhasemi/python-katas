"""
	Caesar Cipher:
	•	Write a function that takes a string and an integer shift, then returns the string encrypted with a Caesar cipher (each letter shifted by the given number of places).
	•	The function should handle wrapping around the alphabet and preserve the case of the letters.
"""

class CaesarCipher:
    """
    A class representing caesar cipher encryption.
    """
    def caesar_cipher_encryption(self, text:str, shift:int) -> str:
        """
        Encrypts the given text using a Caesar cipher with the specified shift.
        :param text: The string to be encrypted.
        :param shift: The integer value by which to shift each letter.
        :return: The encrypted string.
        """

        if not isinstance(text, str):
            raise TypeError("Input text must be a string")
        
        if not isinstance(shift, int):
            raise TypeError("Shift value must be an integer.")

        return ''.join(self.shift_character(character, shift) for character in text)


    def shift_character(self, letter:str, shift:int) -> str:
        """
        Shifts a single character by the given shift value.
        :param letter: The character to shift.
        :param shift: The number of positions to shift.
        :return: The shifted character, or the original character if not alphabetic.
        """
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')
            return chr(start + ((ord(letter) - start + shift) % 26))
        return letter