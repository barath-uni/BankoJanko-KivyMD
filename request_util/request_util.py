import requests


class RequestUtil(object):
    URL_ENDPOINT = "http://192.168.1.2"
    PORT = 8000

    def make_post_request(self, ENDPOINT_ROUTE:str, data=None, json=None, token=None):
        headers = None
        if token:
            headers = {"token": token}
        res = requests.post(url=f"{self.URL_ENDPOINT}:{self.PORT}/{ENDPOINT_ROUTE}", data=data,
                            json=json, headers=headers)
        print(f"Response from the Server = {res.json()}")
        return res.json()

    def make_get_request(self, ENDPOINT_ROUTE: str, token: str):
        res = requests.get(url=f"{self.URL_ENDPOINT}:{self.PORT}/{ENDPOINT_ROUTE}", headers={"token": token})
        print(f"RESPONE = {res.json()}")
        return res.json()

