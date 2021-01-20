import tkinter as tk
import write_to_file
import save_order_to_file


class Order_history:
    def __init__(self, order_list):
        self.o_h = tk.Tk()
        self.o_h.title("Sushi salon")
        self.o_h.geometry("1000x620")
        #self.o_h.iconbitmap(".ico\\Sushi.ico")
        #self.o_h.iconbitmap("Sushi.ico")

        self.__order_list = order_list

        self.__password = "1234"

        self.verification_label = tk.Label(self.o_h, text="ИЗМЕНИТЬ ЗАКАЗ").place(x=190, y=100)
        self.input_password_label = tk.Label(self.o_h, text="Введите пароль: ").place(x=122, y=138)
        self.verification_password = tk.StringVar()
        self.verification_entry = tk.Entry(self.o_h, textvariable=self.verification_password)
        self.verification_entry.place(x=228, y=140)
        self.verification_button = tk.Button(self.o_h, text="Изменить заказ", command=self.change_order_clicked).place(x=190, y=180)

        self.order_history_label = tk.Label(self.o_h, text="История заказов за день:").place(x=500, y=10)
        self.orders_history_output = tk.Text(self.o_h, state=tk.DISABLED, width=48, height=30)
        self.orders_history_output.place(x=500, y=35)
        self.total_orders_label = tk.Label(self.o_h, text="Количество заказов: ", font="2").place(x=500, y=530)
        self.total_orders_res = tk.StringVar(self.o_h)
        self.total_orders_res.set("0")
        self.total_orders_res_label = tk.Label(self.o_h, textvariable=self.total_orders_res, font="2")  # Вывод общее количество заказов
        self.total_orders_res_label.place(x=800, y=530)
        self.total_orders_sum_label = tk.Label(self.o_h, text="Сумма заказов:", font="2").place(x=500, y=570)
        self.total_orders_sum_res = tk.StringVar(self.o_h)

        self.total_orders_sum_res.set("0")
        self.total_orders_sun_res_label = tk.Label(self.o_h, textvariable=self.total_orders_sum_res, font="2")  # Вывод общей суммы заказов
        self.total_orders_sun_res_label.place(x=800, y=570)

        self.fill_text_widget()

        self.wrong_password = tk.StringVar(self.o_h)
        self.wrong_password_label = tk.Label(self.o_h, textvariable=self.wrong_password).place(x=150, y=230)

        self.print_order_label = tk.Label(self.o_h, text="РАСПЕЧАТАТЬ ЗАКАЗ").place(x=185, y=478)
        self.print_order_number_label = tk.Label(self.o_h, text="Введите номер заказ: ").place(x=187, y=507)
        self.print_num = tk.StringVar()
        self.print_entry = tk.Entry(self.o_h, textvariable=self.print_num, width=20)
        self.print_entry.place(x=186, y=533)
        self.print_button = tk.Button(self.o_h, text="Печатать заказ", command=self.print_order, width=20).place(x=174, y=560)

        self.o_h.mainloop()

    def change_order_clicked(self):
        password = self.verification_entry.get()
        if password == self.__password:
            self.wrong_password.set("")
            input_order_number_label = tk.Label(self.o_h, text="Номер заказ: ").place(x=122, y=228)
            self.order_number = tk.StringVar(self.o_h)
            input_order_number_entry = tk.Entry(self.o_h, textvariable=self.order_number, width=20)
            input_order_number_entry.place(x=228, y=230)
            input_position_number_label = tk.Label(self.o_h, text="Номер позиции: ").place(x=122, y=258)
            self.position = tk.StringVar(self.o_h)
            input_position_number_entry = tk.Entry(self.o_h, textvariable=self.position, width=20)
            input_position_number_entry.place(x=228, y=260)
            input_amount_label = tk.Label(self.o_h, text="Количество:").place(x=122, y=288)
            self.amount = tk.StringVar(self.o_h)
            input_amount_entry = tk.Entry(self.o_h, textvariable=self.amount, width=20)
            input_amount_entry.place(x=228, y=290)
            self.add_button = tk.Button(self.o_h, text="Добавить", width=12, command=self.add_to_the_order).place(x=93, y=320)
            self.del_button = tk.Button(self.o_h, text="Удалить", width=12, command=self.del_from_the_order).place(x=193, y=320)
            self.del_order_button = tk.Button(self.o_h, text="Удалить заказ", width=12, command=self.del_the_order).place(x=293, y=320)
        else:
            self.wrong_password.set("Неверный пароль!")

    def fill_text_widget(self):                                   # Метод заполняет историей заказов текстовый виджет
        self.orders_history_output.configure(state=tk.NORMAL)     # Активирует виджет text для печати
        self.clear_text_output()
        total_sum = 0
        for key in self.__order_list.get_orders_dict():
            self.orders_history_output.insert(tk.END, f'{"№:"} {self.__order_list.get_orders_dict()[key].get_order_number()} / ')
            self.orders_history_output.insert(tk.END, f'{self.__order_list.get_orders_dict()[key].get_order_date()} ')
            self.orders_history_output.tag_config('my', foreground='red', font=("Arial", 9, 'bold'))
            self.orders_history_output.insert(tk.END, self.__order_list.get_orders_dict()[key].get_changed_status(), 'my')
            paid_status = ""
            if self.__order_list.get_orders_dict()[key].get_paid_status():
                paid_status = "Оплачен"
            else:
                paid_status = " - "
            count = 0
            for i in self.__order_list.get_orders_dict()[key].get_order_list():
                count += 1
                sum = i.get_amount() * i.get_price_without_discount()
                self.orders_history_output.insert(tk.END, f'\n{count}{"."} {int(i.get_position())} {i.get_name()}/ {i.get_discount()}/ {i.get_amount()}/ {i.get_price_without_discount()}/ {sum}')
                total_sum += sum
            self.orders_history_output.insert(tk.END, f'\n{"Итого: "} {total_sum}\n{"Приборы: обычные "}{self.__order_list.get_orders_dict()[key].get_usual_cutlery()} {"учебные "}{self.__order_list.get_orders_dict()[key].get_teaching_cutlery()}\n{"Статус оплаты: "}{paid_status}\n{"Телефон клиента: "}{self.__order_list.get_orders_dict()[key].get_phone_number()} \n{"Примечание:"}{self.__order_list.get_orders_dict()[key].get_order_note()}{"------------------------------------------------"}\n')
            total_sum = 0
        self.orders_history_output.configure(state=tk.DISABLED)
        self.total_orders_res.set(self.__order_list.get_amount_orders())
        self.total_orders_sum_res.set(self.__order_list.get_day_sum())

    def clear_text_output(self):
        self.orders_history_output.delete("1.0", "end")

    def add_to_the_order(self):
        changed_order_number = self.order_number.get()
        changed_position = self.position.get()
        changed_amount = self.amount.get()
        if int(changed_order_number) in self.__order_list.get_orders_dict():
            self.__order_list.get_orders_dict()[int(changed_order_number)].set_changed_order_status(1)
            for i in self.__order_list.get_orders_dict()[int(changed_order_number)].get_order_list():
                if i.get_position() == int(changed_position):
                    add_to_file = write_to_file.Write_to_file().save_changed_order(i, changed_amount)
                    i.set_amount(int(changed_amount))
        save_order = save_order_to_file.Save_order(self.__order_list.get_orders_dict()[int(changed_order_number)])
        self.fill_text_widget()

    def del_from_the_order(self):
        changed_order_number = self.order_number.get()
        changed_position = self.position.get()
        changed_amount = self.amount.get()
        sub_amount = 0 - int(changed_amount)
        if int(changed_order_number) in self.__order_list.get_orders_dict():
            self.__order_list.get_orders_dict()[int(changed_order_number)].set_changed_order_status(2)
            for i in self.__order_list.get_orders_dict()[int(changed_order_number)].get_order_list():
                if i.get_position() == int(changed_position):
                    add_to_file = write_to_file.Write_to_file().save_changed_order(i, sub_amount)
                    i.subtract_amount(int(changed_amount))
        save_order = save_order_to_file.Save_order(self.__order_list.get_orders_dict()[int(changed_order_number)])
        self.fill_text_widget()

    def del_the_order(self):
        changed_order_number = self.order_number.get()
        if int(changed_order_number) in self.__order_list.get_orders_dict():
            self.__order_list.get_orders_dict()[int(changed_order_number)].set_changed_order_status(3)
            for i in self.__order_list.get_orders_dict()[int(changed_order_number)].get_order_list():
                amount = -int(i.get_amount())
                i.reset_amount()
                add_to_file = write_to_file.Write_to_file().save_changed_order(i, amount)
        save_order = save_order_to_file.Save_order(self.__order_list.get_orders_dict()[int(changed_order_number)])
        self.fill_text_widget()

    def print_order(self):
        pass