
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class RegistrationPage:
    def __init__(self,driver):
        self.driver = driver
        self.userid_box = (By.NAME,"username")
        self.password_box = (By.NAME,"password")
        self.confirm_pass_box = (By.NAME, "repeatedPassword")
        self.first_name_box = (By.NAME, "firstName")
        self.last_name_box = (By.NAME, "lastName")
        self.address1_box = (By.NAME, "address1")
        self.address2_box = (By.NAME, "address2")
        self.email_box = (By.NAME, "email")
        self.phone_box = (By.NAME, "phone")
        self.zip_box = (By.NAME, "zip")
        self.city_box = (By.NAME, "city")
        self.state_box = (By.NAME, "state")
        self.country_box = (By.NAME, "country")
        self.language_dropdown = (By.XPATH , "//*[@id='jpetstore-content']/div[2]/div/div/form/table[3]/tbody/tr[1]/td[2]/select")
        self.faviourate_cat_dropdown = (By.XPATH , "//*[@id='jpetstore-content']/div[2]/div/div/form/table[3]/tbody/tr[2]/td[2]/select")
        self.save_account_button = (By.XPATH ,"//*[@id='jpetstore-content']/div[2]/div/div/form/div/button")

    def enter_userid(self,userid):
        self.driver.find_element(*self.userid_box).send_keys(userid)

    def enter_password(self,password):
        self.driver.find_element(*self.password_box).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(*self.confirm_pass_box).send_keys(confirm_password)

    def enter_first_name(self,f_name):
        self.driver.find_element(*self.first_name_box).send_keys(f_name)

    def enter_last_name(self, l_name):
        self.driver.find_element(*self.last_name_box).send_keys(l_name)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_box).send_keys(phone)

    def enter_zip(self, zip_code):
        self.driver.find_element(*self.zip_box).send_keys(zip_code)

    def enter_city(self, city):
        self.driver.find_element(*self.city_box).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*self.state_box).send_keys(state)

    def enter_address1(self, address1):
        self.driver.find_element(*self.address1_box).send_keys(address1)

    def enter_address2(self, address2):
        self.driver.find_element(*self.address2_box).send_keys(address2)

    def enter_email(self, email):
        self.driver.find_element(*self.email_box).send_keys(email)

    def enter_country(self, country):
        self.driver.find_element(*self.country_box).send_keys(country)

    def select_language(self,lang_text):
        dropdown_lang = self.driver.find_element(*self.language_dropdown)
        select = Select(dropdown_lang)
        select.select_by_visible_text(lang_text)

    def select_fav_cat(self,fav_cat_text):
        dropdown_fav_cat = self.driver.find_element(*self.faviourate_cat_dropdown)
        select = Select(dropdown_fav_cat)
        select.select_by_visible_text(fav_cat_text)

    def click_save_acc_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_account_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        
        self.driver.execute_script("arguments[0].click();", button)
