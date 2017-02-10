

class Product:
    def __init__(self, name, unit, price):
        self.name = name
        self.unit = unit
        self.price = price


class Cart:
    def __init__(self):
        self.cart = []
        self.cart_amount = 0

    # Добавление продуктов в корзину:

    def add(self, p_id, quantity, discount=0):

        # Проверяем, если такой продукт уже в корзине:
        # перезаписываем количество продукта,
        # удаляем предыдущую запись в корзине.

        for i in range(len(self.cart)):
            if p_id.name == self.cart[i][0]:
                quantity = quantity + self.cart[i][3]
                self.cart.pop(i)
            else:
                pass

        # Считаем актуальную скидку и итог на продукт:

        if p_id.unit == 'pieces' and quantity >= 2:
            discount = 0.05
            p_id_amount = round(p_id.price * quantity * (1 - discount), 2)
        else:
            p_id_amount = p_id.price * quantity

        # Записываем данные продукта в корзину с новым количеством и скидкой:

        self.cart.append([p_id.name, p_id.price, p_id.unit, quantity, discount, p_id_amount])

        # Пересчитывем итог корзины:

        self.cart_amount = 0
        for i in range(len(self.cart)):
            self.cart_amount += self.cart[i][5]

    # Форматированная печать чека:

    def check_out(self):
        for i in range(len(self.cart)):
            print('{}'.format(self.cart[i][0]))
            print('{:.2f} * {:.2f} {}'.format(self.cart[i][1], self.cart[i][3], self.cart[i][2]))
            print('{:<5} {:<5.1%} {:>15} {:>10.2f}'.format('disc', self.cart[i][4], '=', self.cart[i][5]), '\n')
        print('{:<25} {} {:>10.2f}'.format('Total amount', '=', self.cart_amount), '\n')


if __name__ == '__main__':

    # Заводим продукты в каталог:

    p_1 = Product('Potato', 'kg', 58.5)
    p_2 = Product('Milk', 'liters', 164)
    p_3 = Product('Bread', 'pieces', 87)
    p_4 = Product('Steak', 'pieces', 950)

    # Добавляем продукты в корзину / пробиваем на кассе:

    cart_1 = Cart()
    cart_1.add(p_1, 2)
    cart_1.add(p_2, 1)
    cart_1.add(p_2, 1)
    cart_1.add(p_3, 1)
    cart_1.add(p_3, 1)
    cart_1.add(p_4, 3)

    # Печатаем чек:

    cart_1.check_out()
