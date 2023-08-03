"""API tests for header"""

import pytest
import allure
from pages.api_page import API

@pytest.mark.my_work
@pytest.mark.non_multiple_CPUs_run
@allure.suite("API tests")
@allure.title("Checking what page is opened")

def test_api():
    """Run API tests"""
    API.select_pizza()
    API.select_lunch()
    API.select_chicken()
    API.select_potato()
    API.select_bread()
    API.select_salads()
    API.select_desserts()
    API.select_drinks()
    API.select_sauce()
    API.select_discount()
    API.select_news()
    API.select_job()
    API.select_loyalty()
