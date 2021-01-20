import time

class Order_list:
    def __init__(self):
        self.__orders_dict = {}
        self.__day_sum = 0
        self.__amount_orders = 0

    def set_orders_dict(self, key, object):
        self.__orders_dict[key] = object

    def get_day_sum(self):
        self.__day_sum = 0
        for key in self.__orders_dict:
            self.__day_sum += self.__orders_dict[key].get_order_sum()
        return self.__day_sum

    def get_amount_orders(self):
        return len(self.__orders_dict)

    def get_orders_dict(self):
        return self.__orders_dict
