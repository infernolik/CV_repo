import pytest, allure
from pytest_check import check
from tests.test_api_positive import BASE_URL

from utils.api_client import BookApiClient

auth_token = None
booking_id = None
booker_name = None
booker_lastname = None


@pytest.fixture
def book_api_client():
    return BookApiClient(BASE_URL)

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Negative testing')
def test_auth(book_api_client):
    global auth_token
    with allure.step("Auth credentials"):
        data = {
            "username" : "admin",
            "password" : "pass111"
        }

    with allure.step("Sending wrong credentials in auth request"):
        response = book_api_client.auth('/auth', data)

    with allure.step("Assertions"):
        with check:
            assert response.status_code == 401
        with check:
            assert response.json()["reason"] == "Bad credentials"

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Negative testing')
def test_post_book(book_api_client):
    global booking_id
    global booker_name
    global booker_lastname

    booker_name = 'John'
    booker_lastname = 'Cena'

    with allure.step("Request body"):
        data = {
            "firstname": booker_name,
            "lastname": booker_lastname
        }
    with allure.step("Sending incomplete booking request"):
        response = book_api_client.post_book('/booking', data)

    with allure.step("Assertions"):
        with check:
            assert response.status_code == 400

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Negative testing')
def test_get_book(book_api_client):
    with allure.step("Requesting nonexistent booking data"):
        response = book_api_client.get_book(f'/booking/55555')

    with allure.step("Assertions"):
        assert response.status_code == 404