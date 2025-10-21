from selenium import webdriver
from selenium.webdriver.common.by import By


class FishPage:
    def __init__(self,driver):
        self.driver = driver

        self.fish_link = (By.XPATH,"//*[@id='SidebarContent']/h4[1]/a")
        self.table = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/table")
        self.return_tab_button = (By.XPATH,"//*[@id='jpetstore-content']/div[2]/div/a")

    def clicking_on_fish_link(self):
        self.driver.find_element(*self.fish_link).click()


    def visibility_of_table(self):
        self.driver.find_element(*self.table)

    def clicking_return_home_tab(self):
        self.driver.find_element(*self.return_tab_button).click()