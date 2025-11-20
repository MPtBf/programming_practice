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


class Transport(ABC):
    """Абстрактный класс транспорта"""

    def __init__(self, type: str, color: str):
        self.type = type
        self.color = color

    @abstractmethod
    def getInfo(self) -> str:
        """
        Метод для получения информации о данном транспорте
        :return: строка с информацией
        """
        pass


class Car(Transport):
    """Класс легковой машины"""

    def __init__(self, color: str,
                 bodyType: str,
                 maximumSeatBeltsPressure: int):
        super().__init__('Легковая Машина', color)
        self.bodyType = bodyType
        self.maximumSeatBeltsPressure = maximumSeatBeltsPressure

    def getInfo(self) -> str:
        """
        Метод для получения информации о данном транспорте
        :return: строка с информацией
        """
        return (f'Тип: {self.type}, цвет: {self.color}, '
                f'тип кузова: {self.bodyType}, максимальное давление на ремни '
                f'безопасности: {self.maximumSeatBeltsPressure} кг')


class Bus(Transport):
    """Класс автобуса"""

    def __init__(self, color: str,
                 doHaveHandrails: bool,
                 passengerCapacity: int):
        super().__init__('Автобус', color)
        self.doHaveHandrails = doHaveHandrails
        self.passengerCapacity = passengerCapacity

    def getInfo(self) -> str:
        """
        Метод для получения информации о данном транспорте
        :return: строка с информацией
        """
        return (f'Тип: {self.type}, цвет: {self.color}, '
                f'наличие поручней: {self.doHaveHandrails}, '
                f'вместимость пассажиров: {self.passengerCapacity} человек')


class Truck(Transport):
    """Класс грузовика"""

    def __init__(self, color: str,
                 maxCargoWeightTons: int,
                 trailerVolumeCubMeters: int):
        super().__init__('Грузовик', color)
        self.maxCargoWeightTons = maxCargoWeightTons
        self.trailerVolumeCubMeters = trailerVolumeCubMeters

    def getInfo(self) -> str:
        """
        Метод для получения информации о данном транспорте
        :return: строка с информацией
        """
        return (f'Тип: {self.type}, цвет: {self.color}, '
                f'максимальный вес груза: {self.maxCargoWeightTons} тонн, '
                f'объём прицепа: {self.trailerVolumeCubMeters} кв. м')


if __name__ == '__main__':

    car = Car('Белый', 'Седан', 1800)
    bus = Bus('Синий', True, 25)
    truck = Truck('Серый', 40, 33)

    print("Информация о car -", car.getInfo())
    print("Информация о bus -", bus.getInfo())
    print("Информация о truck -", truck.getInfo())
