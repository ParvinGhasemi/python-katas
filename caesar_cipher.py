"""
	1.	Caesar Cipher:
	•	Write a function that takes a string and an integer shift, then returns the string encrypted with a Caesar cipher (each letter shifted by the given number of places).
	•	The function should handle wrapping around the alphabet and preserve the case of the letters.
"""

def caesar_cipher(text, shift_number):
    
    return ''.join(shift_character(char, shift_number) for char in text)


def shift_character(letter, shift):
    if letter.isalpha():
        start = ord('A') if letter.isupper() else ord('a')
        return chr(start + ((ord(letter) - start + shift) % 26))
    return letter