from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SerchPage:
    def __init__(self, driver):
        self.driver = driver
        # Use consistent locator names
        self.search_box_locator = (By.XPATH, "//*[@id='jpetstore-content']/div[1]/div/form/div/input")
        self.search_box_icon_locator = (By.XPATH, "//*[@id='jpetstore-search-btn']")

    def search_item_typing(self, item_name, press_enter=False):
        # Wait for element before interacting
        search_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(item_name)
        if press_enter:
            search_box.send_keys(Keys.ENTER)

    def search_item_icon(self, key_text=None):
        search_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.search_box_locator)
        )
        if key_text:
            search_box.clear()
            search_box.send_keys(key_text)

        icon_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.search_box_icon_locator)
        )
        icon_btn.click()

    def get_product_element(self):
        locator = (By.XPATH, "//*[@id='jpetstore-content']/div[2]/table/tbody/tr[2]/td[1]/strong/a")
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def search_invalid_item(self,key_text2,press_enter=False):
        search_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(key_text2)
        if press_enter:
            search_box.send_keys(Keys.ENTER)




