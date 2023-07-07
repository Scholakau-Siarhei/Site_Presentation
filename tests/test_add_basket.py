"""Checking what user can ordering pizza"""
import pytest
import allure
from pages.add_basket_page import Basket

@pytest.mark.my_work
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Basket")
@allure.title("Adding a product in to the basket and checking it price")
def test_add_basket(driver):
    add_basket_page = Basket(driver)
    add_basket_page.open_site()
    add_basket_page.close_banner()
    add_basket_page.add_hotdog_board_for_Munich_pizza()
    add_basket_page.add_Munich_pizza_with_hotdog_board_in_basket()
    add_basket_page.open_basket()
    add_basket_page.open_form_order_pizza()
    add_basket_page.input_data_form_order_pizza()
    add_basket_page.confirm_order()
    add_basket_page.assert_confirm_order()
