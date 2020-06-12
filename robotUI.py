import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GridHolder(GridLayout):
    def __init__(self, **kwargs):
        super(GridHolder, self).__init__(**kwargs)
        self.cols = 2

        self.inside = GridLayout()
        self.inside.cols = 1

        self.findRoom = Button(text="Find Room", font_size=35)
        self.findRoom.bind(on_press=self.findRoomFunction)
        self.inside.add_widget(self.findRoom)

        self.about = Button(text="About", font_size=35)
        self.about.bind(on_press=self.aboutFunction)
        self.inside.add_widget(self.about)

        self.add_widget(self.inside)

        self.map = Label(text="INSERT MAP HERE", font_size = 40)
        #self.map = TextInput(multiline=False)
        self.add_widget(self.map)

    def aboutFunction(self, instance):
        print("About called")
    def findRoomFunction(self, instance):
        print("Find a room Called")
class MyApp(App):

    def build(self):
        return GridHolder()


if __name__ == '__main__':
    MyApp().run()

