import requests


class APIClient:

    def __init__(self, url):
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            print("API Error:", e)
            return None