from kivymd.uix.screen import MDScreen
import os
import json

from request_util.request_util import RequestUtil


class MoneyTransfer(MDScreen):

    def transfer_money(self, *args):
        request_util = RequestUtil()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(dir_path, "token_json.json")
        print(file_name)
        with open(file_name, "r") as token_json:
            token = json.load(token_json)['token']
        current_user = token
        destination_user = self.ids.dest_account_number.text
        amount_to_transfer = self.ids.amount.text
        ifsc_swift = self.ids.ifsc_swift_code.text
        res = request_util.make_post_request(ENDPOINT_ROUTE="transfer_money",
                                       token=token,
                                       json={"destination_user": destination_user,
                                             "amount_to_transfer": amount_to_transfer})
        if "successfully Transferred" in res.get('message'):
            # Fill the label as success
            self.ids.confirmation_label.text = res.get('message')
