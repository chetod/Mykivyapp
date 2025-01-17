from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty, BooleanProperty

class MathGame(BoxLayout):
    score = NumericProperty(0)
    question = StringProperty("Press Start to Begin")
    game_active = BooleanProperty(False)

    def start_game(self):
        self.game_active = True
        self.question = "Game Started! Prepare for the first question."
    def check_answer(self, answer_text):
        
        self.question = "This is where the answer will be checked."

    def show_settings(self):
        
        print("Settings button clicked!")

    def reset_game(self):
        self.score = 0
        self.game_active = False
        self.question = "Press Start to Begin"

class MathGameApp(App):
    def build(self):
        return MathGame()

if __name__ == '__main__':
    MathGameApp().run()
