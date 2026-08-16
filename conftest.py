import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    """Инициализация браузера для сессии с разворачиванием на полный экран."""
    browser = webdriver.Chrome()
    browser.maximize_window()  # Разворнуть окно на весь экран
    yield browser
    browser.quit()  # Закрыть браузер после выполнения тестов
