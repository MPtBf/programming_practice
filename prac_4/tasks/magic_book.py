from datetime import datetime


class Book:
    """Класс книги, можно получить информацию методом .get_info()"""

    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year

    def get_info(self) -> str:
        """
        Возвращает информацию о электронной книге:
        :return: название, автор, год издания в виде строки
        """
        return (f'Книга "{self._title}" от {self._author}, '
                f'{self._year} года издания')


class MagicBook(Book):
    """Класс книги с магическими полями .title, .author, .year"""

    def __init__(self, title, author, year):
        super().__init__(title, author, year)

    @classmethod
    def fromString(cls, data):
        """
        Функция для создания экземпляра книги из строки с её данными:
        название, автор, год - перечисленными через ";"
        """
        split_data = data.split(';')
        title, author, year = [v.strip() for v in split_data]
        year = int(year)

        return cls(title, author, year)

    @property
    def title(self) -> str:
        """Получить название"""
        return self._title

    @title.setter
    def title(self, value: str):
        """Установить название"""
        self._title = str(value).capitalize()

    @property
    def author(self) -> str:
        """Получить автора"""
        return self._author

    @author.setter
    def author(self, value: str):
        """Установить автора"""
        self._author = str(value).title()

    @property
    def year(self) -> int:
        """Получить год"""
        return self._year

    @year.setter
    def year(self, value: int | str):
        """Установить год"""
        value = int(value)
        if not 0 <= value <= datetime.now().year:
            raise ValueError(
                'Год издания должен быть в промежутке от 0 года до сейчашнего'
            )
        self._year = value

    def __eq__(self, other: Book) -> bool:
        """Равенство между книгами"""
        return all([
            self._title == other._title,
            self._author == other._author,
            self._year == other._year,
            ])

    def __str__(self):
        return (f'Книга "{self._title}" от {self._author}, '
                f'{self._year} года издания')


if __name__ == '__main__':

    # Проверим на равенство, а за одно и .fromString()
    b = MagicBook('Lolsk of the lolbruh',
                  'Arnold Uhohovich',
                  1487)
    b2 = MagicBook.fromString('Lolsk of the lolbruh; Arnold Uhohovich; 1487')
    print(b == b2)

    # Проверим на смену автора, получим автора
    # в правильном регистре (с большой буквы)
    print(b.author)
    b.author = 'nikola TESLA'
    print(b.author)
