import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    """Инициализация браузера для всех тестов"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def auth(driver):
    """Фикстура для страницы авторизации"""
    from pages.auth import AuthPage
    driver.get("https://app.lenzaos.com/auth")
    return AuthPage(driver)

@pytest.fixture
def workspace(auth):
    """Фикстура для страницы workspace"""
    return auth.enter_email("test@test.com")

@pytest.fixture
def profile(workspace):
    """Фикстура для страницы профиля"""
    return workspace.set_workspace_name("TestWorkspace").continue_to_profile()