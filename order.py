import time

class Order:
    def __init__(self, number, sum, note, phone, usual_cutlery, teaching_cutlery, paid_status):
        self.__order_number = number
        self.__order_date = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())
        self.__client_phone = phone
        self.__order_list = list()
        self.__order_sum = sum
        self.__order_note = note
        self.__usual_cutlery = usual_cutlery
        self.__teaching_cutlery = teaching_cutlery
        self.__paid_status = paid_status
        self.__changed_status = " "

    def get_order_date(self):
        return self.__order_date

    def get_changed_status(self):
        return self.__changed_status

    def get_order_sum(self):
        self.__order_sum = 0
        for i in self.__order_list:
            self.__order_sum += i.get_amount() * i.get_price_without_discount()
        return self.__order_sum

    def get_order_number(self):
        return self.__order_number

    def get_order_client(self):
        return self.__order_client

    def get_order_list(self):
        return self.__order_list

    def get_usual_cutlery(self):
        return self.__usual_cutlery

    def get_teaching_cutlery(self):
        return self.__teaching_cutlery

    def get_order_note(self):
        return self.__order_note

    def get_paid_status(self):
        return self.__paid_status

    def get_phone_number(self):
        return self.__client_phone

    def set_order_number(self, number):
        self.__order_number = number

    def set_order_client(self, client):
        self.__order_client = client

    def set_changed_order_status(self, status):
        if status == 1:
            self.__changed_status = "Заказ увеличен"
        elif status == 2:
            self.__changed_status = "Заказ уменьшен"
        elif status == 3:
            self.__changed_status = "Заказ удален"
        else:
            self.__changed_status = " "

    def fill_list(self, position):
        self.__order_list.append(position)

