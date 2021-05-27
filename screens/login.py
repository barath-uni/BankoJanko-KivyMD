from kivymd.uix.screen import MDScreen
from kivy.app import App
from screens.home import Home
from request_util.request_util import RequestUtil
import json
import os

class Login(MDScreen):

    def open_home(self, *args):
        print("Inside open Home")
        username = self.ids.username.text
        password = self.ids.password.text
        req_util = RequestUtil()
        response = req_util.make_post_request(ENDPOINT_ROUTE="token", data={"username":username, "password": password})
        if response.get('detail') and "Incorrect Username or Password" in response['detail']:
            print("Do not allow login")
            self.ids.error_msg.text = "Incorrect Username Password. Re-enter"
        else:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_name = os.path.join(dir_path, "token_json.json")
            with open(file_name, "w") as json_token:
                token_val = response.get("access_token")
                print(f"TOKEN VAL = {token_val}")
                json.dump({"token": token_val}, json_token)
            self.manager.transition.direction = 'left'
            self.manager.current = 'home_screen'

