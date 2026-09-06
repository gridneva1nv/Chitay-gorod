from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """ Класс для работы со страницей корзины.
        Обладает методами для взаимодействия со счетчиком добавленных книг в корзину, со страницей корзины"""

    CART_COUNTER = (By.CSS_SELECTOR, 'span[data-testid-indicator-header="cartCounter"]')
    CARD_BUTTON = (By.XPATH, "//button[@data-testid-button-header='cart']")
    CART_ITEM = (By.CLASS_NAME, "cart-page__products-items")
    CLEAR_BUTTON = (By.XPATH, "//button[@data-testid-button-cart='clearAll']")
    CLEAR_BANER = (By.CLASS_NAME, "cart-multiple-delete__title")
    CART_TITLE = (By.CLASS_NAME, "cart-page__title")

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def cart_conter(self, knig: str) -> bool:
        """Проверка количества книг в счетчике корзины"""
        try:
            if self.wait.until(EC.text_to_be_present_in_element(self.CART_COUNTER, knig)):
                print(f"В счетчике корзины отображается {knig}")
                return True
            else:
                print(f"В счетчике корзины не отображается {knig}")
                return False
        except Exception:
            return False

    def open_cart(self) -> None:
        """Открытие страницы корзины"""

        card_button = self.browser.find_element(*self.CARD_BUTTON)
        card_button.click()
        print("Кнопка корзины нажата")

    def book_in_cart(self) -> None:
        """Проверка наличия книги в корзине"""
        try:
            self.wait.until(EC.visibility_of_element_located(
               self.CART_ITEM
            ))
            print("Книги в корзине")
        except Exception as e:
            print(f'Книги в корзине не обнаружены: {e}')

    def clear_cart(self) -> None:
        """Очистка корзины"""
        try:
            clear_button = self.wait.until(EC.element_to_be_clickable(
                self.CLEAR_BUTTON
            ))
            clear_button.click()
            print("Корзина очищена")
        except Exception as e:
            print(f'Кнопка очистки не найдена:{e}')

    def is_cleared(self) -> bool:
        """Проверка выполнения очистки корзины"""
        try:
            self.wait.until(EC.visibility_of_element_located(
                self.CLEAR_BANER
            ))
            print("Книги из корзины удалены")
            return True
        except Exception:
            print("Книги из корзины не удалены")
            return False

    def is_cart_open(self) -> None:
        """Проверка наличия заголовка корзины"""
        assert self.wait.until(EC.presence_of_element_located(self.CART_TITLE))
