
from random import choice, randint
from string import ascii_uppercase


special_symbols_str = '!@#$%^&*'

def letter():          return choice(ascii_uppercase)
def number():          return str(randint(0,9))
def specialSymbol():   return choice(special_symbols_str)

pas = letter() + letter() + letter() + \
      number() + number() + number() + \
      specialSymbol() + specialSymbol()


print('Случайный пароль:', pas)







