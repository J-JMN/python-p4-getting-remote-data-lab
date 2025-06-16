import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Get the raw byte response from the server
        response = requests.get(self.url)
        return response.content  # returns raw bytes

    def load_json(self):
        # Use response content and decode JSON into Python data structures
        response = requests.get(self.url)
        return response.json()  # returns Python list or dict
