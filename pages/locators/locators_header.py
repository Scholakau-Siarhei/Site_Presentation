"""This is locators for Header page"""
from selenium.webdriver.common.by import By

"""buttons in block menu"""
btn_sauce = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/sauce"]')
display_page_sauce = (By.XPATH, '//h1[@class="page-title__title" and text()="Sauce"]')

btn_drinks = (By.XPATH, '//a[@href="/drinks"]')
display_page_drinks = (By.XPATH, '//div[@class="page-title__content-primary"]//h1[text()="Drinks"]')

btn_desserts = (By.XPATH, '//a[@href="/starter"]')
display_page_desserts = (By.XPATH, '//h1[text()="Desserts"]')

btn_salads = (By.XPATH, '//a[@href="/gsalad"]')
display_page_salads = (By.XPATH, '//h1[text()="Salads"]')

btn_bread = (By.XPATH, '//a[@href="/bread"]')
display_page_bread = (By.XPATH, '//h1[text()="Bread"]')

btn_potato = (By.XPATH, '//a[@href="/potato"]')
display_page_potato = (By.XPATH, '//h1[text()="Potato"]')

btn_chicken = (By.XPATH, '//a[@href="/wings"]')
display_page_chicken = (By.XPATH, '//h1[text()="Chicken"]')

btn_lunch = (By.XPATH, '//a[@href="/lunch"]')
display_page_lunch = (By.XPATH, '//h1[text()="Lunch"]')

btn_pizza = (By.XPATH, '//a[@href="/pizza"]')
display_page_pizza = (By.XPATH, '//h1[text()="Pizza"]')

"""buttons in block information"""
btn_discount = (By.XPATH, '//ul[@class="horizontal-menu__list"]//a[@href="/discount_campaign"]')
display_page_discount = (By.XPATH, '//ul[@class="discounts-list__content"]')

btn_news = (By.XPATH, '//ul[@class="horizontal-menu__list"]//a[@href="/news"]')
display_page_news = (By.XPATH, '//h1[text()="Новости"]')

btn_job = (By.XPATH, '//ul[@class="horizontal-menu__list"]//a[@href="/job"]')
display_page_job = (By.XPATH, '//div[@class="job__banner"]')

btn_loyalty_program = (By.XPATH, '//ul[@class="horizontal-menu__list"]'
                                 '//a[@href="/loyalty-program"]')
display_page_loyalty_program = (By.XPATH, '//div[@class="layout-info"]')
