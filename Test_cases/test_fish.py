import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.home_page import HomePage
from Pages.fish_page import FishPage
from Pages.login_page import LogIn
@pytest.mark.usefixtures("setup")

class TestFishes:
    def test_fish_link_verifying(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page =LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        fish_page = FishPage(driver)
        fish_page.clicking_on_fish_link()
        table = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[2]/table")))

        assert table.is_displayed()

    def test_return_to_menu(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page =LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        fish_page = FishPage(driver)
        fish_page.clicking_on_fish_link()
        fish_page.clicking_return_home_tab()
        url = driver.current_url
        print(url)
        assert url == "https://jpetstore.aspectran.com/"
