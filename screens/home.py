from kivy.uix.carousel import Carousel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
import json
from request_util.request_util import RequestUtil
import os


class Home(MDScreen):

    def on_pre_enter(self, *args):
        self.req_util = RequestUtil()
        widget = self.create_carousel()
        cred_card = self.create_credit_history_card()
        print(widget)
        if cred_card:
            self.ids.main_box_layout.add_widget(cred_card)
        self.ids.main_box_layout.add_widget(MDSeparator())
        self.ids.main_box_layout.add_widget(MDSeparator())
        if widget:
            self.ids.main_box_layout.add_widget(widget)
        self.ids.main_box_layout.add_widget(MDSeparator())

    def read_spend_history(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(dir_path, "token_json.json")
        print(file_name)
        with open(file_name, "r") as token_json:
            token = json.load(token_json)['token']
        print(token)
        # Make a request to read the entire spend history
        res = self.req_util.make_get_request(ENDPOINT_ROUTE="spend/history", token=token)
        return res

    def create_carousel(self):
        """"""
        carousel = Carousel()
        # Read the data for the carousel
        data = self.read_spend_history()
        if data:
            # Parse the data and create a dynamic carousel and add
            for key in data.get("spend_hist"):
                print(key)
                value = data.get('spend_hist')[key]
                mdcard = MDCard(size=("400dp", "120dp"))
                mdboxlayout = MDBoxLayout(orientation='vertical', padding="10dp", spacing="10dp")
                mdlabel_month = MDLabel(text=f"Month:{key}", theme_text_color="Secondary")
                mdlabel_value_spend = MDLabel(text=f"TOTAL SPEND: {value.get('total_spend')}")
                mdlabel_value_liability = MDLabel(text=f"Liability: {value.get('total_spend')}")
                mdlabel_value_asset = MDLabel(text=f"Asset: {value.get('total_spend')}")
                mdboxlayout.add_widget(mdlabel_month)
                mdboxlayout.add_widget(mdlabel_value_spend)
                mdboxlayout.add_widget(mdlabel_value_liability)
                mdboxlayout.add_widget(mdlabel_value_asset)
                mdcard.add_widget(mdboxlayout)
                carousel.add_widget(mdcard)
        return carousel

    def read_credit_history(self):
        """"""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(dir_path, "token_json.json")
        print(file_name)
        with open(file_name, "r") as token_json:
            token = json.load(token_json)['token']
        print(token)
        # Make a request to read the entire spend history
        res = self.req_util.make_get_request(ENDPOINT_ROUTE="creditcard/history", token=token)
        return res

    def create_credit_history_card(self):
        """"""
        boxlayout = MDBoxLayout(orientation='vertical', padding="10dp", spacing="10dp")
        # Read the data for the carousel
        data = self.read_credit_history()
        mdcard = MDCard(size=("400dp", "120dp"))
        mdlabel = MDLabel(text="CREDIT CARD HISTORY")
        mdlabel_cred_bal = MDLabel(text=f"CREDIT BALANCE :{data['credit_hist']['credit_balance']}", theme_text_color="Secondary")
        mdlabel_cred_paid = MDLabel(text=f"CREDIT PAID :{data['credit_hist']['credit_paid']}", theme_text_color="Secondary")
        mdlabel_cred_rolling = MDLabel(text=f"CREDIT ROLLING :{data['credit_hist']['credit_rolling']}",
                                       theme_text_color="Secondary")
        boxlayout.add_widget(mdlabel)
        boxlayout.add_widget(mdlabel_cred_bal)
        boxlayout.add_widget(mdlabel_cred_paid)
        boxlayout.add_widget(mdlabel_cred_rolling)
        mdcard.add_widget(boxlayout)
        return mdcard
