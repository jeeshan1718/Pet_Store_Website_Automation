import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages.home_page import HomePage
from Pages.registration_page import RegistrationPage
from conftest import setup


@pytest.mark.usefixtures("setup")
class TestRegistration:
    def test_valid_registration(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signup()

        Reg_page = RegistrationPage(driver)
        Reg_page.enter_userid("Pja@22334599991178988997")
        Reg_page.enter_password("Kohli@1718")
        Reg_page.enter_confirm_password("Kohli@1718")
        Reg_page.enter_first_name("Jeeshan")
        Reg_page.enter_last_name("Ahmad")
        Reg_page.enter_email("jeeshan@example.com")
        Reg_page.enter_phone("9876543210")
        Reg_page.enter_address1("123 Main Street")
        Reg_page.enter_address2("Near Green Park")
        Reg_page.enter_city("New Delhi")
        Reg_page.enter_state("Delhi")
        Reg_page.enter_zip("110001")
        Reg_page.enter_country("India")
        Reg_page.select_language("English")
        Reg_page.select_fav_cat("Cats")
        Reg_page.click_save_acc_button()

        msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='jpetstore-content']/div[2]/div/div/div[1]/p"))
        ).text
        print(msg)

        assert "Your account has been created. Please try login." in msg

    def test_invalidphoneno_registration(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signup()

        Reg_page = RegistrationPage(driver)
        Reg_page.enter_userid("Pooja@778899")
        Reg_page.enter_password("Kohli@1718")
        Reg_page.enter_confirm_password("Kohli@1718")
        Reg_page.enter_first_name("Jeeshan")
        Reg_page.enter_last_name("Ahmad")
        Reg_page.enter_email("jeeshan@example.com")
        Reg_page.enter_phone("9876543210999999%%%%")
        Reg_page.enter_address1("123 Main Street")
        Reg_page.enter_address2("Near Green Park")
        Reg_page.enter_city("New Delhi")
        Reg_page.enter_state("Delhi")
        Reg_page.enter_zip("110001")
        Reg_page.enter_country("India")
        Reg_page.select_language("English")
        Reg_page.select_fav_cat("Cats")
        Reg_page.click_save_acc_button()
        invlid_err_msg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='jpetstore-content']/div[2]/div/div/form/table[2]/tbody/tr[4]/td[2]/span"))).text
        print(invlid_err_msg)

        assert 'must be telephone number format (allowed format: "999-9999-9999" or "999 9999 9999" or "99999999999")' in invlid_err_msg

    def test_blank_field_registration(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signup()

        Reg_page = RegistrationPage(driver)
        Reg_page.enter_userid("Pooja@1888890989")
        Reg_page.enter_password("Kohli@1718")
        Reg_page.enter_confirm_password("Kohli@1718")
        Reg_page.enter_first_name("Jeeshan")
        Reg_page.enter_last_name("")
        Reg_page.enter_email("jeeshan@example.com")
        Reg_page.enter_phone("9876543210999999%%%%")
        Reg_page.enter_address1("123 Main Street")
        Reg_page.enter_address2("Near Green Park")
        Reg_page.enter_city("New Delhi")
        Reg_page.enter_state("Delhi")
        Reg_page.enter_zip("110001")
        Reg_page.enter_country("India")
        Reg_page.select_language("English")
        Reg_page.select_fav_cat("Cats")
        Reg_page.click_save_acc_button()
        warning_msg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='jpetstore-content']/div[2]/div/div/form/table[2]/tbody/tr[2]/td[2]/span"))).text
        print(warning_msg)
        assert "must not be blank" in warning_msg

    def test_multiple_userid_registration(self,setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.click_signup()

        Reg_page = RegistrationPage(driver)
        Reg_page.enter_userid("Pooja@223345")
        Reg_page.enter_password("Kohli@1718")
        Reg_page.enter_confirm_password("Kohli@1718")
        Reg_page.enter_first_name("Jeeshan")
        Reg_page.enter_last_name("ahmad")
        Reg_page.enter_email("jeeshan@example.com")
        Reg_page.enter_phone("9876543888")
        Reg_page.enter_address1("123 Main Street")
        Reg_page.enter_address2("Near Green Park")
        Reg_page.enter_city("New Delhi")
        Reg_page.enter_state("Delhi")
        Reg_page.enter_zip("110001")
        Reg_page.enter_country("India")
        Reg_page.select_language("English")
        Reg_page.select_fav_cat("Cats")
        Reg_page.click_save_acc_button()
        sameuser_warn_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='jpetstore-content']/div[2]/div/div/form/table[1]/tbody/tr[1]/td[2]/span[2]")
            )
        ).text
        print(sameuser_warn_msg)
        assert "This user ID is already in use" in sameuser_warn_msg




