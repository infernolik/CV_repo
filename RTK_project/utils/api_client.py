import requests

class BookApiClient:
    def __init__(self, domain_url):
        self.domain_url = domain_url

    def auth(self, endpoint, data=None, headers=None):
        url = f"{self.domain_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    def get_book(self, endpoint, params=None, headers=None):
        url = f"{self.domain_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    def post_book(self, endpoint, data=None, headers=None):
        url = f"{self.domain_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    def update_book(self, endpoint, data=None, headers=None):
        url = f"{self.domain_url}{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def partial_update_book(self, endpoint, data=None, headers=None):
        url = f"{self.domain_url}{endpoint}"
        response = requests.patch(url, json=data, headers=headers)
        return response

    def delete_book(self, endpoint, headers=None):
        url = f"{self.domain_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response