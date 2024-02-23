from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle, Color
from kivy.metrics import dp

# Custom Button class with rounded corners
class RoundedButton(Button):
    def __init__(self, border_color, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.border_color = border_color
        self.canvas.before.add(Color(border_color[0], border_color[1], border_color[2]))  # Set border color
        self.canvas.before.add(RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(10)]))  # Rounded rectangle
        self.canvas.before.add(RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(10)], line_width=2))  # Border
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, instance, value):
        self.canvas.before.clear()
        self.canvas.before.add(Color(self.border_color[0], self.border_color[1], self.border_color[2]))  # Set border color
        self.canvas.before.add(RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(10)]))  # Rounded rectangle
        self.canvas.before.add(RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(10)], line_width=2))  # Border

# Main login screen layout
class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'  # Vertical arrangement
        self.spacing = dp(20)  # Spacing between widgets
        self.padding = [dp(20), dp(40)]  # Padding around the layout
        self.size_hint = (None, None)  # Fixed size
        self.width = dp(400)  # Width of the layout
        self.height = dp(600)  # Height of the layout
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}  # Center the layout in the window

        # Add image
        self.add_widget(Image(source='SkillSwipe.png'))  # Replace 'SkillSwipe.png' with your image path

        buttons_layout = BoxLayout(spacing=dp(20), size_hint_y=None, height=dp(50))  # Layout for buttons
        self.register_button = RoundedButton(
            text='REGISTER',
            size_hint=(None, None),
            width=dp(200),
            height=dp(50),
            background_color=[0.2, 0.7, 0.8, 1],  # Light blue background color
            color=[1, 1, 1, 1],  # White text color
            border_color=[0.2, 0.7, 0.8, 1]  # Light blue border color
        )
        self.login_button = RoundedButton(
            text='LOGIN',
            size_hint=(None, None),
            width=dp(200),
            height=dp(50),
            background_color=[0.2, 0.7, 0.8, 1],  # Light blue background color
            color=[1, 1, 1, 1],  # White text color
            border_color=[0.2, 0.7, 0.8, 1]  # Light blue border color
        )

        buttons_layout.add_widget(self.register_button)
        buttons_layout.add_widget(self.login_button)

        self.add_widget(buttons_layout)

# App class
class ContractorFindingApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set white background color
        return LoginScreen()  # Return an instance of the LoginScreen

# Run the app
if __name__ == '__main__':
    ContractorFindingApp().run()
