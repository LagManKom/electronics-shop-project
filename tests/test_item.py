"""Nесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item('Xiaomi', 10000, 2)


def test_item_calculate(item):
    assert item.calculate_total_price() == 20000


def test_apply_discount(item):
    item.pay_rate = 0.50
    item.apply_discount()

    assert item.calculate_total_price() == 10000


def test_name(item):
    assert item.name == 'Xiaomi'


def test_name_setter(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_instantiate_form_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 9
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    # with pytest.raises(Exception):


def test_repr_str(item):
    assert repr(item) == "Item('Xiaomi', 10000, 2)"
    assert str(item) == 'Xiaomi'
