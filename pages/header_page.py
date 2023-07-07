"""Functions for Header page"""
import allure
import time
import pytest_check
from pytest_check import check
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import locators_base_page
from pages.locators import locators_header

class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_site(self):
        with allure.step("Go to general page"):
            self.driver.get('https://dominos.by/')

    def close_banner(self):
        with allure.step("Close banner"):
            self.find_element(locators_base_page.btn_close_banner).click()
            time.sleep(1)

    def change_language(self):
        with allure.step("Clik on language icon"):
            self.find_element(locators_base_page.btn_language).click()
        with allure.step("Change language on english"):
            self.find_element(locators_base_page.btn_english).click()
            time.sleep(1)

    def check_block_menu(self):
        # buttons_in_block_menu = {
        #     'Checking display the Sauce page': locators_header.btn_sauce,
        #     'Checking display the Drinks page': locators_header.btn_drinks,
        #     'Checking display the Desserts page': locators_header.btn_desserts,
        #     'Checking display the Salads page': locators_header.btn_salads,
        #     'Checking display the Bread page': locators_header.btn_bread,
        #     'Checking display the Potato page': locators_header.btn_potato,
        #     'Checking display the Chicken page': locators_header.btn_chicken,
        #     'Checking display the Pizza page': locators_header.btn_pizza
        # }
        # check_display_page_menu = {
        #     'Sauce page': locators_header.display_page_sauce,
        #     'Drinks page': locators_header.display_page_drinks,
        #     'Desserts page': locators_header.display_page_desserts,
        #     'Salads page': locators_header.display_page_salads,
        #     'Bread page': locators_header.display_page_bread,
        #     'Potato page': locators_header.display_page_potato,
        #     'Chicken page': locators_header.display_page_chicken,
        #     'Pizza page': locators_header.display_page_pizza
        # }
        # for name in buttons_in_block_menu.values():
        #     with allure.step("Click on element in block menu"):
        #         self.find_element(name).click()
        #         for page in check_display_page_menu.values():
        #             with allure.step("Assert what page is displayed"):
        #                 assert self.find_element(page)


        buttons_in_block_menu = [
            locators_header.btn_sauce,
            locators_header.btn_drinks,
            locators_header.btn_desserts,
            locators_header.btn_salads,
            locators_header.btn_bread,
            locators_header.btn_potato,
            locators_header.btn_chicken,
            locators_header.btn_pizza
        ]
        check_display_page_menu = [
            locators_header.display_page_sauce,
            locators_header.display_page_drinks,
            locators_header.display_page_desserts,
            locators_header.display_page_salads,
            locators_header.display_page_bread,
            locators_header.display_page_potato,
            locators_header.display_page_chicken,
            locators_header.display_page_pizza
        ]
        for name in buttons_in_block_menu:
            with allure.step("Click on element in block menu"):
                self.find_element(name).click()
                time.sleep(2)
                # for page in check_display_page_menu:
                #     with allure.step("Assert what page is displayed"):
                #         self.find_element(page)
                #         wait.is_element_visible(page)








    # def block_menu_click_all_buttons(self):
    #     with allure.step("Click all buttons in the menu-header"):
    #         btn_in_block_menu = self.find_elements(locators_header.block_menu)
    #         num = 1
    #         for button in btn_in_block_menu:
    #             button.find_element(By.XPATH, '//li[@class="horizontal-menu__list-item"][{NUM}]').click()
    #             num += 1
            #return self.find_element(locators_header.display_page_sauce).text

    # def go_to_my_data(self):
    #     with allure.step("Перейти на вкладку личные данные"):
    #         self.is_element_visible(profile_page_locators.my_data_tab).click()
