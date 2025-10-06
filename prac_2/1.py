

from string import punctuation


rusAlph = (''.join(map(lambda i: chr(i), range(ord('а'), ord('я')+1)))
           .replace('е', 'её'))

engAlph = ''.join(map(lambda i: chr(i), range(ord('a'), ord('z')+1)))


def encode(text: str, key: int = 3) -> str:
    """
    Кодирует текст по шифру Цезаря, сдвигая каждую букву на key
    вправо в алфавите
    :param text: Текст для кодировки
    :param key: Число для сдвига каждой буквы в алфавите
    :return: Новый текст со сдвинутыми буквами
    """
    text = list(text)
    # define language of a text
    if text[0].lower() in rusAlph:
        lang = rusAlph
    elif text[0].lower() in engAlph:
        lang = engAlph
    else:
        raise ValueError(
            f'Symbol of unknown language: "{text[0]}". '
            f'Can only encode/decode russian or english text'
        )

    for i, letter in enumerate(text):
        if letter in punctuation + ' ' + '1234567890':
            continue
        if letter.lower() not in lang:
            raise ValueError(f'Cant find "{letter}" in alphabet')
        oldInd = lang.index(letter.lower())
        newLetter = lang[(oldInd + key) % len(lang)]
        if letter.isupper():
            newLetter = newLetter.upper()
        text[i] = newLetter

    return ''.join(text)


def decode(text: str, key: int = 3) -> str:
    """
    Обратное действие к encode(). Декодирует текст по шифру Цезаря,
    сдвигая каждую букву на key влево в алфавите
    :param text: Текст для декодировки
    :param key: Число для сдвига каждой буквы в алфавите
    :return: Новый текст со сдвинутыми буквами
    """
    return encode(text, -key)


inp = 'https://web.telegram.org/a/#-123 123test'
print('Input:', inp)
encoded = encode(inp, key=1)
print('Encoded with key=1:', encoded)
decoded = decode(encoded, key=1)
print('Decoded with key=1:', decoded)
