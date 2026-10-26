# tests/test_inventory.py
import pytest
from pages.login_page import LoginPage


def test_catalog_has_6_products(logged_in):
    assert len(logged_in.get_product_names()) == 6


def test_sort_price_low_to_high(logged_in):
    prices = logged_in.sort_by("lohi").get_product_prices()
    assert prices == sorted(prices)


def test_sort_name_z_to_a(logged_in):
    names = logged_in.sort_by("za").get_product_names()
    assert names == sorted(names, reverse=True)


# Доп. 1: для problem_user тест упадёт — это баг в продукте, а не в тесте
@pytest.mark.parametrize("username", ["standard_user", "problem_user"])
def test_sort_works_for_user(driver, username):
    inventory = LoginPage(driver).open_page().login_as_valid_user(username, "secret_sauce")
    names = inventory.sort_by("za").get_product_names()
    assert names == sorted(names, reverse=True)
