"""This is locators for registration page"""

from selenium.webdriver.common.by import By

#button sing_up
btn_sing_up = (By.XPATH, '//span[contains(text(), "Sign up")]')

#input phone
"""button change country phone"""
btn_singup_code_of_phone = (By.XPATH, '//div[@class="registration"]//div[@class="flag by"]')
"""code phone of ukraine"""
btn_singup_code_of_phone_ukraine = (By.XPATH, '//div[@class="registration"]'
                                              '//span[contains(text(), "Ukraine")]')
"""field for input phone"""
btn_singup_phone = (By.XPATH, '//div[@class="registration"]//input[@type="tel"]')

#input email
btn_singup_email = (By.XPATH, '//div[@class="registration"]//input[@name="email"]')

#input password
btn_singup_password = (By.XPATH, '//div[@class="registration"]//input[@type="password"]')

#button sing_up
btn_reg_sing_up = (By.XPATH, '//div[@class="registration"]//button[@type="submit"]')

#registration is assert
registration_complete = (By.XPATH, '//div[text()="Вы успешно зарегистрированы! '
                                   'Теперь вы можете войти, используя указанный email и пароль."]')
