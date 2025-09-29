

def C_to_F(c):
    return c * 9 / 5 + 32

def C_to_K(c):
    return c + 273.15


c = float(input('°C temperature: '))

f = C_to_F(c)
k = C_to_K(c)

print(f'{c}°C = {round(f, 2)}°F')
print(f'{c}°C = {round(k, 2)}°K')
