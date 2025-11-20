"""
• Создайте иерархию классов для разных типов
    сотрудников в компании. Реализуйте родительский класс
    Employee и дочерние классы Manager и Developer.
    Каждый класс должен иметь метод для расчета
    зарплаты на основе различных критериев класса.
• Отрабатываемый принцип: Наследование
"""


class Employee:
    """Абстрактный класс сотрудника компании, имеет метод
    для получения месячной зарплаты - .getMonthlySalary()"""

    def __init__(self, salaryPerDay=3_000):
        self.salaryPerDay = salaryPerDay

    def getMonthlySalary(self) -> int:
        """
        метод для расчета зарплаты на основе различных критериев класса.
        :return: int - Рассчитанная зарплата на месяц при работе
        по 5 дней в неделю
        """
        # оплачивается работа 5 дней в неделю из 7
        salary = self.salaryPerDay * 30 * (5/7)

        return round(salary)


class Manager (Employee):
    """Класс менеджера компании, имеет
    бОльшую зарплату в день (5_000), чем разработчики"""

    def __init__(self):
        super().__init__(salaryPerDay=5_000)


class Developer (Employee):
    """Класс разработчика компании, имеет обычную
    зарплату в день (3_000)"""

    def __init__(self):
        super().__init__()


if __name__ == '__main__':

    emp1 = Manager()
    emp2 = Developer()

    print('Месячная зарплата менеджера:',
          emp1.getMonthlySalary())

    print('Месячная зарплата разработчика:',
          emp2.getMonthlySalary())
