"""Case-study #7 Text generator
Разработчики:
Турчинович М. (), Зубарева Т. () , Костылев М. ()
"""
import numpy as np
import random
from collections import defaultdict

def delete_characters():
    """Removal of service characters"""
    with open ('input.txt', encoding = 'utf-8') as f_in:
        input_text = f_in.readlines()
    text = ''
    punctuation_symbols = list('"#$%&\()*+-/:;<=>@[]^_`{|}~—–«»')
    incorrect_basic_symbols = [' .', ' !', ' ?', ' ,']
    basic_symbols = ['.', '!', '?', ',']
    for string in input_text:
        text += string[:len(string) - 1] + ' '
    text += input_text[-1][-1]
    for char in punctuation_symbols:
        text = text.replace(char, '')
    text = text.replace('  ', '')
    for i in range(len(incorrect_basic_symbols)):
        text = text.replace(incorrect_basic_symbols[i], basic_symbols[i])
    return text


ind_words = delete_characters().split()
def make_pairs(ind_words):
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])
pair = make_pairs(ind_words)
word_dict = {}

for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]


start_words = []
for ch in word_dict:
    if ch == ch.capitalize():
        if not ch in start_words:
            start_words.append(ch)

print(start_words)
end_symbols = ['.', '!', '?']

last_words = []
for sh in word_dict:
    if sh[-1] in end_symbols:
        if not (sh in last_words):
            last_words.append(sh)
print(last_words)


first_word = np.random.choice(start_words)
while first_word.istitle():
    chain = [first_word]
    n_words = 20
    first_word = np.random.choice(start_words)

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    print(' '.join(chain))