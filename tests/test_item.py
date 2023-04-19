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
