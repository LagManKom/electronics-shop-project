from src.item import Item
import random


class Mixin:
    def __init__(self):
        self.__lang = "EN"

    def change_lang(self):
        """Change the language from ["RU", "EN"]
        to anything non-equal to the current language
        """
        for challenger in ["RU", "EN"]:
            if self.__lang != challenger:
                self.__lang = challenger
                break
        return self

    @property
    def language(self):
        return self.__lang


class KeyBoard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
