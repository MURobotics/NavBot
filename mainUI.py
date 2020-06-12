import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file("floatlayout.kv")

class MainWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class FindRoomWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class FloatLayoutApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    FloatLayoutApp().run()