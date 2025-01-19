import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
class MathGame(BoxLayout):
    score = NumericProperty(0)
    timer = NumericProperty(60)
    question = StringProperty("Press Start to Begin")
    game_active = BooleanProperty(False)

    def start_game(self):
        self.game_active = True
        self.generate_question()
        Clock.schedule_interval(self.update_timer, 1)
        current_answer = None
    
    def check_answer(self, answer_text):
        
        """Check the answer"""
        if not self.game_active:
            return
        user_answer = int(answer_text)
        if user_answer == self.current_answer:
                self.score += 1
                self.ids.status_label.text = "Correct!"
                self.ids.status_label.color = (0, 1, 0, 1)  # Green

        
    
    def show_settings(self):
        
        print("Settings button clicked!")

    def reset_game(self):
        """Reset the game"""
        self.score = 0
        self.timer = self.initial_time
        self.stack = []
        if hasattr(self, 'ids') and 'answer_input' in self.ids:
            self.ids.answer_input.text = ""
            self.ids.status_label.text = ""
        self.start_game()
    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        self.current_answer = num1 + num2
        self.question = f"{num1} + {num2} = ?"
    def update_timer(self, dt):
        """Update the timer"""
        if self.game_active:
            self.timer -= 1
            if self.timer <= 0:
                self.end_game()
class MathGameApp(App):
    def build(self):
        return MathGame()

if __name__ == '__main__':
    MathGameApp().run()
