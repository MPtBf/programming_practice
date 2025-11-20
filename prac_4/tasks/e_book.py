

class Book:
    """Класс книги, можно получить информацию методом .get_info()"""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        """
        Возвращает информацию о электронной книге:
        :return: название, автор, год издания в виде строки
        """
        return (f'Книга "{self.title}" от {self.author}, '
                f'{self.year} года издания')


class EBook(Book):
    """Класс электронной книги, можно получить информацию
    методом .get_info()"""

    def __init__(self, title, author, year, fileFormat):
        super().__init__(title, author, year)
        self.fileFormat = fileFormat

    def get_info(self) -> str:
        """
        Возвращает информацию о электронной книге:
        :return: название, автор, год издания в виде строки
        """
        return (f"Книга '{self.title}' от {self.author}, "
                f"{self.year} года издания. "
                f"Доступна в формате {self.fileFormat}.")


if __name__ == '__main__':

    b = EBook('Lolsk of the lolbruh',
              'Arnold Uhohovich',
              1487,
              '.pdf')
    print(b.get_info())
