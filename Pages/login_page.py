import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogIn:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.login_uerid_box = (By.ID, "username")
        self.login_password_box = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")  # UPDATED

    def enter_userid(self, userid):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_uerid_box)
        ).clear()

        self.driver.find_element(*self.login_uerid_box).send_keys(userid)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_password_box)
        ).clear()

        self.driver.find_element(*self.login_password_box).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
