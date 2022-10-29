from config import WORDS_TO_PLAY
from utils import load_random_word
from player import Player

name = input('Введите имя игрока: ')
player_1 = Player(name)
print(f'Привет {player_1.get_name()}')
words = load_random_word(WORDS_TO_PLAY) #случайное слово
print(f'Составьте {words.get_subclass()} слов из слова {words.get_word()}')
print('Слова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print('Введите ваше первое слово: ')


while True:
    word = input('Введите слово: ')
    if len(word) < 4:
        print('слишком короткое слово')
        continue
    if word == 'стоп':
        exit(1)
    if word == 'stop':
        exit(1)

    if not words.has_subclass(word):
        player_1.add_words_used(word)
        print('верно')
    else:
        print('уже использовано')
        continue
    if player_1.count_words_used() == words.get_subclass():
        print(f'Игра завершена, вы угадали {player_1.count_words_used()} слов!')
        exit(1)


