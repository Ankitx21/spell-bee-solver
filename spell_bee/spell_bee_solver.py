import nltk
from itertools import permutations
from nltk.corpus import words
from nltk.corpus import wordnet

nltk.download('words')
nltk.download('wordnet')

def is_valid_word(word, user_input):
    return len(word) >= 7 and all(letter in user_input for letter in word)

def get_custom_word_list():
    # Add more sources or APIs to fetch words
    word_list_nltk = set(words.words())
    word_list_wordnet = set(wordnet.words())
    # Add more word lists as needed

    return word_list_nltk.union(word_list_wordnet)  # Merge multiple word lists

def generate_words(user_input):
    word_list = get_custom_word_list()
    valid_words = [word for word in word_list if is_valid_word(word, user_input)]
    return valid_words

def find_perfect_pangram(user_input):
    alphabet_set = set(user_input)
    all_words = generate_words(user_input)
    perfect_pangrams = [word for word in all_words if set(word) == alphabet_set]
    return perfect_pangrams
