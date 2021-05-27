from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.app import MDApp
from pathlib import Path
from kivy.uix.screenmanager import ScreenManager

from screens.home import Home
from screens.login import Login
from screens.moneytransfer import MoneyTransfer
from ui import UI
from kivy.lang import Builder


class MainApp(MDApp):

    def build(self):
        Builder.load_file('screens/home.kv')
        Builder.load_file('screens/login.kv')
        Builder.load_file('screens/moneytransfer.kv')
        sm = ScreenManager()
        sm.add_widget(Login(name='login_screen'))
        sm.add_widget(Home(name='home_screen'))
        sm.add_widget(MoneyTransfer(name='money_transfer_screen'))
        return sm


if __name__ == '__main__':
    MainApp().run()

