"""
Problem 1: Word Frequency Counter

Description: Write a Python program that takes a string as input and uses a dictionary to count the frequency of each word in the string.
Example:
Input: "this is a string, this is a dictionary"
Output: {'this': 2, 'is': 2, 'a': 2, 'string': 1, 'dictionary': 1}
"""

import re
from collections import Counter

def word_frequency_counter(text: str = None) -> dict[str, int]:
    if text is None:
        raise TypeError('text must not be None or empty.')
    
    if not isinstance(text, str):
        raise TypeError('text must be a string.')

    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    frequency = {}
    # Solution 1
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


    # Solution 2
    """
    frequency = 
    return dict(Counter(words))
    """


    # Solution 3
    """
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1    

    return frequency
    """    