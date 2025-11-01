


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        """
        :return: Возвращает информацию о книге: название, автор, год издания в виде строки
        """
        return f'Книга "{self.title}" от {self.author}, {self.year} года издания'



if __name__ == '__main__':
    b = Book('Lolsk of the lolbruh', 'Arnold Uhohovich', 1487)
    print(b.info())

