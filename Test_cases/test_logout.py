import time

from selenium import webdriver
import pytest
from Pages.home_page import HomePage
from Pages.login_page import LogIn
from Pages.logout_page import LogOut


@pytest.mark.usefixtures("setup")
class TestLogOut:
    def test_logout(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        lo_page = LogOut(driver)
        lo_page.click_user_acc()
        lo_page.select_logout_option("Sign Out")
        url = driver.current_url
        print(url)
        assert url == "https://jpetstore.aspectran.com/"



