from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.XPATH, "//input[@placeholder='Введите имя']")
        self.last_name = (By.XPATH, "//input[@placeholder='Введите фамилию']")
        self.continue_btn = (By.CSS_SELECTOR, "button.continue-btn")

    def set_names(self, first_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        return self

    def complete_registration(self):
        self.driver.find_element(*self.continue_btn).click()
        return self