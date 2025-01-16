from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class NumberInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text='Input number:', size_hint_y=None, height=30)
        self.number_input = TextInput(
            multiline=False,
            input_type='number',  
            input_filter='float',  
            size_hint_y=None,
            height=40
        )
        layout.add_widget(label)
        layout.add_widget(self.number_input)
        return layout

if __name__ == '__main__':
    NumberInputApp().run()