from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty, BooleanProperty

class MathGame(BoxLayout):
    pass
class MathGameApp(App):
    def build(self):
        return MathGame()

if __name__ == '__main__':
    MathGameApp().run()
