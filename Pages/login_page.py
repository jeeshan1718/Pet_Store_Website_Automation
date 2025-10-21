import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LogIn:
    def __init__(self,driver):
        self.driver = driver
        hh= "Invalid username or password. Signon failed."
        self.login_uerid_box = (By.ID,"username")
        self.login_password_box = (By.NAME,"password")
        self.login_button  = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/div/div/div[1]/div/form/div[3]/button")

    def enter_userid(self,userid):
        self.driver.find_element(*self.login_uerid_box).clear()
        self.driver.find_element(*self.login_uerid_box).send_keys(userid)

    def enter_password(self,password):
        self.driver.find_element(*self.login_password_box).clear()
        self.driver.find_element(*self.login_password_box).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


