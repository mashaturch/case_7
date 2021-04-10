"""Case-study #7 Text generator
Разработчики:
Турчинович М. (), Зубарева Т. () , Костылев М. ()
"""

def delete_characters():
    """Removal of service characters"""
    with open ('input.txt', encoding = 'utf-8') as f_in:
        input_text = f_in.readlines()
    text = ''
    punctuation_symbols = list('"#$%&\'()*+-/:;<=>@[\\]^_`{|}~—')
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
