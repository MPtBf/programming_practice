"""
• Создайте иерархию классов для различных типов
    транспортных средств (Необходим один родительский
    класс и 3 дочерних).
• Реализуйте метод, который позволяет каждому
    транспортному средству возвращать собственное
    описание (Метод в каждом классе должен иметь
    одинаковое название).
• Продемонстрируйте вызов данного метода для
    каждого транспортного средства.
• Отрабатываемый принцип: Полиморфизм
"""

from abc import ABC, abstractmethod



# transport

class Transport(ABC):
    def __init__(self, type, color):
        self.type = type
        self.color = color

    @abstractmethod
    def getInfo(self):
        pass


class Car(Transport):
    def __init__(self, color):
        super().__init__('Легковая Машина', color)

    def getInfo(self):
        return f'Тип: {self.type}, цвет: {self.color}, тип кузова: седан, максимальное давление на ремни безопасности: 1800кг'

class Bus(Transport):
    def __init__(self, color):
        super().__init__('Автобус', color)

    def getInfo(self):
        return f'Тип: {self.type}, цвет: {self.color}, наличие поручней: да, вместимость пассажиров: 20 человек'

class Truck(Transport):
    def __init__(self, color):
        super().__init__('Грузовик', color)

    def getInfo(self):
        return f'Тип: {self.type}, цвет: {self.color}, максимальный вес груза: 30 тонн, объём прицепа: 33 кв. м'



car = Car('Белый')
bus = Bus('Синий')
truck = Truck('Серый')

print(car.getInfo())
print(bus.getInfo())
print(truck.getInfo())

