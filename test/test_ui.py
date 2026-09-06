import pytest
from pages.book_page import BookPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from config import CART_URL
import allure

@allure.severity("BLOCKER")
@allure.id("MainPage-1")
@allure.feature("Доступность главной страницы магазина")
@allure.title("UI тесты: Доступность главной страницы магазина")
@pytest.mark.ui
@pytest.mark.positive
def test_main_page(browser):
    page = MainPage(browser)

    with allure.step("Перейти на страницу магазина"):
        page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    with allure.step("Закрыть окно локализации"):
        page.close_location()
    with allure.step("Проверить, что окно локализации закрыто"):
        assert page.is_location_closed()

    with allure.step("Закрыть окно запроса на куки"):
        page.close_cookie_notice()
    with allure.step("Проверить, что окно запроса на куки закрыто"):
        assert page.is_cookie_closed()

    with allure.step("Закрыть всплывающее окно"):
        page.close_pop_up()
    with allure.step("Проверить, что всплывающее окно закрыто"):
        assert page.is_pop_up_closed()

@allure.severity("Critical")
@allure.id("BookPage-1")
@allure.feature("Открытие страницы книги")
@allure.title("UI тесты: Открытие страницы книги")
@pytest.mark.ui
@pytest.mark.positive
def test_book_page(browser):
    m_page = MainPage(browser)
    b_page = BookPage(browser)

    with allure.step("Перейти на страницу магазина"):
        m_page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    with allure.step("Перейти на страницу книги"):
        b_page.open_book()
    with allure.step("Закрыть окно подтверждения возраста"):
        b_page.close_18age()
    with allure.step("Проверить, что окно подтверждения возраста закрыто"):
        assert b_page.is_18age_closed()
    with allure.step("Проверить наличие наименования книги в заголовке страницы"):
        b_page.is_book_title()

@allure.severity("Critical")
@allure.id("Cart-1")
@allure.feature("Взаимодействие с корзиной")
@allure.title("UI тесты: Добавление книги в корзину")
@pytest.mark.ui
@pytest.mark.positive
def test_add_book_in_cart(browser):
    m_page = MainPage(browser)
    b_page = BookPage(browser)
    c_page = CartPage(browser)

    with allure.step("Перейти на страницу магазина"):
        m_page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    with allure.step("Закрыть окно запроса на куки"):
        m_page.close_cookie_notice()
    with allure.step("Проверить, что окно запроса на куки закрыто"):
        assert m_page.is_cookie_closed()

    with allure.step("Закрыть всплывающее окно"):
        m_page.close_pop_up()
    with allure.step("Проверить, что всплывающее окно закрыто"):
        assert m_page.is_pop_up_closed()

    with allure.step("Перейти на страницу книги"):
        b_page.open_book()
    with allure.step("Закрыть окно подтверждения возраста"):
        b_page.close_18age()
    with allure.step("Проверить, что окно подтверждения возраста закрыто"):
        assert b_page.is_18age_closed()

    with allure.step("Добавить книгу в корзину"):
        b_page.add_to_cart()
    with allure.step("Проверить отображение '1' в счетчике корзины"):
        assert c_page.cart_conter("1")

@allure.severity("Critical")
@allure.id("Cart-2")
@allure.feature("Взаимодействие с корзиной")
@allure.title("UI тесты: Переход в корзину")
@pytest.mark.ui
@pytest.mark.positive
def test_open_cart(browser):
    page = MainPage(browser)
    c_page = CartPage(browser)

    with allure.step("Перейти на страницу магазина"):
        page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    with allure.step("Закрыть окно локализации"):
        page.close_location()
    with allure.step("Проверить, что окно локализации закрыто"):
        assert page.is_location_closed()

    with allure.step("Перейти в корзину"):
        c_page.open_cart()
    with allure.step("Проверить, что перешли на страницу корзины"):
        c_page.is_cart_open()
        assert browser.current_url == CART_URL

@allure.severity("Critical")
@allure.id("Cart-3")
@allure.feature("Взаимодействие с корзиной")
@allure.title("UI тесты: Очистка корзины")
@pytest.mark.ui
@pytest.mark.positive
def test_clear_cart(browser):
    m_page = MainPage(browser)
    b_page = BookPage(browser)
    c_page = CartPage(browser)

    with allure.step("Перейти на страницу магазина"):
        m_page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    with allure.step("Закрыть окно запроса на куки"):
        m_page.close_cookie_notice()
    with allure.step("Проверить, что окно запроса на куки закрыто"):
        assert m_page.is_cookie_closed()

    with allure.step("Закрыть всплывающее окно"):
        m_page.close_pop_up()
    with allure.step("Проверить, что всплывающее окно закрыто"):
        assert m_page.is_pop_up_closed()

    with allure.step("Перейти на страницу книги"):
        b_page.open_book()
    with allure.step("Закрыть окно подтверждения возраста"):
        b_page.close_18age()
    with allure.step("Проверить, что окно подтверждения возраста закрыто"):
        assert b_page.is_18age_closed()

    with allure.step("Добавить книгу в корзину"):
        b_page.add_to_cart()
    with allure.step("Проверить отображение '1' в счетчике корзины"):
        assert c_page.cart_conter("1")

    with allure.step("Перейти в корзину"):
        c_page.open_cart()
    with allure.step("Проверить, что перешли на страницу корзины"):
        c_page.is_cart_open()
        assert browser.current_url == CART_URL

    with allure.step("Закрыть окно локализации"):
         m_page.close_location()
    with allure.step("Проверить наличие элемента в корзине"):
         c_page.book_in_cart()
    with allure.step("Удалить все книгм из корзины"):
        c_page.clear_cart()
    with allure.step("Проверить, что отображается сообщение об очистке корзины"):
        assert c_page.is_cleared()
