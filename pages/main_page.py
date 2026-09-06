from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL


class MainPage:
    """ Класс для работы с главной страницей интернет магазина "Читай-город"
        Обладает методами для взаимодействия с окном локализации, всплывающим окном, окном запроса на куки, открытия корзины
    """
    POPUP_BUTTON = (By.CLASS_NAME, "popmechanic-close")
    COOKIE_BUTTON = (By.XPATH, "(//div[contains(text(),'Понятно, закрыть')])[1]")
    LOCATION_BOX = (By.CLASS_NAME, "tippy-box")
    LOCATION_BUTTON = (By.XPATH, "(//div[contains(text(),'Да, я здесь')])[1]")
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
