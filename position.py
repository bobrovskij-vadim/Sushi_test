
class Position:
    def __init__(self, position, name, price, discount, amount):
        self.__position = position
        self.__name = name
        self.__price = price
        self.__discount = discount
        self.__amount = amount

    def set_amount(self, amount):
        self.__amount += amount
    def subtract_amount(self, amount):
        self.__amount -= amount
    def reset_amount(self):
        self.__amount = 0
    def change_amonut(self, amount):
        self.__amount -= amount
    def set_discount(self, discount):
        self.__discount = discount

    def get_position(self):
        return self.__position
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price - (self.__price * (self.__discount / 100))
    def get_price_without_discount(self):
        return self.__price
    def get_discount(self):
        return self.__discount

    def get_amount(self):
        return self.__amount
    def get_info(self):
        pass




