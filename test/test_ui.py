from pages.book_page import BookPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
import allure

@allure.severity("Critical")
@allure.id("MainPage-1")
@allure.feature("Доступность главной страницы магазина")
@allure.title("UI тесты")
def test_main_page(browser):
    page = MainPage(browser)
    with allure.step("Перейти на страницу магазина"):
        page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    with allure.step("Закрыть окно запроса на куки"):
        page.close_cookie_notice()
    with allure.step("Проверить, что окно запроса на куки закрыто"):
        assert page.is_cookie_closed()

    with allure.step("Закрыть окно локализации"):
        page.close_location()
    with allure.step("Проверить, что окно локализации закрыто"):
        assert page.is_location_closed()

    with allure.step("Закрыть всплывающее окно"):
        page.close_pop_up()
    with allure.step("Проверить, что всплывающее окно закрыто"):
        assert page.is_pop_up_closed()

@allure.severity("Critical")
@allure.id("BookPage-1")
@allure.feature("Открытие страницы книги")
@allure.title("UI тесты")
def test_book_page(browser):
    page = MainPage(browser)
    with allure.step("Перейти на страницу магазина"):
        page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    page = BookPage(browser)
    with allure.step("Перейти на страницу книги"):
        page.open()
    with allure.step("Закрыть окно подтверждения возраста"):
        page.close_18age()
    with allure.step("Проверить, что окно подтверждения возраста закрыто"):
        assert page.is_18age_closed()
    with allure.step("Проверить наличие наименования книги в заголовке страницы"):
        page.is_book_title()

@allure.severity("Critical")
@allure.id("Cart-1")
@allure.feature("Взаимодействие с корзиной")
@allure.title("UI тесты")
def test_cart_page(browser):
    page = MainPage(browser)
    with allure.step("Перейти на страницу магазина"):
        page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"
    with allure.step("Добавить книгу в корзину"):
        page.add_to_cart()

    page = CartPage(browser)
    with allure.step("Перейти в корзину"):
        page.open_cart()
        page.close_location()
    with allure.step("Проверить наличие элемента в корзине"):
        page.book_in_cart()
    with allure.step("Удалить все книгм из корзины"):
        page.clear_cart()
    with allure.step("Проверить, что отображается сообщение об очистке корзины"):
        assert page.is_cleared()
