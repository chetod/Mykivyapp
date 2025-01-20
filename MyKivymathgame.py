import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
class MathGame(BoxLayout):
    score = NumericProperty(0)
    timer = NumericProperty(60)
    question = StringProperty("Press Start to Begin")
    game_active = BooleanProperty(False)
    current_answer = None

    def __init__(self, **kwargs):
        super(MathGame, self).__init__(**kwargs)
        self.initial_time = 60
    
    def start_game(self):
        self.game_active = True
        self.generate_question()
        Clock.schedule_interval(self.update_timer, 1)

    def show_exit_confirmation(self):
        """Show confirmation popup before exiting"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Are you sure you want to exit?'))
        
        buttons = BoxLayout(size_hint_y=None, height=40, spacing=10)
        
        popup = Popup(title='Confirm Exit', 
                     content=content,
                     size_hint=(0.6, 0.3),
                     auto_dismiss=False)
        
        def confirm_exit(instance):
            App.get_running_app().stop()
            
        def cancel_exit(instance):
            popup.dismiss()
            
        yes_button = Button(text='Yes')
        no_button = Button(text='No')
        
        yes_button.bind(on_press=confirm_exit)
        no_button.bind(on_press=cancel_exit)
        
        buttons.add_widget(yes_button)
        buttons.add_widget(no_button)
        content.add_widget(buttons)
        
        popup.open()

    def exit_game(self, instance):
        if self.game_active:
            self.show_exit_confirmation()
        else:
            App.get_running_app().stop()

    def check_answer(self, answer_text):
        """Check the answer"""
        if not self.game_active:
            return

        try:
            user_answer = int(answer_text)
            if user_answer == self.current_answer:
                self.score += 1
                self.ids.status_label.text = "Correct!"
                self.ids.status_label.color = (0, 1, 0, 1)  # Green
            else:
                self.ids.status_label.text = f"Wrong! The correct answer was {self.current_answer}"
                self.ids.status_label.color = (1, 0, 0, 1)  # Red
        except ValueError:
            self.ids.status_label.text = "Please enter a valid number!"
            self.ids.status_label.color = (1, 0, 0, 1)
            return
        self.ids.answer_input.text = ""
        self.generate_question()
    
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
    
    def end_game(self):
        """End the game"""
        self.game_active = False
        Clock.unschedule(self.update_timer)
        self.question = f"Game Over! Final Score: {self.score}"
        self.ids.status_label.text = "Press Reset to play again"
        self.ids.status_label.color = (1, 1, 1, 1)
    
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
