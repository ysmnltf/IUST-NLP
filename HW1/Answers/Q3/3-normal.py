import nltk
from nltk.corpus import words
import re

nltk.download('words')
words = words.words()

repeat_regex = re.compile(r"(\w)\1+")


def remove_at_idx(string, idx):
    return string[0: idx:] + string[idx + 1::]


def fix_word(word):
    fixed_word = word
    should_break = 0
    while fixed_word not in words:
        repeated_char = (repeat_regex.search(fixed_word))
        if repeated_char is None:
            break
        fixed_word = remove_at_idx(fixed_word, repeated_char.span()[0])
        should_break += 1
        if should_break > len(word):
            break
    return fixed_word


if __name__ == '__main__':
    for i in range(5):
        input_word = input("please enter a word: ")
        print("correct word: ", fix_word(input_word.strip()))
