
import math

class Abstract_product(object):
    volume_descripton = None
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Purchase_price_total(object):
    def product_price_calc(self, name, price, quantity, q_description):
        if q_description == 'unit(s)' and quantity >= 2:
            total_price = (price * quantity) * 0.95
            print(total_price, 'rubles (with 5% discount) for', quantity, q_description, 'of', name)
        elif q_description == 'kg':
            rounding = math.modf(quantity)
            if rounding[0] > 0.5:
                quantity = rounding[1] + 1
            else:
                quantity = rounding[1]
            total_price = price * quantity
            print(total_price, 'rubles for', quantity, q_description, '(rounded to 50g) of', name)
        else:
            total_price = price * quantity
            print(total_price, 'rubles for', quantity, q_description, 'of', name) #как убрать пробел между суммой и rubles
        return total_price
    

class Product_by_weight(Abstract_product):
    volume_descripton = 'kg'
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    

class Product_by_unit(Abstract_product):
    volume_descripton = 'unit(s)'
    def __init__(self, name, price, unit):
        super().__init__(name, price)
        self.unit = unit


class Product_by_volume(Abstract_product):
    volume_descripton = 'litre'
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume
    
# данные для проврки работы программы
w1 = Product_by_weight('meat', 200, 2.7)
purchase_w1 = Purchase_price_total()
purchase_w1.product_price_calc(w1.name, w1.price, w1.weight, w1.volume_descripton)

u1 = Product_by_unit('chips', 55, 2)
purchase_u1 = Purchase_price_total()
purchase_u1.product_price_calc(u1.name, u1.price, u1.unit, u1.volume_descripton)

v1 = Product_by_volume('pepsi', 45, 3)
purchase_u1 = Purchase_price_total()
purchase_u1.product_price_calc(v1.name, v1.price, v1.volume, v1.volume_descripton)