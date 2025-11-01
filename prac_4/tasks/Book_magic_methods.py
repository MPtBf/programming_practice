from datetime import datetime

from Book import Book


class MBook(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)

    @classmethod
    def fromString(cls, data):
        title, author, year = data.split(';')
        year = int(year)
        return cls(title, author, year)


    @property
    def Title(self):
        return self.title
    @Title.setter
    def Title(self, value):
        self.title = str(value).capitalize()

    @property
    def Author(self):
        return self.author
    @Author.setter
    def Author(self, value):
        self.author = str(value).title()

    @property
    def Year(self):
        return self.year
    @Year.setter
    def Year(self, value):
        value = int(value)
        if not 0 <= value <= datetime.now().year:
            raise ValueError('Год издания должен быть в промежутке от 0 года до сейчашнего')
        self.year = value

    def __eq__(self, other):
        return all([
            self.title == other.title,
            self.author == other.author,
            self.year == other.year,
            ])
    def __str__(self):
        return f'Книга "{self.title}" от {self.author}, {self.year} года издания'


if __name__ == '__main__':
    b = MBook('Lolsk of the lolbruh', 'Arnold Uhohovich', 1487)

    print(b.Author)
    b.Author = 'nikola TESLA'
    print(b.Author)



