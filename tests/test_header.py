"""Checking what all elements of header clickable"""
import pytest
import allure
from pages.header_page import Header

@pytest.mark.my_work
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Header")
@allure.title("Checking all elements of header")
def test_header(driver):
    header_page = Header(driver)
    header_page.open_site()
    header_page.close_banner()
    header_page.change_language()
    header_page.check_block_menu()
    header_page.check_block_information()
