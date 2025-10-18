from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        """
        :return: Возвращает информацию о книге: название, автор, год издания в виде строки
        """
        return f'Книга "{self.title}" от {self.author}, {self.year} года издания'

    def print_info(self):
        print(self.info())



if __name__ == '__main__':
    b = Book('Lolsk of the lolbruh', 'Arnold Uhohovich', 1487)
    b.print_info()
