
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

words =('These are indeed interesting, an obvious understatement, times. What say you?')
def convert_to_word_list(text):
    """
        This function splits the sentence at any punctuation marks as well as spaces.
        And returns a list of words
    """
    text = split('. , [ ] { } ? / \\ ; : * - + # !', text.lower())
    return list(filter(None, text))
print(convert_to_word_list(words))

def words_longer_than(length, text):
    """
        This function returns a list of words in the text that is longer than 10.
    """
    text = convert_to_word_list(text)
    text = list(filter(lambda word: len(word) > length, text))
    return text
print(words_longer_than(10,words))

def words_lengths_map(text):
    """
        This function takes the string and return a dictionary that maps a word length.
    """
    text = convert_to_word_list(text)
    text = sorted(list(map(lambda word: len(word), text)))
    worddict = {}
    for f in text:
        worddict[f] =text.count(f)
    return(worddict)
print(words_lengths_map(words))

def letters_count_map(text):
    """
        This function takes a string and return a dictionary that maps each alphabet letter
        to the number of times that letter occurs in the text.
    """
    text = ''.join(convert_to_word_list(text))
    text = sorted(list(map(lambda word: word, text)))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    worddict = {}
    for f in alphabet:
        worddict[f] =text.count(f)
    return(worddict)
print(letters_count_map(words))

def most_used_character(text):
    """
        This function displays the letter that has been used the most in a list.
    """
    counter = letters_count_map(text)
    number = max(counter, key=counter.get)
    if not text:
        return None
    else:
        return(number)
print(most_used_character(words))
