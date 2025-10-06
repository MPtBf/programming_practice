

import roman


def convertFromRomanList(romanNumbersList: list[str]) -> list[int]:
    """
    Конвертирует список из римских чисел в список из обычных чисел
    :param romanNumbersList: список с римскими числами
    :return: list[int]
    """

    numbersList = []
    for n in romanNumbersList:
        numbersList.append(roman.fromRoman(n))

    return numbersList


def convertToRomanList(numbersList: list[int]) -> list[str]:
    """
    Конвертирует список из обычных чисел в список из римских чисел
    :param numbersList: список с числами
    :return: list[int]
    """

    romanNumbersList = []
    for n in numbersList:
        romanNumbersList.append(roman.toRoman(n))

    return romanNumbersList


input = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
print('Input:', input)
numbersTests = convertFromRomanList(input)
print('Roman numbers:', numbersTests)
romanNumbersTests = convertToRomanList(numbersTests)
print('Numbers:', romanNumbersTests)
