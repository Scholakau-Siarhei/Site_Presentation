"""Functions for Sing Up page"""
import time
import allure
from faker import Faker
from pages.base_page import BasePage
from pages.locators import locators_base_page, locators_log_in, locators_sing_up


class SingUp(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    def click_login_btn(self):
        with allure.step("Click button Log in"):
            self.find_element(locators_log_in.btn_log_in).click()
            time.sleep(1)

    def click_singup_btn(self):
        with allure.step("Click button Sing up"):
            self.find_element(locators_sing_up.btn_sing_up).click()
            time.sleep(1)

    def input_registration_data(self):
        fake = Faker("ru_RU")
        """Phone number"""
        with allure.step("Click on icon flag"):
            self.find_element(locators_sing_up.btn_singup_code_of_phone).click()
        with allure.step("Change code Ukraine"):
            self.find_element(locators_sing_up.btn_singup_code_of_phone_ukraine).click()
        with allure.step("Input phone number"):
            self.find_element(locators_sing_up.btn_singup_phone).send_keys(fake.phone_number())
            time.sleep(2)
        """Email"""
        with allure.step("Input fake email"):
            self.find_element(locators_sing_up.btn_singup_email).send_keys(fake.email())
            time.sleep(2)
        """Password"""
        with allure.step("Input fake password"):
            self.find_element(locators_sing_up.btn_singup_password).send_keys(fake.password())
            time.sleep(2)

    def click_reg_sing_up_btn(self):
        with allure.step("Click button Sing up"):
            self.find_element(locators_sing_up.btn_reg_sing_up).click()
            time.sleep(1)

    def registration_is_assert(self):
        with allure.step("Assert of registration"):
            assert self.is_element_present(locators_sing_up.registration_complete)
            time.sleep(2)
