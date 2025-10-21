import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LogOut:
    def __init__(self,driver):
        self.driver = driver

        self.user_profile_dropdown = (By.ID,"dropdownMenuButton")
        self.log_out_option = (By.XPATH,"//*[@id='jpetstore-content']/div[1]/div/div[2]/div/ul/li[3]/a")

    def click_user_acc(self):
        self.driver.find_element(*self.user_profile_dropdown).click()

    def select_logout_option(self,text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.log_out_option))).click()