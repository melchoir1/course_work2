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
