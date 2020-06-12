import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    about = ObjectProperty(None)
    findroom = ObjectProperty(None)

    def aboutFunc(self):
        print("About called")

    def findRoomFunc(self):
        print("Find Room Called")

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()