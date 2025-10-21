import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.product_link = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/table/tbody/tr[1]/td[1]/a")
        self.add_to_cart_button = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/table/tbody/tr[1]/td[5]/a")
        self.remove_button = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/form/table/tbody/tr/td[8]/a")
        self.update_button = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/form/table/tfoot/tr/td[2]/button")
        self.check_out_button = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/div[2]/a")

    def click_product(self):
        self.driver.find_element(*self.product_link).click()

    def click_cart_button(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_remove_button(self):
        self.driver.find_element(*self.remove_button).click()

    def click_update_button(self):
        self.driver.find_element(*self.update_button).click()

    def click_check_out_button(self):
        self.driver.find_element(*self.check_out_button).click()
