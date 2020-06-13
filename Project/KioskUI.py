import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.11.1')

Builder.load_file('screen.kv')

# Declare the screens
class MenuScreen(Screen):
    def changeSettings(self):
        print('Screen Call')
        #This function won't execute much, but will call the connection.py classes to get relevant info and then probably a navigation.py for running navigation to the destination
    pass

class SettingsScreen(Screen):
    def changeSettings(self):
        print('Settings Changed')
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.current = 'menu'

class Menu(App):
    def build(self):
        return sm