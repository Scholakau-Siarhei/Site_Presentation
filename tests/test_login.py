"""Checking of authorization"""
import pytest
import allure
from pages.login_page import Login


@pytest.mark.my_work
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Authorisation")
@allure.title("Authorisation with valid data")
def test_login(driver):
    login_page = Login(driver)
    login_page.open_site()
    login_page.close_banner()
    login_page.change_language()
    login_page.go_to_login_page()
    login_page.fill_login_inputs_valid_data_and_submit()
    login_page.go_to_profile()
    login_page.check_authorisation()
