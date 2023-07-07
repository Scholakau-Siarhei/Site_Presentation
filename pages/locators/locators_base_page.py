"""This is locators for Base page"""
from selenium.webdriver.common.by import By

"""button logo dominos"""
btn_logo = (By.XPATH, '//div[@class="logo-dominos"]')

"""button close banner"""
btn_close_banner = (By.XPATH, '//button[@data-test-type="close"]')

"""language buttons"""
btn_language = (By.XPATH, '//div[@data-test-name="language"]')
btn_english = (By.XPATH, '//li[@value="en"]')
btn_russian = (By.XPATH, '//li[@value="ru"]')
