"""Functions for Basket page"""

import random
import time
import allure
from faker import Faker
from pages.base_page import BasePage
from pages.locators import locators_base_page, locators_add_basket


class Basket(BasePage):
    """Methods for checking the addition of an item to the basket"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_site(self):
        with allure.step("Go to general page"):
            self.driver.get('https://dominos.by/')

    def close_banner(self):
        with allure.step("Close banner"):
            if self.is_element_visible(locators_base_page.btn_close_banner):
                self.find_element(locators_base_page.btn_close_banner).click()
            else:
                pass
            time.sleep(1)

    def add_hotdog_board_for_Munich_pizza(self):
        with allure.step("Add hot-dog board for Munich pizza"):
            self.find_element(locators_add_basket.btn_add_hotdog_board).click()
            time.sleep(1)

    def add_Munich_pizza_with_hotdog_board_in_basket(self):
        with allure.step("Add Munich pizza with hot-dog board in the basket"):
            self.find_element(locators_add_basket.btn_add_to_basket_munich).click()
            time.sleep(1)

    def open_basket(self):
        with allure.step("Open basket"):
            self.find_element(locators_add_basket.btn_basket).click()
            time.sleep(1)

    def open_form_order_pizza(self):
        with allure.step("Opening form-order of pizza"):
            self.find_element(locators_add_basket.btn_open_form_order_pizza).click()
            time.sleep(1)

    def input_data_form_order_pizza(self):
        fake = Faker("ru_RU")
        """Input valid data in the form-order of pizza"""
        #street
        with allure.step("Input street"):
            time.sleep(2)
            self.driver.execute_script(
            """var element = document.querySelector('.custom-field-text[data-test="custom-field-text"]');
                if (element) {
                  element.click();
                } else {
                  console.log('Элемент не найден');}
            """
            )
            time.sleep(1)
            self.find_element(locators_add_basket.btn_search_field_street).send_keys("левкова")
            time.sleep(1)
            self.find_element(locators_add_basket.btn_change_street).click()
            time.sleep(1)
        #house
        with allure.step("Input house number"):
            self.find_element(locators_add_basket.btn_house_number).send_keys(random.randrange(10,20))
            time.sleep(1)
        #apartment
        with allure.step("Input apartment number"):
            self.find_element(locators_add_basket.btn_room_number).send_keys(random.randrange(1,36))
            time.sleep(1)
        #floor
        with allure.step("Input floor number"):
            self.find_element(locators_add_basket.btn_floor_number).send_keys(random.randrange(1,9))
            time.sleep(1)
        #entrance
        with allure.step("Input entrance number"):
            self.find_element(locators_add_basket.btn_entrance_number).send_keys(random.randrange(1,3))
            time.sleep(1)
        #entrance code
        with allure.step("Input entrance code"):
            self.find_element(locators_add_basket.btn_entrance_code).send_keys(random.randrange(1000,9999))
            time.sleep(1)
        #phone
        with allure.step("Click on code button"):
            self.find_element(locators_add_basket.btn_basket_code_of_phone).click()
            time.sleep(1)
        with allure.step("Change country on Ukraine"):
            self.find_element(locators_add_basket.
                              btn_basket_code_of_phone_code_of_phone_ukraine).click()
            time.sleep(1)
        with allure.step("Input phone"):
            self.find_element(locators_add_basket.btn_basket_phone).send_keys(fake.phone_number())
            time.sleep(1)
        #email
        with allure.step("Input email"):
            self.find_element(locators_add_basket.btn_basket_email).send_keys(fake.email())
            time.sleep(1)
        #comment
        with allure.step("Input comment"):
            self.find_element(locators_add_basket.btn_basket_comment).send_keys(fake.text())
            time.sleep(1)
        #payment
        with allure.step("Open pyment"):
            self.find_element(locators_add_basket.btn_basket_field_payment).click()
            time.sleep(1)
        with allure.step("Change cash"):
            self.find_element(locators_add_basket.btn_basket_change_cash).click()
            time.sleep(1)

    def confirm_order(self):
        with allure.step("Confirm order"):
            self.find_element(locators_add_basket.btn_basket_submit).click()
            time.sleep(1)

    def assert_confirm_order(self):
        with allure.step("Checking confirm order"):
            assert self.is_element_visible(locators_add_basket.confirm_order)
            time.sleep(1)
