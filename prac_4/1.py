"""
• Создайте иерархию классов для разных типов
    сотрудников в компании. Реализуйте родительский класс
    Employee и дочерние классы Manager и Developer.
    Каждый класс должен иметь метод для расчета
    зарплаты на основе различных критериев класса.
• Отрабатываемый принцип: Наследование
"""



class Employee:
    def __init__(self, salaryPerDay=3_000):
        self.salaryPerDay = salaryPerDay

    def getMonthlySalary(self):
        """
        метод для расчета зарплаты на основе различных критериев класса.
        """
        salary = self.salaryPerDay * 30 * (5/7)  # оплачивается работа 5 дней в неделю
        return round(salary)


class Manager (Employee):
    def __init__(self):
        super().__init__(salaryPerDay=5_000)

class Developer (Employee):
    def __init__(self):
        super().__init__()


emp1 = Manager()
emp2 = Developer()

print(emp1.getMonthlySalary())
print(emp2.getMonthlySalary())


