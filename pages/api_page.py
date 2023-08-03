"""Functions for API tests"""

import allure
import requests
from pages.locators import locators_for_api_tests

class API:
    """Methods for API tests for header"""
    def select_pizza():
        """Open pizza page"""
        response = requests.request("GET", locators_for_api_tests.URL_PIZZA,
                        headers=locators_for_api_tests.headers_pizza, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Pizza'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Pizza") > 0, "No this word in the response"

    #Select Lunch
    def select_lunch():
        """Open lunch page"""
        response = requests.request("GET", locators_for_api_tests.URL_LUNCH,
                                    headers=locators_for_api_tests.headers_lunch, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Lunch'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Lunch") > 0, "No this word in the response"

    #Select Chicken
    def select_chicken():
        """Open chicken page"""
        response = requests.request("GET", locators_for_api_tests.URL_CHICKEN,
                                headers=locators_for_api_tests.headers_chicken, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Chicken'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Chicken") > 0, "No this word in the response"

    #Select Potato
    def select_potato():
        """Open potato page"""
        response = requests.request("GET", locators_for_api_tests.URL_POTATO,
                                    headers=locators_for_api_tests.headers_potato, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Potato'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Potato") > 0, "No this word in the response"

    #Select Bread
    def select_bread():
        """Open bread page"""
        response = requests.request("GET", locators_for_api_tests.URL_BREAD,
                                    headers=locators_for_api_tests.headers_bread, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Bread'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Bread") > 0, "No this word in the response"

    #Select Salads
    def select_salads():
        """Open salads page"""
        response = requests.request("GET", locators_for_api_tests.URL_SALADS,
                                    headers=locators_for_api_tests.headers_salads, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Salads'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Salads") > 0, "No this word in the response"

    #Select Desserts
    def select_desserts():
        """Open desserts page"""
        response = requests.request("GET", locators_for_api_tests.URL_DESSERTS,
                                headers=locators_for_api_tests.headers_desserts, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Desserts'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Desserts") > 0, "No this word in the response"

    #Select Drinks
    def select_drinks():
        """Open drinks page"""
        response = requests.request("GET", locators_for_api_tests.URL_DRINKS,
                                headers=locators_for_api_tests.headers_drinks, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Drinks'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Drinks") > 0, "No this word in the response"

    #Select Sauce
    def select_sauce():
        """Open sauce page"""
        response = requests.request("GET", locators_for_api_tests.URL_SAUCE,
                                    headers=locators_for_api_tests.headers_sauce, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Sauce'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Sauce") > 0, "No this word in the response"

    #Select Discount
    def select_discount():
        """Open discount page"""
        response = requests.request("GET", locators_for_api_tests.URL_DISCOUNT,
                                    headers=locators_for_api_tests.headers_discount, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Discount'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Discount") > 0, "No this word in the response"

    #Select News
    def select_news():
        """Open news page"""
        response = requests.request("GET", locators_for_api_tests.URL_NEWS,
                                    headers=locators_for_api_tests.headers_news, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Новости'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Новости") > 0, "No this word in the response"

    #Select Job
    def select_job():
        """Open job page"""
        response = requests.request("GET", locators_for_api_tests.URL_JOB,
                                    headers=locators_for_api_tests.headers_job, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Работа'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Работа") > 0, "No this word in the response"

    #Select Loyalty program
    def select_loyalty():
        """Open loyalty program page"""
        response = requests.request("GET", locators_for_api_tests.URL_LOYALTY,
                                    headers=locators_for_api_tests.headers_loyalty, timeout=(5, 10))
        print(response.text)
        with allure.step("Check on status code 200"):
            assert response.status_code == 200, "Other code in the response"
        with allure.step("Check what answer contains 'Программа лояльности'"):
            answer = response.json()
            data = str(answer.values())
            assert data.count("Программа лояльности") > 0, "No this word in the response"
