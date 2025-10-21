import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.home_page import HomePage
from Pages.login_page import LogIn
from Pages.search_page import SerchPage


@pytest.mark.usefixtures("setup")
class TestSearch:

    def test_search_keyboard(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        search_page = SerchPage(driver)
        search_page.search_item_typing("Angelfish", press_enter=True)

        # Wait for element and get WebElement
        locator = (By.XPATH, "//*[@id='jpetstore-content']/div[2]/table/tbody/tr[2]/td[1]/strong/a")
        item_product_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

        # Assert visibility and print text
        assert item_product_element.is_displayed()

    def test_search_icon(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        search_page = SerchPage(driver)
        search_page.search_item_icon("Angelfish")  # pass text here

        locator = (By.XPATH, "//*[@id='jpetstore-content']/div[2]/table/tbody/tr[2]/td[1]/strong/a")
        item_product_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

        assert item_product_element.is_displayed()



    def test_unavialbe_item(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        search_page = SerchPage(driver)
        search_page.search_invalid_item("xyz",press_enter=True)  # pass text here

        warn_msg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[2]/table/tbody/tr[1]/th[1]"))).text
        print(warn_msg)

        assert warn_msg != "Product ID"


