import openpyxl
import position
from position import Position

class Read_from_file:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__book = openpyxl.open(self.__file_name, read_only=True)
        self.__sheet = self.__book.active
        self.__position_list = list()


        for row in range(2, 162):     # Разобраться почему не работает sheet.max_row
            pos = self.__sheet[row][0].value
            name = self.__sheet[row][1].value
            price = self.__sheet[row][2].value
            discount = self.__sheet[row][3].value
            amount = self.__sheet[row][4].value
            unit = position.Position(pos, name, price, discount, amount)
            self.__position_list.append(unit)

        self.__book.close()

    def get_position_list(self):
        return self.__position_list

# Читает из файла товаров позиции и создает массив





