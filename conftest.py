import pytest
from selenium import webdriver
import requests
from config import BASE_URL, TOKEN_API


@pytest.fixture(scope="session")
def browser():
    """Инициализация браузера для сессии с разворачиванием на полный экран."""
    browser = webdriver.Chrome()
    browser.maximize_window()  # Разворнуть окно на весь экран
    yield browser
    browser.quit()  # Закрыть браузер после выполнения тестов

@pytest.fixture
def headers():
    """Фикстура для заголовков с токеном авторизации"""
    headers = {
        'accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': BASE_URL,
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN_API}'
    }
    return headers

@pytest.fixture
def params():
    """Фикстура для параметров поиска"""
    params = {
        'phrase': 'phrase',
        'include': 'authors,bookCycles,categories,publishers,publisherSeries,products',
        'products[per-page]': 60,
        'products[page]': 1
    }
    return params