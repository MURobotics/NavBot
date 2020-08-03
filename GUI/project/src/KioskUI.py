import kivy
#from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import (ScreenManager, Screen)
from kivy.uix.vkeyboard import VKeyboard
from kivy.config import Config

import Alert as AlertClass
from Connect import RosNode

RN = RosNode()
RN.toggle()

kivy.require('1.11.1')

Builder.load_file('Template.kv')
Builder.load_file('Map.kv')
Builder.load_file('Settings.kv')
Builder.load_file('Alerts.kv')
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
Config.write()

class LocationOption(Button):
    pass

class Test(VKeyboard):
    player = VKeyboard()

class LimitInput(TextInput):
    def keyboard_on_key_up(self, keycode, text):
        if self.readonly and text[1] == "backspace":
            self.readonly = False
            self.do_backspace()
# Credit to user Jaivin https://groups.google.com/forum/#!topic/kivy-users/xTcDcm2eKEE

# Declare the screens
class MenuScreen(Screen):
    renderLoc = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.name = 'home'
        super(Screen, self).__init__(**kwargs)
        self.renderRooms()

    def navigationTest(self):
        print('Screen Call')
        # This function won't execute much, but will call the connection.py classes to get relevant info and then probably a navigation.py for running navigation to the destination

    def renderRooms(self):
        self.renderLoc.clear_widgets()
        for i in range(1, 20):
            temp = LocationOption()
            self.renderLoc.add_widget(LocationOption(text=self.search.text + str(i)))

class SettingsScreen(Screen):

    def changeSettings(self):
        print('Settings Changed')
        RN.toggle()

    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(AlertClass.Suspend(name='Suspend'))
sm.add_widget(AlertClass.LowPower(name='LowPower'))
sm.add_widget(AlertClass.Error(name='Error'))
sm.add_widget(AlertClass.Success(name='Success'))
sm.current = 'menu'


class Menu(App):
    def build(self):
        return sm
