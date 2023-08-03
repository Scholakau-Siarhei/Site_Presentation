"""Functions for Leave Comment page"""

import time
import allure
from faker import Faker
from pages.base_page import BasePage
from pages.locators import locators_base_page
from pages.locators import locators_leave_comment

class LeaveComment(BasePage):
    """Methods for checking leave comment"""
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
            if self.find_element(locators_base_page.btn_close_banner).click():
                self.find_element(locators_base_page.btn_close_banner).click()
            else:
                pass
            time.sleep(1)

    def change_language(self):
        """Changes language from Russian to English"""
        with allure.step("Clik on language icon"):
            self.find_element(locators_base_page.btn_language).click()
        with allure.step("Change language on english"):
            self.find_element(locators_base_page.btn_english).click()
            time.sleep(1)

    def open_form_leave_comment(self):
        """Open form leave comment"""
        with allure.step("Clik on Leave feedback button"):
            self.find_element(locators_leave_comment.btn_leave_feedback).click()
            time.sleep(1)

    def input_fake_data_in_form_leave_comment(self):
        """Input valid data in form leave comment"""
        fake = Faker("ru_RU")

        #Name
        with allure.step("Input fake name"):
            self.find_element(locators_leave_comment.btn_comment_field_name).send_keys(fake.first_name())
            time.sleep(1)
        #Email
        with allure.step("Input fake email"):
            self.find_element(locators_leave_comment.btn_comment_field_email).send_keys(fake.email())
            time.sleep(1)
        #Comment
        with allure.step("Add comment"):
            self.find_element(locators_leave_comment.btn_input_field_comment).send_keys(fake.text())
            time.sleep(1)
        #Phone
        with allure.step("Click on icon flag"):
            self.find_element(locators_leave_comment.btn_comment_code_of_phone).click()
        with allure.step("Change code Ukraine"):
            self.find_element(locators_leave_comment.btn_comment_code_of_phone_ukraine).click()
        with allure.step("Input phone number"):
            self.find_element(locators_leave_comment.btn_comment_field_phone).send_keys(fake.phone_number())
        #Category
        with allure.step("Click on button 'Category feedback'"):
            self.find_element(locators_leave_comment.btn_change_category_feedback).click()
        with allure.step("Change category feedback 'Site'"):
            self.find_element(locators_leave_comment.btn_change_category_feedback_site).click()
            time.sleep(1)
        #Photo
        with allure.step("Add photo"):
            self.find_element(locators_leave_comment.btn_add_photo).send_keys(locators_leave_comment.photo)
            time.sleep(1)
        with allure.step("Checking adding photo"):
            load = self.find_element(locators_leave_comment.adding_photo).text
            assert load != "", "Файл не был загружен"
        #Send comment
        with allure.step("Send comment"):
            self.find_element(locators_leave_comment.btn_send).click()
            time.sleep(1)

    def assert_leave_comment(self):
        """Checking what comment is sending"""
        with allure.step("Assert what feedback is leaved"):
            assert self.is_element_present(locators_leave_comment.successful_comment)
            time.sleep(1)
