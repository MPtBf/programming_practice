"""
1. Создайте модель для онлайн-магазина с
    классами Product, Order, Customer, и
    ShoppingCart.
2. Product включает информацию о цене, наличии
    на складе и категории товара. Order
    обрабатывает процесс покупки, включая расчет
    цены с учетом скидок и налогов.
3. Customer управляет информацией о
    пользователе и его истории заказов.
4. ShoppingCart позволяет добавлять, удалять и
    обновлять количество товаров перед
    оформлением заказа.
"""


class Product:
    """
    Product включает информацию о цене, наличии
    на складе и категории товара.
    """
    def __init__(self, name: str, price: int | float,
                 isInStock: bool, category: str):
        self.name = name
        self.price = price
        self.isInStock = isInStock
        self.category = category


class ShoppingCart:
    """
    ShoppingCart позволяет добавлять, удалять и
    обновлять количество товаров перед
    оформлением заказа.
    """
    def __init__(self):
        self.productsList = []

    def addProduct(self, product, amount):
        if not product.isInStock:
            print(f'Невозможно добавить "{product.name}" в корзину, '
                  f'товар закончился на складе.')
            return
        else:
            print(f'"{product.name}" {amount} шт добавлен в корзину!')
            self.productsList += [product] * amount

    def removeProduct(self, product, amount):
        newProductList = []
        removedAmount = 0
        for p in self.productsList:
            if p == product and amount != 0:
                amount -= 1
                removedAmount += 1
            else:
                newProductList += [p]

        self.productsList = newProductList

        print(f'Удалено {removedAmount} шт "{product.name}" из корзины')


class Customer:
    """
    Customer управляет информацией о
    пользователе и его истории заказов.
    """

    def __init__(self, name: str, email: str, shoppingCart: ShoppingCart):
        self.name = name
        self.email = email
        self.shoppingCart = shoppingCart
        self.balance = 1_000
        self.orderHistory = []

    def addToCart(self, product: Product, amount: int = 1) -> None:
        """
        Функция для добавления amount количества продуктов Product в
        корзину пользователя
        :return: None
        """
        self.shoppingCart.addProduct(product, amount)

    def removeFromCart(self, product: Product, amount: int = -1) -> None:
        """
        Функция для удаления amount количества продуктов Product из
        корзины пользователя. При amount = -1 удаляются все подходящие продукты
        :return: None
        """
        self.shoppingCart.removeProduct(product, amount)

    def depositBalance(self, amount: int | float) -> None:
        """
        Положить amount условных рублей с карты на баланс магазина
        :return: None
        """
        userCardBalance = 50_000  # заменить на реальный счёт банковской карты

        if userCardBalance > amount:
            userCardBalance -= amount
            self.balance += amount
            print(f'Баланс успешно пополнен на {amount}! '
                  f'Новый баланс: {self.balance:.2f}.')
        else:
            print('На карте недостаточно средств')

    def orderProducts(self) -> None:
        """
        Заказать продукты, лежащие в корзине
        :return: None
        """
        order = Order(self)
        orderPrice = order.calcPrice()

        if orderPrice > self.balance:
            print(f'Не хватает денег для оплаты заказа '
                  f'(есть {self.balance:.2f} из {orderPrice:.2f}).')
            return
        else:
            print(f'Заказ на сумму {orderPrice:.2f} успешно оформлен!')
            self.balance -= orderPrice
            self.orderHistory += [{
                'Список продуктов': self.shoppingCart.productsList.copy(),
                'Сумма заказа': orderPrice,
            }]
            self.shoppingCart.productsList = []

    def viewBalance(self):
        """Вывод баланса в консоль"""
        print(f'Ваш баланс: {self.balance:.2f}')

    def viewOrderHistory(self):
        """Вывод истории заказов консоль"""
        print('История заказов:')
        for i, order in enumerate(self.orderHistory):
            print(f' - Заказ №{i+1}:')
            print(' - - Список продуктов:')
            for p in order["Список продуктов"]:
                print(f' - - - "{p.name}", цена: {p.price}')
            print(f' - - Сумма заказа: {order["Сумма заказа"]:.2f}')

    def viewShoppingCart(self):
        """Вывод содержимого корзины консоль"""
        print('Продукты в корзине:')
        for product in self.shoppingCart.productsList:
            print(f' - "{product.name}", цена: {product.price:.2f}')


