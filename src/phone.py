from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, support_sim: int):
        super().__init__(name, price, quantity)
        self.__support_sim = support_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__support_sim})"

    @property
    def number_of_sim(self):
        return self.__support_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        elif not isinstance(value, int):
            raise ValueError('Число должно быть целым (int)')
        else:
            self.__support_sim = value
