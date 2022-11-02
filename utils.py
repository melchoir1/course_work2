import random

import requests as requests

from basic_word import BasicWord


def load_data(path):
    """загрузка данных по URL"""
    result = requests.get(path)
    result_status = result.status_code
    if result_status != 200:
        return []

    return result.json()

def load_random_word(path):
    list_words = load_data(path)

    if len(list_words) == 0:
        return None

    random_word =random.choice(list_words)
    word = random_word['word']
    sub_words = random_word['subwords']

    basic_word = BasicWord(word, sub_words)
    return basic_word
