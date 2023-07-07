"""Functions for Leave Comment page"""
import random
import time
import allure
import self as self
import pathlib
from pathlib import Path
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from faker import Faker
from pages.base_page import BasePage
from pages.locators import locators_base_page
from pages.locators import locators_leave_comment

class LeaveComment(BasePage):
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

    def open_form_leave_comment(self):
        with allure.step("Clik on Leave feedback button"):
            self.find_element(locators_leave_comment.btn_leave_feedback).click()
            time.sleep(1)

    def input_fake_data_in_form_leave_comment(self):
        fake = Faker("ru_RU")
        """Name"""
        with allure.step("Input fake name"):
            self.find_element(locators_leave_comment.btn_comment_field_name).send_keys(fake.first_name())
            time.sleep(2)
        """Email"""
        with allure.step("Input fake email"):
            self.find_element(locators_leave_comment.btn_comment_field_email).send_keys(fake.email())
            time.sleep(2)
        """Comment"""
        with allure.step("Add comment"):
            self.find_element(locators_leave_comment.btn_input_field_comment).send_keys(fake.text())
            time.sleep(2)
        """Phone"""
        with allure.step("Click on icon flag"):
            self.find_element(locators_leave_comment.btn_comment_code_of_phone).click()
        with allure.step("Change code Ukraine"):
            self.find_element(locators_leave_comment.btn_comment_code_of_phone_ukraine).click()
        with allure.step("Input phone number"):
            self.find_element(locators_leave_comment.btn_comment_field_phone).send_keys(fake.phone_number())
            time.sleep(2)
        """Category"""
        with allure.step("Click on button 'Category feedback'"):
            self.find_element(locators_leave_comment.btn_change_category_feedback).click()
        with allure.step("Change category feedback 'Site'"):
            self.find_element(locators_leave_comment.btn_change_category_feedback_site).click()
            time.sleep(2)
        """Photo"""
        dir_path = pathlib.Path.cwd()
        path = Path(dir_path, "site", "images", "img_add.jpg")
        with allure.step("Add photo"):
            self.find_element(locators_leave_comment.btn_add_photo).send_keys(str(path))
            time.sleep(2)
        """Send comment"""
        with allure.step("Send comment"):
            self.find_element(locators_leave_comment.btn_send).click()
            time.sleep(1)

    def assert_leave_comment(self):
        with allure.step("Assert what feedback is leaved"):
            assert self.is_element_present(locators_leave_comment.successful_comment)
            time.sleep(2)
