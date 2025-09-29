

inp = input('Enter a number: ')
n = int(inp)


if n % 2 == 0:   print(n, '- чётное')
else:            print(n, '- нечётное')

if   n > 0:    print(n, '- положительное')
elif n == 0:   print(n, '- ноль')
else:          print(n, '- отрицательное')

if 10 <= n <= 50:   print(n, '- принадлежит [10; 50]')
else:               print(n, '- не принадлежит [10; 50]')
