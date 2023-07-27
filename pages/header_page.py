"""Functions for Header page"""

import time
import allure

from pages.base_page import BasePage
from pages.locators import locators_base_page
from pages.locators import locators_header


class Header(BasePage):
    """Methods for checking buttons of header and opening pages"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.implicitly_wait(10)

    def open_site(self):
        with allure.step("Go to general page"):
            self.driver.get('https://dominos.by/')

    def close_banner(self):
        with allure.step("Close banner"):
            if self.find_element(locators_base_page.btn_close_banner):
                self.find_element(locators_base_page.btn_close_banner).click()
            else:
                pass
            time.sleep(1)

    def change_language(self):
        with allure.step("Clik on language icon"):
            self.find_element(locators_base_page.btn_language).click()
        with allure.step("Change language on english"):
            self.find_element(locators_base_page.btn_english).click()
            time.sleep(1)

    def check_block_menu(self):
        buttons_in_block_menu = [
            locators_header.btn_sauce,
            locators_header.btn_drinks,
            locators_header.btn_desserts,
            locators_header.btn_salads,
            locators_header.btn_bread,
            locators_header.btn_potato,
            locators_header.btn_chicken,
            locators_header.btn_lunch,
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
            locators_header.display_page_lunch,
            locators_header.display_page_pizza
        ]
        for name, present in zip(buttons_in_block_menu, check_display_page_menu):
            with allure.step("Click on element in block menu"):
                self.find_element(name).click()
            with allure.step("Assert what page is displayed"):
                assert self.find_element(present).is_displayed(), f"Page {present} is not displayed"
                time.sleep(1)

    def check_block_information(self):
        buttons_in_block_information = [
            locators_header.btn_discount,
            locators_header.btn_news,
            locators_header.btn_job,
            locators_header.btn_loyalty_program
        ]
        check_display_block_information = [
            locators_header.display_page_discount,
            locators_header.display_page_news,
            locators_header.display_page_job,
            locators_header.display_page_loyalty_program
        ]
        for name, present in zip(buttons_in_block_information, check_display_block_information):
            with allure.step("Click on element in block information"):
                self.find_element(name).click()
                time.sleep(1)
            with allure.step("Assert what page is displayed"):
                assert self.find_element(present).is_displayed(), f"Page {present} is not displayed"
                time.sleep(1)
                self.driver.back()
