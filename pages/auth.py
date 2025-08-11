from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.language_btn = (By.CSS_SELECTOR, "button.lang-switch")
        self.email_input = (By.CSS_SELECTOR, "input#email-input")
        self.continue_btn = (By.XPATH, "//button[not(@disabled)]")

    def switch_language(self, language):
        self.driver.find_element(*self.language_btn).click()
        self.driver.find_element(
            By.XPATH, f"//div[@class='context-menu__option']//span[contains(., '{language}')]"
        ).click()
        return self

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input)
        ).send_keys(email)
        self.driver.find_element(*self.continue_btn).click()
        from pages.workspace import WorkspacePage
        return WorkspacePage(self.driver)