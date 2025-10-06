

from faker import Faker


fake = Faker('ru_RU')  # Русская локаль


def hideWord(originalWord: str, guessedLetters: str) -> str:
    """
    Заменить все символы в слове, кроме guessedLetters на "-"
    :param originalWord: оригинальное слово
    :param guessedLetters: уже названные пользователем буквы
    :return: str, скрытое слово
    """

    hiddenWord = ''
    for letter in originalWord:
        if letter in guessedLetters:
            hiddenWord += letter
        else:
            hiddenWord += '-'

    return hiddenWord


def terminalHangmanGame():
    """
    Игра виселица в терминале
    :return: None
    """

    randWord = fake.word()
    guessedLetters = ''
    guessesNum = 1

    while True:
        print(f'Слово: {hideWord(randWord, guessedLetters)} '
              f'({len(randWord)} букв)')
        inp = input(f'Попытка {guessesNum}. Выберите букву: ').lower()[0]

        if inp in guessedLetters:
            print(f'Вы уже называли эту букву, как и: '
                  f'{", ".join(guessedLetters)}')
            print()
            continue
        guessedLetters += inp

        if inp in randWord:
            print('Вы угадали букву!')
        else:
            print('Вы не угадали букву.')
        print()

        guessesNum += 1

        if hideWord(randWord, guessedLetters) == randWord:
            break

    print(f'Вы выиграли за {guessesNum} попыток!')
    print(f'Слово было: {randWord}')


terminalHangmanGame()
