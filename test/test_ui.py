import pytest
from selenium import webdriver
from pages.book_page import BookPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from config import CART_URL
import allure

@allure.severity("BLOCKER")
@allure.id("MainPage-1")
@allure.feature("Доступность главной страницы магазина")
@allure.title("UI тесты")
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
@allure.title("UI тесты")
@pytest.mark.ui
@pytest.mark.positive
def test_book_page(browser):
    m_page = MainPage(browser)
    with allure.step("Перейти на страницу магазина"):
        m_page.open()
        assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"

    b_page = BookPage(browser)
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
@allure.title("UI тесты")
@pytest.mark.ui
@pytest.mark.positive
def test_cart_page(browser):
    m_page = MainPage(browser)
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

    with allure.step("Добавить книгу в корзину"):
        m_page.add_to_cart()
    with allure.step("Перейти в корзину"):
        m_page.open_cart()
        assert browser.current_url == CART_URL

    c_page = CartPage(browser)
    with allure.step("Закрыть окно локализации"):
        c_page.close_location()
    with allure.step("Проверить наличие элемента в корзине"):
        c_page.book_in_cart()
    with allure.step("Удалить все книгм из корзины"):
        c_page.clear_cart()
    with allure.step("Проверить, что отображается сообщение об очистке корзины"):
        assert c_page.is_cleared()

# @allure.severity("Critical")
# @allure.id("Search-3")
# @allure.feature("Поиск книг (позитивный)")
# @allure.title("Поиск книг с получением списка")
# @pytest.mark.ui
# @pytest.mark.positive
# @pytest.mark.parametrize ("input_str",[
#     "тестировщик",
#     "дети капитана гранта"
# ])
# def test_search_ui_positive(browser, input_str):
#     page = MainPage(browser)
#     with allure.step("Перейти на страницу магазина"):
#         page.open()
#         assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"
#     with allure.step("Закрыть окно локализации"):
#         page.close_location()
#     with allure.step("Проверить, что окно локализации закрыто"):
#         assert page.is_location_closed()
#
#     with allure.step("Ввести значение в поле поиска"):
#         page.send_phrase(input_str)
#     with allure.step("Нажать кнопку Поиск"):
#         page.find_book()
#     with allure.step("Проверить, что отображается список книг"):
#         assert page.book_items() > 0, print("Элементы, соответствующие поиску не найдены")
#
# @allure.severity("Critical")
# @allure.id("Search-4")
# @allure.feature("Поиск книг (негативный)")
# @allure.title("UI тесты")
# @pytest.mark.ui
# @pytest.mark.negative
# @pytest.mark.parametrize ("input_str",[
#     "1",
#     None,
#     "  ",
#     ".)",
#     ";-"
# ])
# def test_search_ui_negative(browser, input_str):
#     page = MainPage(browser)
#     with allure.step("Перейти на страницу магазина"):
#         page.open()
#         assert browser.title == "Читай-город — магазин интересных книг, подарков и канцелярии"
#     with allure.step("Закрыть окно локализации"):
#         page.close_location()
#     with allure.step("Проверить, что окно локализации закрыто"):
#         assert page.is_location_closed()
#
#     with allure.step("Ввести значение в поле поиска"):
#         page.send_phrase(input_str)
#     with allure.step("Нажать кнопку Поиск"):
#         page.find_book()
#     with allure.step("Проверить, что список книг отсутствует"):
#         assert page.book_items() == 0, print("Элементы, соответствующие поиску не найдены")