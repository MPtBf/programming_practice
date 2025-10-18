from Book import Book




class EBook(Book):
    def __init__(self, title, author, year, fileFormat):
        super().__init__(title, author, year)
        self.fileFormat = fileFormat

    def info(self) -> str:
        """
        :return: Возвращает информацию о книге: название, автор, год издания, ссылку на сайт в виде строки
        """
        return f"""
Книга "{self.title}" от {self.author}, {self.year} года издания.
Доступна в формате {self.fileFormat}.
"""





if __name__ == '__main__':
    b = EBook('Lolsk of the lolbruh', 'Arnold Uhohovich', 1487, '.pdf')
    print(b.info())




