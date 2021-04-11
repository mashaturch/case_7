"""Case-study #7 Text generator
Разработчики:
Турчинович М. (60%), Зубарева Т. (40%) , Костылев М. (40%)
"""
import numpy as np

def delete_characters(name_file):
    """Removal of service characters"""
    with open(name_file, encoding='utf-8') as f_in:
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
    for i in range(len(incorrect_basic_symbols)):
        text = text.replace(incorrect_basic_symbols[i], basic_symbols[i])
    text = text.replace('  ', ' ')
    return text

def make_pairs(ind_words):
    """Function for concatenating pairs of words"""
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])

# entered data
name_file = input('Имя файла: ')
number_of_offers = int(input('Количество генерируемых предложений: '))


ind_words = delete_characters(name_file).split()
pair = make_pairs(ind_words)

# sorting similar words
word_dict = {}
for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

# compiling a list of starting words
start_words = []
for word in word_dict:
    if word == word.capitalize():
        if not (word in start_words):
            start_words.append(word)

end_symbols = ['.', '!', '?']

# random compilation of new text
k = 0
while k < number_of_offers:
    first_word = np.random.choice(start_words)
    chain = [first_word]
    n_words = 20
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
        if chain[-1][-1] in end_symbols:
            break
    print(' '.join(chain), end='')
    k += 1
    if chain[-1][-1] != '.':
        print('.', end=' ')
        k += 1
    else:
        print(' ', end='')