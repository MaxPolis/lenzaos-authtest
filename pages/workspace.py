from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WorkspacePage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.CSS_SELECTOR, "input#domain-company")
        self.continue_btn = (By.XPATH, "//button[contains(., 'Продолжить')]")

    def set_workspace_name(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_input)
        ).send_keys(name)
        return self

    def continue_to_profile(self):
        self.driver.find_element(*self.continue_btn).click()
        from pages.profile import ProfilePage
        return ProfilePage(self.driver)