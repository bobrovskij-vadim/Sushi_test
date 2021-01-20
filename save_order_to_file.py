import time
import io
import orders_list

class Save_order:
    def __init__(self, order):
        self.__date = time.strftime("%Y-%m-%d", time.localtime())
        extension = ".txt"
        self.__file_name = self.__date + extension
        self.__order = order
        self.add_order()

    def add_order(self):
        with io.open(self.__file_name, 'a', encoding="utf-8") as file:
            str_num_date_status = "#: " + str(self.__order.get_order_number()) + " / " + self.__order.get_order_date() + " " + self.__order.get_changed_status() + "\n"
            file.write(str_num_date_status)
            count = 0
            total_sum = 0
            for i in self.__order.get_order_list():
                count += 1
                sum = i.get_amount() * i.get_price_without_discount()
                str_position_list = str(count) + ". " + str(i.get_position()) + " " + i.get_name() + " / " + str(i.get_discount()) + " / " + str(i.get_amount()) + " / " + str(i.get_price_without_discount()) + " / " + str(sum) + "\n"
                file.write(str_position_list)
                total_sum += sum
            str_total_sum = "Итого: " + str(total_sum) + "\n"
            file.write(str_total_sum)
            str_cutlery = "Приборы: " + str(self.__order.get_usual_cutlery()) + " обычные " + str(self.__order.get_teaching_cutlery()) + " учебные" + "\n"
            file.write(str_cutlery)
            str_phone = "Телефон клиента: " + str(self.__order.get_phone_number()) + "\n"
            file.write(str_phone)
            str_note = "Примечение: " + self.__order.get_order_note() + "\n" + "--------------------------------------------------" + "\n"
            file.write(str_note)


