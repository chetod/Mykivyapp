from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty, BooleanProperty

class MathGame(BoxLayout):
    score = NumericProperty(0)#save scores 
    question = StringProperty("Press Start to Begin") # Show question only string
    game_active = BooleanProperty(False) # to add start button
    
    def check_answer(self, answer_text): # fucntion check
        self.question = "This is where the answer will be checked." 

class MathGameApp(App):
    def build(self):
        return MathGame()

if __name__ == '__main__':
    MathGameApp().run()
