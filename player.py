class Player:
    def __init__(self, name):
        self.name = name
        self.words_used = set()

    def __repr__(self):
        return f'Player({self.name}, {self.words_used})'

    def get_name(self):
        """имя пользователя"""
        return self.name

    def count_words_used(self):
        """получение количества использованных слов"""
        return len(self.words_used)

    def add_words_used(self, add_word):
        # self.add_word = add_word
        """добавление слова в использованные слова"""
        self.words_used.add(add_word)

    def exam_words_used(self, add_word):
        """проверка использования данного слова """
        return add_word in self.words_used
