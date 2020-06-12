import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.11.1')

Builder.load_file('screen.kv')

# Declare the screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.current = 'menu'



class Menu(App):
    def build(self):
        return sm