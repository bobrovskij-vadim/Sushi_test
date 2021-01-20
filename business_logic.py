import read_from_file
import position
import order
import orders_list
import write_to_file
import printout

class Business_logic():
    def __init__(self):
        self.__position_list = read_from_file.Read_from_file(".xlsx\\database.xlsx").get_position_list()
        #self.__position_list = read_from_file.Read_from_file("database.xlsx").get_position_list()
        self.__order_sum = 0
        self.__order_number = 0
        self.__day_orders = orders_list.Order_list()

    def add_position(self, position, amount, discount):
        self.__order_sum = 0
        for i in self.__position_list:
            if int(position) == int(i.get_position()):
                i.set_amount(int(amount))
                i.set_discount(int(discount))
            self.__order_sum += i.get_amount() * i.get_price()

    def set_main_discount(self, discount):
        self.__order_sum = 0
        for i in self.__position_list:
            if i.get_amount() != 0:
                i.set_discount(int(discount))
            self.__order_sum += i.get_amount() * i.get_price()


    def del_position(self, position, amount):
        self.__order_sum = 0
        for i in self.__position_list:
            if int(position) == int(i.get_position()):
                i.change_amonut(int(amount))
            self.__order_sum += i.get_amount() * i.get_price()

    def confirm_order(self, note, phone, usual_cutlery, teaching_cutlery, paid_status):
        self.__order_number += 1
        self.__confirmed_order = order.Order(self.__order_number, self.__order_sum, note, phone, usual_cutlery, teaching_cutlery, paid_status)
        for i in self.__position_list:
            if i.get_amount() != 0:
                i_position = i.get_position()
                i_name = i.get_name()
                i_price = i.get_price()
                i_discount = i.get_discount()
                i_amount = i.get_amount()
                temp = position.Position(i_position, i_name, i_price, i_discount, i_amount)
                self.__confirmed_order.fill_list(temp)
        add_to_file = write_to_file.Write_to_file().add_to_month_result(self.get_position_list())
        self.__day_orders.set_orders_dict(self.__order_number, self.__confirmed_order)

        #return self.__confirmed_order

    def get_confirmed_order(self):
        return self.__confirmed_order

    def get_day_orders_list(self):
        return self.__day_orders

    def print_order(self):
        pass
        print_order = "№: "
        # print_order
        # # print_orderjoin(self.__confirmed_order.get_order_number())
        # # print_order.join(self.__confirmed_order.get_order_date())
        # print(print_order)



    def get_total_orders(self):
        return self.__order_number

    def get_order_sum(self):
        return self.__order_sum

    def get_position_list(self):
        return self.__position_list

    def reset_order_sum(self):
        self.__order_sum = 0

    def reset_position_list(self):
        for i in self.__position_list:
            i.reset_amount()
            i.set_discount(0)



