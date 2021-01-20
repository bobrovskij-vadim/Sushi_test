import tkinter as tk
from tkinter import ttk
import business_logic
import order_history
import save_order_to_file

class Graphic_interface:

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Sushi salon")
        self.main_window.geometry("1200x620")
        #self.main_window.iconbitmap(".ico\\Sushi.ico")
        #self.main_window.iconbitmap("Sushi.ico")

        self.__position_list = business_logic.Business_logic()

    # Блок Add
        self.add_label = tk.Label(self.main_window, text="Добавить", font="10").place(x=10, y=10)
        self.discount_label = tk.Label(self.main_window, text="Скидка:").place(x=10, y=45)
    # Блок радиобатонов для скидок
        self.radio_var = tk.IntVar()

        self.discount_0_rb = tk.Radiobutton(self.main_window, text="0%", variable=self.radio_var, value=0).place(x=60, y=45)
        self.discount_10_rb = tk.Radiobutton(self.main_window, text="10%", variable=self.radio_var, value=10).place(x=120, y=45)
        self.discount_15_rb = tk.Radiobutton(self.main_window, text="15%", variable=self.radio_var, value=15).place(x=180, y=45)
        self.discount_20_rb = tk.Radiobutton(self.main_window, text="20%", variable=self.radio_var, value=20).place(x=240, y=45)
        self.discount_100_rb = tk.Radiobutton(self.main_window, text="100%", variable=self.radio_var, value=100).place(x=300, y=45)

        self.operator_name_label = tk.Label(self.main_window, text="Оператор:").place(x=260, y=10)
        self.operator_name = tk.StringVar()
        self.operator_name_entry = tk.Entry(self.main_window, textvariable=self.operator_name, width="25")
        self.operator_name_entry.place(x=330, y=11)

        self.add_amount_label = tk.Label(self.main_window, text="Кол-во:").place(x=10, y=75)
        self.add_position_label = tk.Label(self.main_window, text="Позиция:").place(x=70, y=75)
    # Блок полей и кнопок добавить
        self.amount = tk.StringVar(self.main_window)
        self.amount.set('1')
        self.add_amount_spinbox = tk.Spinbox(self.main_window, from_=1, to=1000, width=5, textvariable=self.amount)
        self.add_amount_spinbox.place(x=10, y=100)
        self.position = tk.StringVar()
        self.add_position_entry = tk.Entry(self.main_window, textvariable=self.position, width=10)
        self.add_position_entry.place(x=70, y=100)
        self.add_button = tk.Button(self.main_window, text = "Добавить", width=14, command=self.add_button_clicked).place(x=144, y=96)
        self.del_button = tk.Button(self.main_window, text="Удалить", width=14, command=self.del_button_clicked).place(x=256, y=96)
        self.reset_order_button = tk.Button(self.main_window, text="Сбросить заказ", width=15, command=self.reset_order_button_clicked).place(x=370, y=96)

        # Блок table
        self.order_output_tree = ttk.Treeview(self.main_window)                                                         # Определение таблицы
        self.order_output_tree['columns'] = ("Pos", "Name", "Discount", "Amount", "Price", "Sum")                       # Определение колонок
    # Формат колонок
        self.order_output_tree.column("#0", anchor=tk.CENTER, width=30)
        self.order_output_tree.column("Pos", anchor=tk.CENTER, width=40)
        self.order_output_tree.column("Name", anchor=tk.W, width=200)
        self.order_output_tree.column("Discount", anchor=tk.W, width=50)
        self.order_output_tree.column("Amount", anchor=tk.W, width=50)
        self.order_output_tree.column("Price", anchor=tk.W, width=50)
        self.order_output_tree.column("Sum", anchor=tk.W, width=52)
    # Создание заголовков таблицы
        self.order_output_tree.heading("#0", text="№", anchor=tk.CENTER)
        self.order_output_tree.heading("Pos", text="Поз", anchor=tk.CENTER)
        self.order_output_tree.heading("Name", text="Наименование", anchor=tk.CENTER)
        self.order_output_tree.heading("Discount", text="Скидка", anchor=tk.CENTER)
        self.order_output_tree.heading("Amount", text="Кол-во", anchor=tk.CENTER)
        self.order_output_tree.heading("Price", text="Цена", anchor=tk.CENTER)
        self.order_output_tree.heading("Sum", text="Сумма", anchor=tk.CENTER)

        self.order_sum_label = tk.Label(self.main_window, text="Итого:", font="2").place(x=320, y=418)
        self.order_sum = tk.StringVar()
        self.order_sum.set("0")
        self.order_result_label = tk.Label(self.main_window, textvariable=self.order_sum, font="2").place(x=390, y=418)
        self.order_output_tree.place(x=10, y=130)
    # Блок примечание
        self.note_order_label = tk.Label(self.main_window, text="ПРИМЕЧАНИЕ К ЗАКАЗУ:").place(x=10, y=358)
        self.note_order = tk.Text(self.main_window, width=59, height=2)
        self.note_order.place(x=10, y=380)
    # Кнопка оформления заказ
        self.checkout_button = tk.Button(self.main_window, text="Оформить заказ", background="green", width=30, font="2", command=self.checkout_button_clicked).place(x=80, y=565)

    #Скидка постфактум
        self.main_discount_label = tk.Label(self.main_window, text="Дать единую скидку по заказу:").place(x=10, y=455)
        self.main_discount = tk.StringVar(self.main_window)
        self.main_discount_entry = tk.Entry(self.main_window, textvariable=self.main_discount, width=22)
        self.main_discount_entry.place(x=190, y=457)
        self.main_discount_button = tk.Button(self.main_window, text="Дать скидку", width=20, command=self.main_discount_clicked).place(x=338, y=453)

    # Блок информация клиента
        self.usual_cutlery_label = tk.Label(self.main_window, text="КОЛИЧЕСТВО ПРИБОРОВ:   обычные ").place(x=10, y=493)
        self.usual_cutlery_entry = tk.Entry(self.main_window, width="15")
        self.usual_cutlery_entry.place(x=230, y=494)
        self.teaching_cutlery_label = tk.Label(self.main_window, text="учебные").place(x=332, y=494)
        self.teaching_cutlery_entry = tk.Entry(self.main_window, width="15")
        self.teaching_cutlery_entry.place(x=393, y=495)

        self.client_ID_label = tk.Label(self.main_window, text="ID клиента(телефон)").place(x=10, y=527)
        self.ID_client_entry = tk.Entry(self.main_window, width="25")
        self.ID_client_entry.place(x=140, y=531)

        self.was_paid = tk.BooleanVar()
        self.paid_status = tk.Checkbutton(self.main_window, text="Оплачено", variable = self.was_paid, onvalue=1, offvalue=0)
        self.paid_status.place(x=380, y=528)

    #Средний блок
        self.order_history_button = tk.Button(self.main_window, text="История заказов", width=20, command=self.order_history_button_clicked).place(x=540, y=570)

    #Блок количество и сумма закзазов
        self.total_orders_label = tk.Label(self.main_window, text="Количество заказов: ", font="2").place(x=800, y=530)
        self.total_orders_res = tk.StringVar()
        self.total_orders_res.set("0")
        self.total_orders_res_label = tk.Label(self.main_window, textvariable=self.total_orders_res, font="2") # Вывод общее количество заказов
        self.total_orders_res_label.place(x=1100, y=530)
        self.total_orders_sum_label = tk.Label(self.main_window, text="Сумма заказов:", font="2").place(x=800, y=570)
        self.total_orders_sum_res = tk.StringVar()
        self.total_orders_sum_res.set("0")
        self.total_orders_sun_res_label = tk.Label(self.main_window, textvariable=self.total_orders_sum_res, font="2") # Вывод общей суммы заказов
        self.total_orders_sun_res_label.place(x=1100, y=570)

    # Блок кнопок сетка
        frame_main = tk.Frame(self.main_window)
        frame_main.place(x=550, y=10)

        canvas = tk.Canvas(frame_main, width=566, height=508)
        canvas.grid(row=0, column=0)

        vsb = tk.Scrollbar(frame_main, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)

        frame_button = tk.Frame(canvas)
        canvas.create_window((1, 0), window=frame_button, anchor='nw')

        buttons_list = list()
        for i in self.__position_list.get_position_list():
            b = tk.Button(frame_button, text=i.get_name(), width="20", font=('Arial', 12), command=lambda i=i: self.add_button_list_clicked(i.get_position()))
            buttons_list.append(b)
        r = 0
        c = 0
        for i in buttons_list:
            i.grid(row=r, column=c)
            c += 1
            if c == 3:
                r += 1
                c = 0

        frame_button.update_idletasks()
        frame_main.config(width=1, height=1)
        canvas.config(scrollregion=canvas.bbox("all"))

        self.main_window.mainloop()

    def cout_to_output_tree(self):        # Функция вывода списка заказ в таблицу
        self.order_output_tree.delete(*self.order_output_tree.get_children())
        count = 1
        for i in self.__position_list.get_position_list():
            if int(i.get_amount()) != 0:
                sum = i.get_amount() * i.get_price()
                self.order_output_tree.insert('', 'end', text=count, values=(
                int(i.get_position()), i.get_name(), i.get_discount(), i.get_amount(), i.get_price(), sum))
                count += 1

    def add_button_clicked(self):                                         # Реализация кнопки добавления позиции в предварительный заказ
        amount = self.add_amount_spinbox.get()
        position = self.position.get()
        discount = self.radio_var.get()
        discount_indicator = tk.StringVar()
        self.discount_label = tk.Label(self.main_window, textvariable=discount_indicator, foreground="red", font=10).place(x=380, y=43)
        if discount > 0:
            discount_indicator.set("Скидка")
        else:
            discount_indicator.set("           ")
        self.__position_list.add_position(position, amount, discount)
        self.order_sum.set(self.__position_list.get_order_sum())           # Вывод суммы заказа
        self.cout_to_output_tree()                                         # Вызов функции вывода в таблицу
        self.amount.set('1')
        self.add_position_entry.delete(0, tk.END)                          # Очистка поля ввода номера позиции

    def add_button_list_clicked(self, position):                           # Добавление позиции через сетку кнопок
        amount = self.add_amount_spinbox.get()
        discount = self.radio_var.get()
        discount_indicator = tk.StringVar()
        self.discount_label = tk.Label(self.main_window, textvariable=discount_indicator, foreground="red", font=10).place(x=380, y=43)
        if discount > 0:
            discount_indicator.set("Скидка")
        else:
            discount_indicator.set("           ")
        self.__position_list.add_position(int(position), amount, discount)
        self.order_sum.set(self.__position_list.get_order_sum())  # Вывод суммы заказа
        self.cout_to_output_tree()  # Вызов функции вывода в таблицу
        self.amount.set('1')
        self.add_position_entry.delete(0, tk.END)  # Очистка поля ввода номера позиции

    def del_button_clicked(self):                                          # Реализация кнопки удаления позиции либо количеста из предварительного заказ
        amount = self.add_amount_spinbox.get()
        position = self.position.get()
        self.__position_list.del_position(position, amount)
        self.order_sum.set(self.__position_list.get_order_sum())
        self.cout_to_output_tree()
        self.add_position_entry.delete(0, tk.END)                          # Очистка поля ввода номера позиции

    def main_discount_clicked(self):
        discount = self.main_discount.get()
        self.__position_list.set_main_discount(discount)
        self.cout_to_output_tree()
        self.order_sum.set(self.__position_list.get_order_sum())
        self.main_discount_entry.delete(0, tk.END)

    def checkout_button_clicked(self):                                     # Подтверждение закза
        note = self.note_order.get(1.0, tk.END)
        usual_cutlery = self.usual_cutlery_entry.get()
        teaching_cutlery = self.teaching_cutlery_entry.get()
        phone = self.ID_client_entry.get()
        paid_status = self.was_paid.get()
        self.__position_list.confirm_order(note, phone, usual_cutlery, teaching_cutlery, paid_status)
        self.total_orders_res.set(self.__position_list.get_day_orders_list().get_amount_orders())  # Вывод общее количество заказов
        self.total_orders_sum_res.set(self.__position_list.get_day_orders_list().get_day_sum())    # Вывод общей суммы заказов
        self.save_order_to_file = save_order_to_file.Save_order(self.__position_list.get_confirmed_order())
        self.reset_order_button_clicked()

    def reset_order_button_clicked(self):                                   # Сбросить заказ
        self.__position_list.reset_position_list()
        self.__position_list.reset_order_sum()
        self.order_sum.set("0")
        self.order_output_tree.delete(*self.order_output_tree.get_children())
        self.note_order.delete(1.0, tk.END)

    def order_history_button_clicked(self):                                # Кнопка истории заказов
        or_history = order_history.Order_history(self.__position_list.get_day_orders_list())







