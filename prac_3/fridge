
import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'
def is_valid_date(date_string, date_format):
    try:
        datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False



def add(items, title, amount, expiration_date=None):

    if expiration_date is not None:
        dateParsed = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    else: dateParsed = None

    if items.get(title):
        items[title].append({
            'amount': amount,
            'expiration_date': dateParsed,
        })
    else:
        items[title] = [{
            'amount': amount,
            'expiration_date': dateParsed,
        }]

def add_by_note(items, note):
    parts = note.split()

    expiration_date = parts[-1]

    if is_valid_date(expiration_date, DATE_FORMAT):
        dateParsed = datetime.datetime.strptime(expiration_date, DATE_FORMAT)
        amount = Decimal(parts[-2])
        title = ' '.join(parts[0:-2])
    else:
        dateParsed = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[0:-1])
        expiration_date = None

    add(items, title, amount, expiration_date)

def find(items, needle):
    result_items = []

    for key in items.keys():
        keyLower = key.lower()
        if needle.lower() in keyLower:
            result_items += [key]

    return result_items

def amount(items, needle):
    needleItems = find(items, needle)

    totalAmount = 0
    for key ,val in items.items():
        if key in needleItems:
            for v in val:
                totalAmount += v['amount']

    return Decimal(str(totalAmount))





goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 9, 30)}
    ]
}

print('Старый список продуктов:', goods)
print()


# Пользователь купил ещё два килограмма пельменей с тем же названием.
# Добавляем покупку в словарь goods:
add(goods, 'Пельмени Универсальные', Decimal('2'), '2023-10-28')


print('Новый список продуктов:', goods)

