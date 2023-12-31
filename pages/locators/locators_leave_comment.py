"""This is locators for leave comment page"""

from selenium.webdriver.common.by import By

#button leave feedback
btn_leave_feedback = (By.XPATH, '//ul[@class="footer__menu-group-list"]//a[@href="/feedback"]')

#buttons in feedback form
"""name"""
btn_comment_field_name = (By.XPATH, '//form[@class="feedback__form"]//input[@type="text"]')

"""email"""
btn_comment_field_email = (By.XPATH, '//form[@class="feedback__form"]//input[@type="email"]')

"""comment"""
btn_input_field_comment = (By.XPATH, '//form[@class="feedback__form"]//textarea[@type="text"]')

"""phone"""
#button change country phone
btn_comment_code_of_phone = (By.XPATH, '//div[@class="selected-flag"]')
#code phone of ukraine
btn_comment_code_of_phone_ukraine = (By.XPATH, '//span[@class="dial-code" and text()="+380"]')
#field for input phone
btn_comment_field_phone = (By.XPATH, '//form[@class="feedback__form"]//input[@type="tel"]')

"""category"""
btn_change_category_feedback = (By.XPATH,
                                '//select[@class="jss2 custom-select__select jss15 jss18"]')
btn_change_category_feedback_site = (By.XPATH, '//option[@value="1"]')

"""photo"""
#button for adding photo
btn_add_photo = (By.XPATH, '//input[@type="file"]')
#adress adding photo
photo = ["X:\Learn_QA\PYTHON\my_work\static\images\img_add.jpg"]
#button confirm adding photo
adding_photo = (By.XPATH, '//*[contains(text(),"img_add.jpg")]')

"""Send comment"""
btn_send = (By.XPATH, '//form[@class="feedback__form"]//button[@type="submit"]')

"""Successful comment"""
successful_comment = (By.XPATH, '//div[text()="Успешно отправлено"]')
