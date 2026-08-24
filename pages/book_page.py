from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookPage:
    """ Класс для работы со страницей книги
        Обладает методами для взаимодействия с окном подтверждения совершеннолетия, открытия страницы книги, добавления
        книги в корзину"""

    BOOK_DETAIL = (By.CLASS_NAME, "global-page-white-box")
    BOOK_CARD = (By.CLASS_NAME, "product-card__image-wrapper")
    BOOK_TITLE = (By.CLASS_NAME, "product-title__title")
    AGE_ACCEPT = (By.XPATH, "(//div[contains(text(),'Да, мне есть 18 лет')])[1]")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-testid-button-mini-product-card="canBuy"]')

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def close_18age(self):
        """Закрытие окна подтверждения совершеннолетия"""
        try:
            age_button = self.wait.until(EC.element_to_be_clickable(
                self.AGE_ACCEPT
            ))
            age_button.click()
            print("Возраст 18 лет подтвержден")
        except Exception as e:
            print(f'Запрос подтверждения возраста не найден или не был закрыт: {e}')

    def is_18age_closed(self) -> bool:
        """Проверка отсутствия окна подтверждения совершеннолетия"""
        try:
            self.wait.until_not(EC.visibility_of_element_located(
                self.AGE_ACCEPT
            ))
            return True
        except Exception:
            return False

    def open_book(self) -> None:
        """Открытие страницы книги"""
        try:
            self.browser.execute_script("window.scrollBy(0, window.innerHeight);")
            book_element = self.wait.until(EC.element_to_be_clickable(
                self.BOOK_CARD
            ))
            book_element.click()
            self.wait.until(EC.presence_of_element_located(
                self.BOOK_DETAIL
            ))
            print("Переход на страницу информации о книге выполнен.")
        except Exception as e:
            print(f"Не удалось найти элемент книги для перехода на страницу информации: {e}")

    def is_book_title(self) -> None:
        """Проверка отражения названия книги в заголовке страницы"""
        try:
            browser_title = self.browser.title
            print(browser_title)
            book_title = self.wait.until(EC.visibility_of_element_located(
                self.BOOK_TITLE
            )).text
            print(book_title)
            assert book_title in browser_title
            print("Название книги отражено в заголовке страницы")
        except Exception:
            print(f'Название книги не отражено в заголовке страницы')

    def add_to_cart(self) -> None:
        """Добавление книги в корзину"""
        try:
            buy_element = self.wait.until(EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            ))
            buy_element.click()
            print("Книга добавлена в корзину.")
        except Exception as e:
            print(f"Не удалось найти кнопку для добавления в корзину: {e}")
