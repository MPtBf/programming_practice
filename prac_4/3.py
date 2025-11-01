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


# online store


class Product:
    """
    Product включает информацию о цене, наличии
    на складе и категории товара.
    """
    def __init__(self, name, price, isInStock, category):
        self.name = name
        self.price = price
        self.isInStock = isInStock
        self.category = category


class Order:
    """
    Order
    обрабатывает процесс покупки, включая расчет
    цены с учетом скидок и налогов.
    """
    def __init__(self, customer):
        self.customer = customer
        self.shoppingCart = customer.shoppingCart
        self.taxSize = 0.05  # налоги

    def applyDiscount(self, totalPrice):
        # расчёт скидки: -15% при покупке от 500 руб
        if totalPrice < 500:
            return totalPrice
        else:
            print('Ваша скидка: -15%')
            return totalPrice * 0.85

    def calcPrice(self):
        totalPrice = sum([product.price for product in self.shoppingCart.productsList])

        return self.applyDiscount(totalPrice) * (1 + self.taxSize)


class Customer:
    """
    Customer управляет информацией о
    пользователе и его истории заказов.
    """
    def __init__(self, name, email, shoppingCart):
        self.name = name
        self.email = email
        self.shoppingCart = shoppingCart
        self.balance = 1_000
        self.orderHistory = []

    def addToCart(self, product, amount=1):
        self.shoppingCart.addProduct(product, amount)

    def removeFromCart(self, product, amount=-1):
        self.shoppingCart.removeProduct(product, amount)

    def depositBalance(self, amount):
        if 'на карте пользователя достаточно денег':
            self.balance += amount
            print(f'Баланс успешно пополнен на {amount}! Новый баланс: {self.balance:.2f}.')
            # списать amount с карты
        else:
            print('На карте недостаточно средств')

    def orderProducts(self):
        order = Order(self)
        orderPrice = order.calcPrice()

        if orderPrice > self.balance:
            print(f'Не хватает денег для оплаты заказа (есть {self.balance:.2f} из {orderPrice:.2f}).')
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
        print(f'Ваш баланс: {self.balance:.2f}')

    def viewOrderHistory(self):
        print('История заказов:')
        for i, order in enumerate(self.orderHistory):
            print(f' - Заказ №{i+1}:')
            print(f' - - Список продуктов:')
            for p in order["Список продуктов"]:
                print(f' - - - "{p.name}", цена: {p.price}')
            print(f' - - Сумма заказа: {order["Сумма заказа"]:.2f}')

    def viewShoppingCart(self):
        print('Продукты в корзине:')
        for product in self.shoppingCart.productsList:
            print(f' - "{product.name}", цена: {product.price:.2f}')



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
            print(f'Невозможно добавить "{product.name}" в корзину, товар закончился на складе.')
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





products = {
    'Пирожок с картошкой': Product('Пирожок с картошкой', 79, True, 'Хлебобулочные изделия'),
    'Пирожок с рыбой': Product('Пирожок с рыбой', 129, False, 'Хлебобулочные изделия'),
    'Мороженое сливочное': Product('Мороженое сливочное', 169, True, 'Сладости'),
    'Торт шоколадный': Product('Торт шоколадный', 649, True, 'Сладости'),
    'Помидор': Product('Помидор', 33, True, 'Овощи'),
    'Огурец': Product('Огурец', 39, True, 'Овощи'),
}

shoppingCart = ShoppingCart()
customer = Customer('Марк', '123123@yandex.ru', shoppingCart)


customer.viewBalance()

customer.addToCart(products['Пирожок с картошкой'], 2)
customer.addToCart(products['Пирожок с рыбой'])
customer.addToCart(products['Помидор'], 5)

customer.viewShoppingCart()
customer.orderProducts()

customer.viewBalance()

print()

customer.depositBalance(500)

customer.addToCart(products['Мороженое сливочное'])
customer.addToCart(products['Торт шоколадный'], 2)

customer.viewShoppingCart()
customer.orderProducts()

print()

customer.removeFromCart(products['Торт шоколадный'], 1)

customer.viewShoppingCart()
customer.orderProducts()

print()

customer.viewOrderHistory()



