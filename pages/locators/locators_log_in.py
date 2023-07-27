"""This is locators for authorisation page"""

from selenium.webdriver.common.by import By

#button log in
btn_log_in = (By.XPATH, '//div[@class="authorization-cta"]')

#input email
btn_login_email = (By.XPATH, '//form[@class="authorization-form"]//input[@type="email"]')

#input password
btn_login_password = (By.XPATH, '//form[@class="authorization-form"]//input[@type="password"]')

#button authorisation log in
btn_aut_log_in = (By.XPATH, '//form[@class="authorization-form"]//button[@type="submit"]')

#button profile
btn_profile = (By.XPATH, '//div[@class="authorization-cta"]')

#button profile
profile_form = (By.XPATH, '//div[@data-test="profile-authorized"]')
