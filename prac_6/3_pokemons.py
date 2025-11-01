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

    def printInfo(self, indent=0):
        """
        Выводит базовую информацию об этом покемоне
        :param indent: количество дополнительного отступа
        (для перечисления в цикле, чтобы выглядело хорошо)
        """

        self.loadInfo()

        stringsToPrint = [
            f'Информация о покемоне {self.name}:',
            f'- Тип: {self.type}',
            f'- Вес: {self.weight} кг',
            f'- Высота: {self.height} м',
            f'- Способности: {", ".join(self.abilitiesList)}',
        ]

        for s in stringsToPrint:
            print('- '*indent + s)

    def getScore(self) -> int:
        """
        Рассчитывает счёт покемона в соответствии с весом, ростом и количеством
        способностей покемона (применяется для тренировочного боя)
        :return: int общий счёт
        """

        self.loadInfo()

        return (self.weight + self.height * 5) * len(self.abilitiesList) * 100


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


def pokemonBattle(pok1: Pokemon, pok2: Pokemon):
    """
    Устраиваем тренировочный бой между покемонами. Выводим в консоль результат
    :param: pok1: первый покемон для боя
    :param: pok2: второй покемон для боя
    :return: None
    """

    pok1Score = pok1.getScore()
    pok2Score = pok2.getScore()

    print(f'Тренировочный бой - {pok1.name} VS {pok2.name}:')
    print(f'- Покемон {pok1.name} - вес: {pok1.weight} кг, '
          f'высота: {pok1.height} м, способностей: {len(pok1.abilitiesList)}, '
          f'общий счёт: {pok1Score}')
    print(f'- Покемон {pok2.name} - вес: {pok2.weight} кг, '
          f'высота: {pok2.height} м, способностей: {len(pok2.abilitiesList)}, '
          f'общий счёт: {pok2Score}')

    pokWinner = pok1 if pok1Score > pok2Score else pok2
    print(f'- Победитель - покемон {pokWinner.name}')


def getPoksList() -> list[Pokemon]:
    """
    Делает запрос на список имён покемонов (первые 20) и делает
    объекты классов Pokemon
    :return: list[Pokemon] список с покемонами (первые 20)
    """

    pokListJson = requests.get(URL).json()

    pokNamesList = [p['name'].title() for p in pokListJson['results']]
    pokemonsList = [Pokemon(n) for n in pokNamesList]

    return pokemonsList


def printAvailableCmds() -> None:
    """
    Выводит список доступных консольных команд
    :return: None
    """
    print('Список доступных консольных команд:')
    print('- >>> help: вывести список консольных команд')
    print('- >>> list all: вывести имена всех доступных покемонов')
    print('- >>> list team: вывести имена покемонов в вашей команде')
    print('- >>> add [имя покемона]: добавить покемона в свою команду')
    print('- >>> rem [имя покемона]: удалить покемона из своей команды')
    print('- >>> info [имя покемона]: вывести информацию о покемонах')
    print('- >>> info *: вывести информацию о всех покемонах в команде')
    print('- >>> find [имя покемона]: найти покемона')
    print('- >>> battle [имя покемона 1] [имя покемона 2]: тренировочный бой '
          'между 2 покемонами')
    print('- >>> exit: выход')


