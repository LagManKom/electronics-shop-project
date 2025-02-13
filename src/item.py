import csv
import os


class InstantiateCSVError(Exception):

    def __int__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.__name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        raise Exception

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Exception: Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls, path='./items.csv'):

        if not os.path.exists(path):
            raise FileNotFoundError('Отсутствует файл items.csv')

        with open(path, 'r', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            correct_name = ['Смартфон', 'Ноутбук', 'Кабель', 'Мышка', 'Клавиатура']
            index = 0
            for row in reader:
                if not row['name'] == correct_name[index]:
                    raise InstantiateCSVError('Файл items.csv поврежден')
                index += 1

        with open(path, 'r', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(data):
        return int(float(data))


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item1.instantiate_from_csv()
