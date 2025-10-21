import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.home_page import HomePage

from Pages.login_page import LogIn
@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_valid(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page =LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()
        dash_pic = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[1]/div/a/img")))
        assert dash_pic.is_displayed()

    def test_login_invalid(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()
        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("rohli@1718")
        lp_page.click_login_button()
        err_msg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[2]/div/div/div[1]/div/form/div[4]"))).text
        print(err_msg)
        assert "Invalid username or password. Signon failed." in err_msg