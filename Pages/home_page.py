from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver = driver

        self.sign_up_button = (By.XPATH,"//*[@id='jpetstore-content']/div[1]/div/div[2]/a[3]")
        self.sign_in_button  = (By.XPATH , "//*[@id='jpetstore-content']/div[1]/div/div[2]/a[2]")

    def click_signup(self):
        self.driver.find_element(*self.sign_up_button).click()

    def click_signin(self):
        self.driver.find_element(*self.sign_in_button).click()