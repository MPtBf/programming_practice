


inp = input('Enter a string: ').lower()

symbols = {}
for s in inp:
    if not symbols.get(s):   symbols[s] = 0
    symbols[s] += 1

symbolsItemsSorted = sorted(symbols.items(), key = lambda x: -x[1])
symbolsSorted = list(map(lambda x: x[0], symbolsItemsSorted))
threeMostFrequentSymbols = symbolsSorted[:3]

print(', '.join(threeMostFrequentSymbols))
















