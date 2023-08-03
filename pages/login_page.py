"""Functions for Log In page"""

import time
import allure
from pages.base_page import BasePage
from pages.locators import locators_base_page
from pages.locators import locators_log_in


class Login(BasePage):
    """Methods for login in site"""
    def __init__(self, driver):
        """WebDriver Initialization"""
        super().__init__(driver)
        self.driver = driver

    def open_site(self):
        """Open site"""
        with allure.step("Go to general page"):
            self.driver.get('https://dominos.by/')

    def close_banner(self):
        """Closes advertising banner"""
        with allure.step("Close banner"):
            if self.is_element_visible(locators_base_page.btn_close_banner):
                self.find_element(locators_base_page.btn_close_banner).click()
            else:
                pass

    def change_language(self):
        """Changes language from Russian to English"""
        with allure.step("Clik on language icon"):
            self.find_element(locators_base_page.btn_language).click()
        with allure.step("Change language on english"):
            self.find_element(locators_base_page.btn_english).click()
            time.sleep(1)

    def go_to_login_page(self):
        """Open login page"""
        with allure.step("Click button Log in"):
            self.find_element(locators_log_in.btn_log_in).click()
            time.sleep(1)

    def fill_login_inputs_valid_data_and_submit(self):
        """Inputing valid data and submiting"""
        #Email
        with allure.step("Fill in the email field"):
            self.find_element(locators_log_in.btn_login_email).send_keys("test.xoy@gmail.com")
            time.sleep(1)
        #Password
        with allure.step("Fill in the password field"):
            self.find_element(locators_log_in.btn_login_password).send_keys("@123qwe@")
            time.sleep(1)
        #Log in
        with allure.step("Click button Log in"):
            self.find_element(locators_log_in.btn_aut_log_in).click()
            time.sleep(1)

    def go_to_profile(self):
        """Open profile page"""
        with allure.step("Clik on profile button"):
            self.find_element(locators_log_in.btn_profile).click()
            time.sleep(1)

    def check_authorisation(self):
        """Checking what user is authorisation"""
        with allure.step("Assert what profile form is open"):
            assert self.is_element_present(locators_log_in.profile_form)
            time.sleep(2)
