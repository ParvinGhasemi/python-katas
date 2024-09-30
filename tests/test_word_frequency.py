import unittest
from word_frequency import word_frequency_counter

class TestWordFrequencyCounter(unittest.TestCase):

    def test_sentence_with_repeated_words(self):
        text = "word word word"
        expected_output = {'word': 3}
        self.assertEqual(word_frequency_counter(text), expected_output)

    def test_basic_sentence(self):
        text = "this is a string this is a dictionary"
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'string': 1, 'dictionary': 1}
        self.assertEqual(word_frequency_counter(text), expected_output)

    def test_sentence_with_punctuations(self):
        text = "hello world. this is a sentence, this is a string."
        expected_output = {'hello': 1, 'world': 1,'this': 2, 'is': 2, 'a': 2, 'string': 1, 'dictionary': 1}
        self.assertEqual(word_frequency_counter(text), expected_output)
    
    def test_empty_string(self):
        text = ""
        expected_output = {}
        self.assertEqual(word_frequency_counter(text), expected_output)

    def test_with_mixed_strings(self):
        text = "This is a Test, this is only a test."
        expected_output = {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
        self.assertEqual(word_frequency_counter(text), expected_output)

    def test_with_non_string_inputs(self):
        with self.assertRaises(TypeError):
            word_frequency_counter(123) # Integer input
            word_frequency_counter({"this": 1, "is": 2})  # Dictionary input
            word_frequency_counter(None)  # NoneType input
            word_frequency_counter(["this", "is", "a", "list"])  # List input

    


if __name__ == '__main__':
    unittest.main()
