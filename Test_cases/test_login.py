import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.home_page import HomePage
from Pages.login_page import LogIn

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_valid(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        # Validate dashboard displayed
        dash_pic = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='WelcomeContent']//img"))
        )
        assert dash_pic.is_displayed()

    def test_login_invalid(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("rohli@1718")
        lp_page.click_login_button()

        # Validate error message
        err_msg = lp_page.get_error_message()
        print("Error message:", err_msg)
        assert "Invalid username or password" in err_msg
