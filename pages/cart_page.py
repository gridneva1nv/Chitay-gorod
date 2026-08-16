from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CART_URL


class CartPage:
    """ Класс для работы со страницей корзины"""

    CART_ITEM = (By.CLASS_NAME, "cart-page__products-items")
    CLEAR_BUTTON = (By.XPATH, "//button[@data-testid-button-cart()='clearAll'")
    CLEAR_BANER = (By.CLASS_NAME, "cart-multiple-delete__title")
    LOCATION_BOX = (By.CLASS_NAME, "tippy-box")
    LOCATION_BUTTON = (By.CLASS_NAME, "header-location")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def open_cart(self) -> None:
        """Открытие страницы корзины"""
        self.browser.get(CART_URL)

    def book_in_cart(self) -> None:
        """Проверка наличия книги в корзине"""
        try:
            self.wait.until(EC.visibility_of_element_located(
               self.CART_ITEM
            ))
            print("Книги в корзине")
        except Exception as e:
            f'Книги в корзине не обнаружены: {e}'

    def clear_cart(self) -> None:
        """Очистка корзины"""
        try:
            self.wait.until(EC.element_to_be_clickable(
                self.CLEAR_BUTTON
            ))
            print("Корзина очищена")
        except Exception as e:
            f'Кнопка очистки не найдена:{e}'

    def is_cleared(self) -> bool:
        """Проверка выполнения очистки корзины"""
        try:
            self.wait.until(EC.visibility_of_element_located(
                self.CLEAR_BANER
            ))
            print("Корзина пуста")
            return True
        except Exception:
            return False

    def close_location(self) -> None:
        """Закрытие окна локализации"""
        try:
            self.wait.until(EC.visibility_of_element_located(
                self.LOCATION_BOX
            ))
            location_button = self.wait.until(EC.element_to_be_clickable(
                self.LOCATION_BUTTON
            ))
            location_button.click()
            print("Запрос локализации закрыт")
        except Exception as e:
            f'Запрос локализации не найден или не был закрыт: {e}'