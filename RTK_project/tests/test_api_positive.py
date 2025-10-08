import pytest, allure

from utils.api_client import BookApiClient

BASE_URL = "https://restful-booker.herokuapp.com"
auth_token = None
booking_id = None
booker_name = None
booker_lastname = None


@pytest.fixture
def book_api_client():
    return BookApiClient(BASE_URL)

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Positive testing')
def test_auth(book_api_client):
    global auth_token
    with allure.step("Auth credentials"):
        data = {
            "username" : "admin",
            "password" : "password123"
        }

    with allure.step("Sending auth request"):
        response = book_api_client.auth('/auth', data)

    with allure.step("Assertions"):
        assert response.status_code == 200
        assert "token" in response.json()

    if "token" in response.json():
        auth_token = response.json()["token"]

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Positive testing')
def test_post_book(book_api_client):
    global booking_id
    global booker_name
    global booker_lastname

    booker_name = 'John'
    booker_lastname = 'Cena'

    with allure.step("Request body"):
        data = {
            "firstname": booker_name,
            "lastname": booker_lastname,
            "depositpaid": True,
            "totalprice": 1000,
            "bookingdates": {
                "checkin": "2030-09-02",
                "checkout": "2030-10-10"
            }
        }
    with allure.step("Sending booking request"):
        response = book_api_client.post_book('/booking', data)

    with allure.step("Assertions"):
        assert response.status_code == 200
        assert response.json()['booking']['firstname'] == booker_name
        assert response.json()['booking']['lastname'] == booker_lastname

    if "bookingid" in response.json():
        booking_id = int(response.json()['bookingid'])

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Positive testing')
def test_get_book(book_api_client):
    with allure.step("Requesting booking data"):
        response = book_api_client.get_book(f'/booking/{booking_id}')

    with allure.step("Assertions"):
        assert response.status_code == 200
        assert response.json()['firstname'] == booker_name
        assert response.json()['lastname'] == booker_lastname

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Positive testing')
def test_partial_update_book(book_api_client):
    with allure.step("Request body"):
        data = {
            "totalprice": 5555,
            "bookingdates": {
                "checkin": "2025-09-02",
                "checkout": "2025-10-10"
            }
        }

    with allure.step("Headers"):
        headers = {
            "Cookie": f"token={auth_token}"
        }

    with allure.step('Sending partial update request'):
        response = book_api_client.partial_update_book(f'/booking/{booking_id}', data, headers)

    with allure.step("Assertions"):
        assert response.status_code == 200
        assert response.json()['totalprice'] == 5555
        assert response.json()['bookingdates']['checkin'] == '2025-09-02'
        assert response.json()['bookingdates']['checkout'] == '2025-10-10'
        assert response.json()['firstname'] == booker_name
        assert response.json()['lastname'] == booker_lastname

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Positive testing')
def test_update_book(book_api_client):
    global booker_name
    global booker_lastname
    booker_name = 'Zato'
    booker_lastname = 'One'

    with allure.step("Request body"):

        data = {
            "firstname": booker_name,
            "lastname": booker_lastname,
            "depositpaid": False,
            "totalprice": 3333,
            "bookingdates": {
                "checkin": "2027-04-02",
                "checkout": "2027-05-10"
            }
        }

    with allure.step("Headers"):
        headers = {
            "Cookie": f"token={auth_token}"
        }

    with allure.step('Sending update request'):
        response = book_api_client.update_book(f'/booking/{booking_id}', data, headers)

    with allure.step('Assertions'):
        assert response.status_code == 200
        assert response.json()['firstname'] == 'Zato'
        assert response.json()['lastname'] == 'One'

@allure.epic('API Client')
@allure.feature('CRUD operations')
@allure.story('Positive testing')
def test_delete_book(book_api_client):
    with allure.step('Headers'):
        headers = {
            "Cookie": f"token={auth_token}"
        }

    with allure.step('Sending delete request'):
        response = book_api_client.delete_book(f'/booking/{booking_id}', headers)

    with allure.step('Assertions'):
        assert response.status_code == 201