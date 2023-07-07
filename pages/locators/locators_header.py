"""This is locators for Header page"""
from selenium.webdriver.common.by import By

"""blok menu"""
block_menu = (By.XPATH, '//div[@class="sticky-component"]'
                        '//div[@data-test="composed-navigation-primary"]'
                        '//li[@class="horizontal-menu__list-item"]')

"""buttons in block menu"""
btn_sauce = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/sauce"]')
display_page_sauce = (By.XPATH, '//h1[@class="page-title__title" and text()="Sauce"]')

btn_drinks = (By.XPATH, '//a[@href="/drinks"]')
display_page_drinks = (By.XPATH, '//h1[text()="Drinks"]')

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

btn_pizza = (By.XPATH, '//a[@href="/pizza"]')
display_page_pizza = (By.XPATH, '//h1[text()="Pizza"]')

"""block infirmation"""
block_infirmation = (By.XPATH, '//div[@class="sticky-component"]'
                     '//div[@class="composed-navigation__secondary"]')

"""buttons in block infirmation"""
btn_discount = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/discount_campaign"]')
display_page_discount = (By.XPATH, '//h1[text()="Discounts"]')

btn_news = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/news"]')
display_page_news = (By.XPATH, '//h1[text()="Новости"]')

btn_work_in_dominis = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/job"]')
display_page_job = (By.XPATH, '//div[@class="job__banner-actions"]'
                              '//span[@class="custom-button__content"]')

btn_loyalty_program = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/loyalty-program"]')
display_page_loyalty_program = (By.XPATH, '//div[@class="layout-info"]')
