"""This is locators for order pizza"""
from selenium.webdriver.common.by import By

"""button add hot-dog board for Munich pizza"""
btn_add_hotdog_board = (By.XPATH, '//div[@data-code="MUNH"]//div[@data-type="hotdog"]'
                                  '//button[@data-test="topping-counter-add"]')

"""button add to basket Munich"""
btn_add_to_basket_munich = (By.XPATH, '//div[@data-code="MUNH"]'
                                      '//div[@class="product-card__actions"]')

"""button basket"""
btn_basket = (By.XPATH, '//div[@class="cart-button"]')

"""open form for order pizza"""
btn_open_form_order_pizza = (By.XPATH, '//a[@data-action="checkout"]')

"""fields in order pizza form """
"""street"""
btn_search_street = (By.XPATH, '//div[@class="checkout"]//input[@name="street"]')
btn_search_field_street = (By.XPATH, '//div[@class="search-street__modal-content"]'
                                     '//input[@name="street"]')
btn_change_street = (By.XPATH, '//div[contains(text(),"ЛЕВКОВА")]')
"""house"""
btn_house_number = (By.XPATH, '//input[@name="streetnumber"]')
"""apartment"""
btn_room_number = (By.XPATH, '//input[@name="apartment"]')
"""floor"""
btn_floor_number = (By.XPATH, '//input[@name="floor"]')
"""entrance"""
btn_entrance_number = (By.XPATH, '//input[@name="entrance"]')
"""entrance code"""
btn_entrance_code = (By.XPATH, '//input[@name="doorCode"]')
"""phone"""
btn_basket_code_of_phone = (By.XPATH, '//div[@class="checkout__group-content"]'
                                      '//div[@class="flag by"]')
btn_basket_code_of_phone_code_of_phone_ukraine = (By.XPATH,
                                                  '//div[@class="checkout__group-content"]'
                                                  '//div[@class="flag ua"]')
btn_basket_phone = (By.XPATH, '//div[@class="checkout__group-content"]'
                              '//input[@class="custom-field-phone__input form-control"]')
"""email"""
btn_basket_email = (By.XPATH, '//div[@class="checkout__group-content"]//input[@type="email"]')
"""coupon"""
btn_basket_coupon = (By.XPATH, '//div[@class="checkout__group-content"]'
                               '//div[@data-test-name="coupon"]')
"""comment"""
btn_basket_comment = (By.XPATH, '//div[@class="checkout__group-content"]'
                                '//textarea[@class="custom-field-text__input"]')
"""payment"""
btn_basket_field_payment = (By.XPATH, '//form[@action="get"]//div[@class="jss1"]')
btn_basket_change_cash = (By.XPATH, '//form[@action="get"]//option[@value="cash"]')
"""submit button"""
btn_basket_submit = (By.XPATH, '//div[@class="checkout__group"]//button[@type="submit"]')
"""confirm order"""
confirm_order = (By.XPATH, '//div[@class="custom-modal__content"]'
                           '//div[contains(text(),"We have received you order")]')
