import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.home_page import HomePage
from Pages.fish_page import FishPage
from Pages.login_page import LogIn
from Pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestAddToCart:
    def test_add_to_cart(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page =LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        fish_page = FishPage(driver)
        fish_page.clicking_on_fish_link()

        cart_page = CartPage(driver)
        cart_page.click_product()
        cart_page.click_cart_button()

        quanity_tab = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[2]/form/table/thead/tr/th[5]/b"))).text
        print(quanity_tab)

        assert "Quantity" in quanity_tab

    def test_remove_item(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        fish_page = FishPage(driver)
        fish_page.clicking_on_fish_link()

        cart_page = CartPage(driver)
        cart_page.click_product()
        cart_page.click_cart_button()
        cart_page.click_remove_button()

        confimation_msg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[2]/form/table/tbody/tr/td"))).text
        print(confimation_msg)
        curent_url = driver.current_url

        assert 'https://jpetstore.aspectran.com/cart/viewCart' == curent_url

    def test_update_item(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        fish_page = FishPage(driver)
        fish_page.clicking_on_fish_link()

        cart_page = CartPage(driver)
        cart_page.click_product()
        cart_page.click_cart_button()
        cart_page.click_update_button()
        curnt_url = driver.current_url

        assert "https://jpetstore.aspectran.com/cart/viewCart" != curnt_url

    def test_checkout(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signin()

        lp_page = LogIn(driver)
        lp_page.enter_userid("Jeeshan1718")
        lp_page.enter_password("Kohli@1718")
        lp_page.click_login_button()

        fish_page = FishPage(driver)
        fish_page.clicking_on_fish_link()

        cart_page = CartPage(driver)
        cart_page.click_product()
        cart_page.click_cart_button()
        cart_page.click_check_out_button()

        crnt_url = driver.current_url
        print(crnt_url)
        assert "https://jpetstore.aspectran.com/order/newOrderForm" == crnt_url

