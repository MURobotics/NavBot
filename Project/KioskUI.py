import kivy
from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.11.1')

Builder.load_file('Template.kv')
Builder.load_file('Map.kv')
Builder.load_file('Settings.kv')

class LocationOption(Button):
    pass

# Declare the screens
class MenuScreen(Screen):
    renderLoc = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.name = 'home'
        super(Screen, self).__init__(**kwargs)
        self.renderRooms('Null')

    pass

    def navigationTest(self):
        print('Screen Call')
        #This function won't execute much, but will call the connection.py classes to get relevant info and then probably a navigation.py for running navigation to the destination

    def renderRooms(self, search):
        for i in range(1, 20):
            temp = LocationOption()
            self.renderLoc.add_widget(LocationOption(text='TEST: '+str(i)))

        return

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