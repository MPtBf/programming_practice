

from random import choice
from string import punctuation as specialSymbols


alphLower = ''.join(map(lambda i: chr(i), range(ord('a'), ord('z')+1)))
alphUpper = ''.join(map(lambda i: chr(i), range(ord('A'), ord('Z')+1)))
numbers = '0123456789'


def generatePassword(doUseLowercase: bool, doUseUppercase: bool,
                     doUseSpecialSymbols: bool, doUseNumbers: bool,
                     length: int) -> str:
    r"""
    Генерирует пароль с заданными параметрами
    :param doUseLowercase: использовать ли буквы нижнего регистра (abcdefghijklmnopqrstuvwxyz)
    :param doUseUppercase: использовать ли буквы верхнего регистра (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
    :param doUseSpecialSymbols: использовать ли спец. символы (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    :param doUseNumbers: использовать ли цифры (0123456789)
    :param length: длина пароля
    :return: строка пароля
    """

    # собираем символы для генерации в одну переменную для удобства
    symbolsToChooseFrom = ''
    if doUseLowercase:
        symbolsToChooseFrom += alphLower
    if doUseUppercase:
        symbolsToChooseFrom += alphUpper
    if doUseSpecialSymbols:
        symbolsToChooseFrom += specialSymbols
    if doUseNumbers:
        symbolsToChooseFrom += numbers

    resPassword = ''
    for _ in range(length):
        resPassword += choice(symbolsToChooseFrom)

    return resPassword


def tryInputData(dataTypeCastFunc, messageBeforeInput: str = '',
                 messageOnError: str = 'Ошибка!'):
    """
    Пытается получить данные нужного типа от пользователя.
    Если пользователь вводит данные, вызывающие ошибку в dataTypeCastFunc,
    то ему выводится messageOnError и запрашивается повторный ввод
    :param dataTypeCastFunc: функция для преобразования текста в нужное значение. При невозможности преобразования должна вызывать ошибку ValueError
    :param messageBeforeInput: сообщение, вопрос, высвечивающийся перед вводом пользователя
    :param messageOnError: сообщение об ошибке, в случае, если dataTypeCastFunc вызывает ошибку
    :return: данные тех типов, которые может вернуть заданная dataTypeCastFunc
    """

    # в цикле для того, чтобы при ошибке пользователь вводил текст ещё раз
    while True:
        inp = input(messageBeforeInput + ' ')

        try:
            res = dataTypeCastFunc(inp)
        except ValueError:
            print(messageOnError)

            # доп. отступ
            print()

            continue

        return res


# user input cast functions
def getYesOrNo(text) -> bool:
    """
    Функция для преобразования текста в ответ y/yes или n/no в булево значение.
    В случае невозможности преобразования вызывает ошибку ValueError
    :param text: текст для преобразования
    :return: True/False
    """

    text = text.lower()
    if text in ['y', 'yes']:
        return True
    elif text in ['n', 'no']:
        return False
    else:
        raise ValueError(f'Cant determine yes or no for text: {text}')


def getPositiveNumber(text) -> int:
    """
    Функция для преобразования текста в положительное целое число.
    В случае невозможности преобразования вызывает ошибку ValueError
    :param text: текст для преобразования
    :return: int, > 0
    """

    try:
        num = int(text)
    except:
        raise ValueError('Cant cast text to a number')

    if num > 0:
        return num
    else:
        raise ValueError('Cant use non-positive numbers')


def terminalInterfaceGenPass() -> None:
    """
    Запускает диалог с пользователем в терминале.
    Спрашивает пользователя параметры для пароля, генерирует пароль и выводит его.
    При ошибке распознавания вводимого значения просит ввести значение повторно
    :return: None
    """

    # узнаём необходимые данные у пользователя
    doUseLowercase = tryInputData(getYesOrNo,
                                  'Использовать ли маленькие буквы в пароле? y/n:',
                                  'Ошибка, введите y/n!')
    doUseUppercase = tryInputData(getYesOrNo,
                                  'Использовать ли большие буквы в пароле? y/n:',
                                  'Ошибка, введите y/n!')
    doUseSpecialSymbols = tryInputData(getYesOrNo,
                                       'Использовать ли спец. символы в пароле? y/n:',
                                       'Ошибка, введите y/n!')
    doUseNumbers = tryInputData(getYesOrNo,
                                'Использовать ли цифры в пароле? y/n:',
                                'Ошибка, введите y/n!')
    length = tryInputData(getPositiveNumber,
                          'Введите длину пароля:',
                          'Ошибка, введите целое положительное число!')

    # генерим пар
    password = generatePassword(doUseLowercase, doUseUppercase,
                                doUseSpecialSymbols, doUseNumbers,
                                length)

    # доп. отступ
    print()

    print(f'Ваш пароль: {password}')


terminalInterfaceGenPass()
