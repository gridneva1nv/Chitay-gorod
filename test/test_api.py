import pytest
import requests
import allure
from config import BOOK_URL, SERCH_URL

@allure.severity("Critical")
@allure.id("BookPage-2")
@allure.feature("Проверка получения информации о книге")
@allure.title("API тесты: Получение информации о книге по её slug")
@pytest.mark.api
@pytest.mark.positive
def test_book_info_api(headers):
    book_slug = "poslednee-zelanie-3089169"
    with allure.step("Отправка запроса на получение информации о книге"):
        response = requests.get(f'{BOOK_URL}/products/slug/{book_slug}', headers=headers)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, но получен {response.status_code}"
    with allure.step("Проверка наличия поля 'title' в ответе"):
        data = response.json().get("data", {})
        assert "title" in data, "Отсутствует поле 'title' в ответе"

@allure.severity("Critical")
@allure.id("Cart-2")
@allure.feature("Взаимодействие с корзиной")
@allure.title("API тест: Проверка доступности корзины")
@pytest.mark.api
@pytest.mark.positive
def test_view_cart(headers):
    with allure.step("Отправка запроса на просмотр корзины"):
        response = requests.get(f'{BOOK_URL}/cart', headers=headers)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, но получен {response.status_code}"

@allure.severity("Critical")
@allure.id("Cart-3")
@allure.feature("Взаимодействие с корзиной")
@allure.title("API тест: Добавление книги в корзину")
@pytest.mark.api
@pytest.mark.positive
def test_add_book_to_cart_api(headers):
    book_id = 3089169
    body = {"id": book_id}
    with allure.step("Отправка запроса на добавление книги в корзину"):
        response = requests.post(f'{BOOK_URL}/cart/product', headers=headers, json=body)
    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, но получен {response.status_code}"
    with allure.step("Проверка подтверждения добавления книги в ответе"):
        if response.text.strip():
            response_data = response.json()
            assert book_id in response_data, f"Отсутствует подтверждение добавления в корзину"

@allure.severity("Critical")
@allure.id("Cart-4")
@allure.feature("Взаимодействие с корзиной")
@allure.title("API тест: Очистка корзины")
@pytest.mark.api
@pytest.mark.positive
def test_clear_cart_api(headers):
    book_id = 3089169
    body = {"id": book_id}
    with allure.step("Отправка запроса на добавление книги в корзину"):
        response = requests.post(f'{BOOK_URL}/cart/product', headers=headers, json=body)
    with allure.step("Проверка подтверждения добавления книги в ответе"):
        if response.text.strip():
            response_data = response.json()
            assert "id" in response_data, f"Отсутствует подтверждение добавления в корзину"
    with allure.step("Отправка запроса на очистку корзины"):
        response_body = {"deleteAll": True}
        response = requests.delete(f'{BOOK_URL}/cart', headers=headers, json=response_body)
    with allure.step("Проверка статус кода 204"):
        assert response.status_code == 204, f"Ошибка: ожидался статус 204, но получен {response.status_code}"
    with allure.step("Отправка запроса на просмотр корзины"):
        response = requests.get(f'{BOOK_URL}/cart', headers=headers)
    with allure.step("Проверка отсутствия книг в корзине"):
        response_data = response.json()
        assert len(response_data['products']) == 0, f"Корзина не пуста"

@allure.severity("Critical")
@allure.id("Search-1")
@allure.feature("Поиск книг")
@allure.title("позитивные тесты")
@pytest.mark.api
@pytest.mark.positive
@pytest.mark.parametrize ("input_str, expected",[
    ("тестировщик", 200),
    ("дети капитана гранта", 200)
])
def test_search_api_positive(headers, input_str, expected):
    params = {'phrase': input_str}
    with allure.step("Отправка запроса на поиск текста"):
        response = requests.get(f'{SERCH_URL}/search/product', headers=headers, params=params)
    with allure.step(f"Проверка статус кода {expected}"):
        assert response.status_code == expected, f'Ошибка: ожидался статус {expected}, но получен {response.status_code}'

allure.severity("Critical")
@allure.id("Search-2")
@allure.feature("Поиск книг")
@allure.title("негативные тесты")
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.parametrize ("input_str, expected",[
    ("1", 400),
    (None, 400),
    ("  ", 422),
    (".)", 422),
])
def test_search_api_negative(headers, input_str, expected):
    params = {'phrase': input_str}
    with allure.step("Отправка запроса на поиск текста"):
        response = requests.get(f'{SERCH_URL}/search/product', headers=headers, params=params)
        resp = response.json()['errors'][0]['title']
        print(resp)
    with allure.step(f"Проверка статус кода {expected}"):
        assert response.status_code == expected, f'Ошибка: ожидался статус {expected}, но получен {response.status_code}'
