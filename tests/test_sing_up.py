"""Checking of registration"""
import pytest
import allure
from pages.sing_up_page import SingUp

@pytest.mark.my_work
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Registration")
@allure.title("Registration with valid data")
def test_sing_up(driver):
    sing_up_page = SingUp(driver)
    sing_up_page.open_site()
    sing_up_page.close_banner()
    sing_up_page.change_language()
    sing_up_page.click_login_btn()
    sing_up_page.click_singup_btn()
    sing_up_page.input_registration_data()
    sing_up_page.click_reg_sing_up_btn()
    sing_up_page.registration_is_assert()
