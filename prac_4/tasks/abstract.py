from abc import ABC, abstractmethod


class Printable(ABC):
    """Абстрактный класс предмета с возможностью
    вывода в консоль - .print_info()"""

    @abstractmethod
    def print_info(self) -> None:
        """
        Вывод в консоль информации о предмете
        :return: None
        """
        pass


class Book(Printable):
    """Класс книги, наследуется от Printable для
    возможности вызова .print_info()"""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        """
        Возвращает информацию о книге в виде строки
        :return: Строка с названием, автором, годом издания
        """
        return (f'Книга "{self.title}" от {self.author}, '
                f'{self.year} года издания')

    def print_info(self) -> None:
        """
        Вывод в консоль информации о данной книге:
        название, автора, год издания
        :return: None
        """
        print(self.get_info())


if __name__ == '__main__':
    b = Book('Lolsk of the lolbruh', 'Arnold Uhohovich', 1487)
    b.print_info()
