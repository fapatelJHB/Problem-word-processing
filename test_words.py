import unittest
import word_processor

class Testword_processor(unittest.TestCase):
    def test_convert_to_word_list(self):
        """
            This function makes sure that the sentence is split at any punctuation mark and spaces. 
        """
        words = word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you'],words)

    def test_words_longer_than(self):
        """
            This function makes sure that it only returns a list of words in the text that is longer than 10
        """
        words = word_processor.words_longer_than(10,'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['interesting','understatement'],words)

     
    def test_words_lengths_map(self):
        """
            This function makes sure that it returns a dictionary that maps a word length.
        """
        words = word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1},words)

    def test_letters_count_map(self):
        """
        This function makes sure that it returns a dictionary that maps each alphabet letter
        to the number of times that letter occurs in the text.
        """
        words = word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 
        'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 
        's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0},words)

    def test_most_used_character(self):
        """
            This function makes sure that it displays the letter that has been used the most in a list.
        """
        words = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual('e',words)