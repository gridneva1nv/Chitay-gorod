from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL


class MainPage:
    """ Класс для работы с главной страницей интернет магазина "Читай-город"
        У класса есть окно локализации, всплывающее окно, окно запроса на куки
    """
    POPUP_BUTTON = (By.CLASS_NAME, "popmechanic-close")
    COOKIE_BUTTON = (By.XPATH, "(//div[contains(text(),'Понятно, закрыть')])[1]")
    LOCATION_BOX = (By.CLASS_NAME, "tippy-box")
    LOCATION_BUTTON = (By.XPATH, "(//div[contains(text(),'Да, я здесь')])[1]")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//div[@class='chg-app-button chg-app-button--primary chg-app-button--s chg-app-button--breeze product-buttons__main-action product-buttons__main-action--stretch product-buttons__main-action product-buttons__main-action--stretch'])[2]")
    CARD_BUTTON = (By.XPATH, "//button[@aria-label='Корзина']")
    SEARCH_FORM = (By.ID, "app-search")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-form__icon-search")
    BOOK_ITEM = (By.CLASS_NAME, "product-card__caption")

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)

    def open(self) -> None:
        """Открытие главной страницу магазина"""
        self.browser.get(BASE_URL)

    def close_pop_up(self) -> None:
        """Закрытие всплывающего окно"""
        try:
            popup_button = self.wait.until(EC.element_to_be_clickable(
                self.POPUP_BUTTON
            ))
            popup_button.click()
            print("Всплывающее окно закрыто.")
        except Exception as e:
            print(f"Всплывающее окно не найдено или не было закрыто: {e}")

    def is_pop_up_closed(self) -> bool:
        """Проверка, что всплывающее окно закрыто"""
        try:
            self.wait.until_not(EC.visibility_of_element_located(
                self.POPUP_BUTTON
            ))
            return True
        except Exception:
            return False

    def close_cookie_notice(self) -> None:
        """Закрытие окна запроса на куки"""
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(
                    self.COOKIE_BUTTON
            ))
            cookie_button.click()
            print("Уведомление о куки закрыто.")
        except Exception as e:
            print(f"Уведомление о куки не найдено или не было закрыто: {e}")

    def is_cookie_closed(self) -> bool:
        """Проверка, что окно запроса на куки закрыто"""
        try:
            self.wait.until_not(EC.visibility_of_element_located(
                self.COOKIE_BUTTON
            ))
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
            print(f'Запрос локализации не найден или не был закрыт: {e}')

    def is_location_closed(self) -> bool:
        """Проверка, что окно локализации закрыто"""
        try:
            self.wait.until_not(EC.visibility_of_element_located(
                self.LOCATION_BOX
            ))
            return True
        except Exception:
            return False
    def add_to_cart(self)-> None:
        """Добавление книги в корзину"""
        try:
            element = self.wait.until(EC.presence_of_element_located(
                self.ADD_TO_CART_BUTTON
            ))
            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            buy_element = self.wait.until(EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            ))
            buy_element.click()
            print("Книга добавлена в корзину.")
        except Exception as e:
            print(f"Не удалось найти кнопку для добавления в корзину: {e}")

    def open_cart(self) -> None:
        """Открытие страницы корзины"""
        try:
            card_button = self.wait.until(EC.element_to_be_clickable(
                self.CARD_BUTTON
            ))
            card_button.click()
            print("Кнопка корзины нажата")
        except Exception as e:
            print(f'Кнопка корзины не найдена: {e}')

    def send_phrase(self, phrase: str) -> None:
        """Внесение фразы в поле поиска"""
        try:
            search_form = self.wait.until(EC.element_to_be_clickable(
                self.SEARCH_FORM
            ))
            search_form.clear()
            search_form.send_keys(f"{phrase}")
            print(f"В поле поиска внесена фраза: {phrase}")
        except Exception as e:
            print(f"Поле поиска не найдено или недоступно: {e}")

    def find_book(self) -> None:
        """Запуск поиска книг по фразе из строки поиска"""
        try:
            search_button = self.wait.until(EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            ))
            search_button.click()
            print("Кнопка поиска нажата")
        except Exception as e:
            print(f"Кнопка поиска не нажата или не найдена: {e}")

    def book_items(self) -> int:
        """Получение количества книг со страницы"""
        books = []
        books = self.browser.find_elements(
            *self.BOOK_ITEM
        )
        return len(books)