class Order:
    """
    Обрабатывает процесс покупки, включая расчет
    цены с учетом скидок и налогов.
    """

    def __init__(self, customer: Customer):
        self.customer = customer
        self.shoppingCart = customer.shoppingCart
        self.taxSize = 0.05  # налоги
        self.discount = 0.15

    def applyDiscount(self, totalPrice: int | float) -> float:
        """
        Расчёт скидки при покупке от 500 руб.
        :return: Float - цена после применения скидки
        """
        if totalPrice < 500:
            return totalPrice
        else:
            print(f'Ваша скидка: -{self.discount * 100:.0f}%')
            return totalPrice * (1 - self.discount)

    def calcPrice(self) -> float:
        """
        Вычислить цену заказа
        :return: float
        """
        totalPrice = sum(
            [product.price for product in self.shoppingCart.productsList]
        )

        return self.applyDiscount(totalPrice) * (1 + self.taxSize)


def printComment(*args) -> None:
    """Функция для красивого вывода комментариев в консоль"""
    print('\n-=-=-', *args, '-=-=-\n')


if __name__ == '__main__':
    from pprint import pprint

    # -=-=- -=-=-
    printComment('Доступные продукты')

    products = {
        'Пирожок с картошкой': Product('Пирожок с картошкой', 79,
                                       True, 'Хлебобулочные изделия'),
        'Пирожок с рыбой': Product('Пирожок с рыбой', 129,
                                   False, 'Хлебобулочные изделия'),
        'Мороженое сливочное': Product('Мороженое сливочное', 169,
                                       True, 'Сладости'),
        'Торт шоколадный': Product('Торт шоколадный', 649,
                                   True, 'Сладости'),
        'Помидор': Product('Помидор', 33,
                           True, 'Овощи'),
        'Огурец': Product('Огурец', 39, True, 'Овощи'),
    }
    pprint(products)

    # -=-=- -=-=-
    printComment('Создаём корзину и присваиваем её покупателю')

    shoppingCart = ShoppingCart()
    customer = Customer('Марк', '123123@yandex.ru', shoppingCart)
    print(customer.name, customer.email)

    print()

    # -=-=- -=-=-
    printComment('Просматриваем наш баланс и добавляем товары в корзину')

    customer.viewBalance()

    customer.addToCart(products['Пирожок с картошкой'], 2)
    customer.addToCart(products['Пирожок с рыбой'])
    customer.addToCart(products['Помидор'], 5)

    # -=-=- -=-=-
    printComment('Просматриваем корзину')

    customer.viewShoppingCart()

    # -=-=- -=-=-
    printComment('Заказываем продукты из корзины и смотрим, '
                 'сколько денег у нас осталось')

    customer.orderProducts()

    customer.viewBalance()

    print()

    # -=-=- -=-=-
    printComment('Положим ещё 500 условных рублей на баланс магазина, '
                 'добавим в корзину ещё пару товаров')

    customer.depositBalance(500)

    customer.addToCart(products['Мороженое сливочное'])
    customer.addToCart(products['Торт шоколадный'], 2)

    # -=-=- -=-=-
    printComment('Посмотрим, что у нас в корзине')

    customer.viewShoppingCart()

    # -=-=- -=-=-
    printComment('Заказываем продукты из корзины')

    customer.orderProducts()

    print()

    # -=-=- -=-=-
    printComment('Не хватает денег... Тогда удалим что-нибудь '
                 'из корзины и попробуем заказать снова')

    customer.removeFromCart(products['Торт шоколадный'], 1)

    customer.viewShoppingCart()
    customer.orderProducts()

    print()

    # -=-=- -=-=-
    printComment("Посмотрим историю наших заказов")

    customer.viewOrderHistory()
