import random


def get_words():
    '''This function get the words from text file.'''

    words = []
    with open('english_words.text', mode='r') as f:
        for line in f:
            words.append(line.rstrip('\n'))

    return words


def create_question(words):
    '''This function returns a random word in 3000 words.'''

    question = words[random.randint(1, 3000)]
    return question


def judge_input(user_input, question):
    '''judge the usert_input

       if user_input is not string, will return 2.
       if user_input = question, will return 1.
       if user_input != question, will return 0.
    '''

    if not isinstance(user_input, str):
        return 2

    if user_input == question:
        return 1
    else:
        return 0
