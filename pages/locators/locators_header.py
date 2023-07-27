"""This is locators for Header page"""

from selenium.webdriver.common.by import By

#buttons in block menu
#open sause page
btn_sauce = (By.XPATH, '//div[@class="sticky-component"]//a[@href="/sauce"]')
#element in open sause page
display_page_sauce = (By.XPATH, '//h1[@class="page-title__title" and text()="Sauce"]')

#open drinks page
btn_drinks = (By.XPATH, '//a[@href="/drinks"]')
#element in open drinks page
display_page_drinks = (By.XPATH, '//div[@class="page-title__content-primary"]//h1[text()="Drinks"]')

#open desserts page
btn_desserts = (By.XPATH, '//a[@href="/starter"]')
#element in open desserts page
display_page_desserts = (By.XPATH, '//h1[text()="Desserts"]')

#open salads page
btn_salads = (By.XPATH, '//a[@href="/gsalad"]')
#element in open salads page
display_page_salads = (By.XPATH, '//h1[text()="Salads"]')

#open bread page
btn_bread = (By.XPATH, '//a[@href="/bread"]')
#element in open bread page
display_page_bread = (By.XPATH, '//h1[text()="Bread"]')

#open potato page
btn_potato = (By.XPATH, '//a[@href="/potato"]')
#element in open potato page
display_page_potato = (By.XPATH, '//h1[text()="Potato"]')

#open chicken page
btn_chicken = (By.XPATH, '//a[@href="/wings"]')
#element in open chicken page
display_page_chicken = (By.XPATH, '//h1[text()="Chicken"]')

#open lunch page
btn_lunch = (By.XPATH, '//a[@href="/lunch"]')
#element in open lunch page
display_page_lunch = (By.XPATH, '//h1[text()="Lunch"]')

#open pizza page
btn_pizza = (By.XPATH, '//a[@href="/pizza"]')
#element in open pizza page
display_page_pizza = (By.XPATH, '//h1[text()="Pizza"]')

"""buttons in block information"""
#open discount page
btn_discount = (By.XPATH, '//ul[@class="horizontal-menu__list"]//a[@href="/discount_campaign"]')
#element in open discount page
display_page_discount = (By.XPATH, '//ul[@class="discounts-list__content"]')

#open news page
btn_news = (By.XPATH, '//ul[@class="horizontal-menu__list"]//a[@href="/news"]')
#element in open news page
display_page_news = (By.XPATH, '//h1[text()="Новости"]')

#open job page
btn_job = (By.XPATH, '//ul[@class="horizontal-menu__list"]//a[@href="/job"]')
#element in open job page
display_page_job = (By.XPATH, '//div[@class="job__banner"]')

#open loyalty program page
btn_loyalty_program = (By.XPATH, '//ul[@class="horizontal-menu__list"]'
                                 '//a[@href="/loyalty-program"]')
#element in open loyalty program page
display_page_loyalty_program = (By.XPATH, '//div[@class="loyalty"]')
