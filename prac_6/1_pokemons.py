import requests


URL = "https://pokeapi.co/api/v2/pokemon/"


class Pokemon:
    """Класс покемона. Имеет параметры:
    name, type, weight, height, abilitiesList"""

    def __init__(self, name: str, type: str = None, weight: int = None,
                 height: int = None, abilitiesList: list[str] = None):
        self.name = name
        self.type = type
        self.weight = weight
        self.height = height
        self.abilitiesList = abilitiesList

        self.isInfoLoaded = all(
            [f is not None for f in [type, weight, height, abilitiesList]]
        )

    def loadInfo(self):
        """
        Делает запрос для получения информации о покемоне.
        Сохраняет параметры: type, weight, height, abilities.
        """

        if self.isInfoLoaded:
            return

        pokJson = requests.get(URL + self.name).json()

        self.type = pokJson['types'][0]['type']['name']
        self.weight = pokJson['weight']
        self.height = pokJson['height']
        self.abilitiesList = [ab['ability']['name']
                              for ab in pokJson['abilities']]

        self.isInfoLoaded = True

    def printInfo(self):
        """
        Выводит базовую информацию об этом покемоне
        """

        self.loadInfo()

        print(f'Информация о покемоне {self.name}:')
        print(f'- Тип: {self.type}')
        print(f'- Вес: {self.weight} кг')
        print(f'- Высота: {self.height} м')
        print(f'- Способности: {", ".join(self.abilitiesList)}')


def getPokemonsList() -> list[Pokemon]:
    """
    Делает запрос для получения имён 20 первых покемонов,
    из которых делает объекты класса Pokemon.
    :return: список из 20 объектов Pokemon.
    """

    res = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=20")
    pokListJson = res.json()
    pokNamesList = [p['name'].title() for p in pokListJson['results']]
    pokemonsList = [Pokemon(n) for n in pokNamesList]

    return pokemonsList


def pokemonFind(pokName: str, pokList: list[Pokemon]) -> Pokemon | None:
    """
    Находит объект покемона с заданным именем
    :param: pokName: имя покемона
    :param: pokList: список всех доступных покемонов для поиска
    :return: Pokemon или None (если не найден)
    """
    for pok in pokList:
        if pok.name.lower() == pokName.lower():
            return pok

    return None


def startConsoleDialogue() -> None:
    """
    Запускает диалог в консоли
    :return: None
    """

    pokList = getPokemonsList()

    print('В нашем зоопарке есть замечательные 20 покемонов:')
    print(', '.join([p.name for p in pokList]).title())
    print()
    print('Пишите названия покемонов для получения доп. информации.')

    while True:
        print()
        inp = input('>>> ').lower()

        pokFound = pokemonFind(inp, pokList)
        if not pokFound:
            print('Такого покемона нет в списке.')
            continue

        pokFound.printInfo()


if __name__ == '__main__':
    startConsoleDialogue()
