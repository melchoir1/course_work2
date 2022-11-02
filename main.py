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

while player_1.count_words_used() < words.get_subclass():
    word = input('Введите слово: ')
    #1 вариант когда ннабрали слова стоп
    if word == 'стоп':
        break
    elif word == 'stop':
        exit(1)
    #2 вариант когда пользователь ввел не короче 3 букв
    elif len(word) < 3:
        print('слишком короткое слово')
    #слово нельзя составить, его нет в подсловах
    elif not words.has_subclass(word):
        print('такое слово нельзя составить')
    #данное слово уже использоввано
    elif player_1.exam_words_used(word):
        print('уже использовано')
    else:
        print('верно')
        player_1.add_words_used(word)
print(f'Игра завершена, вы угадали {player_1.count_words_used()} слов!')
