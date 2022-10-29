class BasicWord:
    """
    - исходное слово,
    - набор допустимых подслов.
    """
    def __init__(self, word, subclass):
        self.word = word
        self.subclass = subclass


    def __repr__(self): #можно попробовать прописать потом с методом __str__
        return f'BasicWord({self.word},{self.subclass})'

    def get_word(self):
        """:return исходное слово"""
        return self.word

    def get_subclass(self):
        """подсчет количества подслов (вернет int)"""
        return len(self.subclass)

    def has_subclass(self, check_word):
        """проверкa введенного слова в списке допустимых подслов"""
        return check_word in self.subclass
#check_word.lower() можно добавить чтоб пользователь не вводил большими буквами

# python_check_word = ["пони","тон","ион","опт","пот","тип","топ","пион","понт"]
# test_word = BasicWord('питон', python_check_word)

# print(test_word)
# print(test_word.get_subclass())
# print(test_word.has_subclass('опт'))
# print(test_word.has_subclass('square'))
# print(test_word.get_word())