"""Checking what user can leave comment"""
import pytest
import allure
from pages.leave_comment_page import LeaveComment

@pytest.mark.my_work
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Leave Comment")
@allure.title("Leave Comment with all valid data")
def test_leave_comment(driver):
    leave_comment_page = LeaveComment(driver)
    leave_comment_page.open_site()
    leave_comment_page.close_banner()
    leave_comment_page.change_language()
    leave_comment_page.open_form_leave_comment()
    leave_comment_page.input_fake_data_in_form_leave_comment()
    leave_comment_page.assert_leave_comment()