def startConsoleDialogue() -> None:
    """
    Запускает диалог с консоли
    :return: None
    """

    poksList: list[Pokemon] = getPoksList()
    teamPoksList: list[Pokemon] = []

    print()
    print('Добро пожаловать в замечательный зоопарк замечательных покемонов!')
    print()
    printAvailableCmds()

    while True:
        print()
        inp = input('>>> ').lower()
        inpSplit = inp.split(' ')

        try:
            cmdName = inpSplit[0]
            cmdArgs = inpSplit[1:]

            match cmdName:
                case 'help':
                    printAvailableCmds()

                case 'list':
                    place = cmdArgs[0]

                    if place == 'team':
                        print('Покемоны в вашей команде:')
                        for pok in teamPoksList:
                            print(f'- {pok.name}')

                    elif place == 'all':
                        print('Все доступные покемоны:')
                        for pok in poksList:
                            print(f'- {pok.name}')

                    else:
                        print('Неизвестный аргумент консольной команды. '
                              'Используйте один из: team, all')

                case 'add':
                    pokName = cmdArgs[0]

                    pokFoundAll = pokemonFind(pokName, poksList)
                    pokFoundTeam = pokemonFind(pokName, teamPoksList)

                    if not pokFoundAll:
                        print(f'Покемона {pokName.title()} нет в списке '
                              f'доступных. Просмотреть список: >>> list all')
                        continue

                    elif pokFoundTeam:
                        print(f'Покемон {pokFoundAll.name} уже '
                              f'есть в вашей команде. Посмотреть '
                              f'покемонов в вашей команде: >>> list team')
                        continue

                    teamPoksList += [pokFoundAll]
                    print(f'Покемон {pokFoundAll.name} добавлен '
                          f'в вашу команду')

                case 'rem':
                    pokName = cmdArgs[0]

                    pokFoundTeam = pokemonFind(pokName, teamPoksList)

                    if not pokFoundTeam:
                        print(f'Покемона {pokName.title()} нет в вашей '
                              f'команде. Посмотреть покемонов в вашей '
                              f'команде: >>> list team')
                        continue

                    teamPoksList.remove(pokFoundTeam)
                    print(f'Покемон {pokFoundTeam.name} удалён из '
                          f'вашей команды')

                case 'info':
                    pokName = cmdArgs[0]

                    if pokName == '*':
                        print('Информация оо всех покемонах в ваше команде:')
                        for pok in teamPoksList:
                            pok.printInfo(indent=1)

                    else:
                        pokFound = pokemonFind(pokName, poksList)

                        if not pokFound:
                            print(f'Покемона {pokName.title()} нет в списке '
                                  f'доступных. Просмотреть список: '
                                  f'>>> list all')
                            continue

                        pokFound.printInfo()

                case 'find':
                    pokName = cmdArgs[0]

                    pokFoundAll = pokemonFind(pokName, poksList)
                    pokFoundTeam = pokemonFind(pokName, teamPoksList)

                    if pokFoundTeam:
                        print(f'Покемон {pokFoundAll.name} находится '
                              f'в вашей команде')

                    elif pokFoundAll:
                        print(f'Покемон {pokFoundAll.name} есть в списке '
                              f'доступных, но не находится в вашей команде')

                    else:
                        print(f'Покемона {pokName.title()} нет в списке '
                              f'доступных. Просмотреть список: >>> list all')

                case 'battle':
                    pok1Name = cmdArgs[0]
                    pok2Name = cmdArgs[1]

                    pokFound1 = pokemonFind(pok1Name, poksList)
                    pokFound2 = pokemonFind(pok2Name, poksList)

                    if not pokFound1:
                        print(f'Покемона {pok1Name.title()} нет в списке '
                              f'доступных. Просмотреть список: >>> list all')
                        continue
                    if not pokFound2:
                        print(f'Покемона {pok2Name.title()} нет в списке '
                              f'доступных. Просмотреть список: >>> list all')
                        continue
                    if pokFound1 == pokFound2:
                        print('Покемон не может сражаться сам с собой. '
                              'Выберите 2 разных')
                        continue

                    pokemonBattle(pokFound1, pokFound2)

                case 'exit':
                    print('Вы вышли из зоопарка покемонов. '
                          'Заходите к нам ещё!')
                    break

                case _:
                    print('Неизвестная команда. Список доступных '
                          'консольных команд: >>> help')

        except Exception as e:
            print(f'Произошла ошибка при обработке консольной команды: '
                  f'{e}. Попробуйте ещё раз')


if __name__ == '__main__':
    startConsoleDialogue()
