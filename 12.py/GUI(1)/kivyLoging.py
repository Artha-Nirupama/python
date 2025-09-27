# save as kivy_login.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class LoginApp(App):
    def build(self):
        root = FloatLayout()

        # Background image
        bg = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        root.add_widget(bg)

        # Semi-transparent box (simulated blur)
        box = BoxLayout(orientation='vertical', size_hint=(0.4, 0.5), pos_hint={'center_x':0.5, 'center_y':0.5})
        box.padding = 20
        box.spacing = 15
        box.canvas.before.clear()
        with box.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(1, 1, 1, 0.25)  # semi-transparent white
            self.rect = RoundedRectangle(size=box.size, pos=box.pos, radius=[20])

        # Update rectangle size & pos on resize
        def update_rect(instance, value):
            self.rect.size = instance.size
            self.rect.pos = instance.pos
        box.bind(size=update_rect, pos=update_rect)

        # Widgets
        box.add_widget(Label(text="Login", font_size=30, color=(1,1,1,1)))
        self.username = TextInput(hint_text="Username", multiline=False, padding_y=(10,10))
        box.add_widget(self.username)
        self.password = TextInput(hint_text="Password", multiline=False, password=True, padding_y=(10,10))
        box.add_widget(self.password)
        login_btn = Button(text="Login", size_hint=(1, None), height=50, background_color=(0,0.5,1,0.8))
        login_btn.bind(on_press=self.login)
        box.add_widget(login_btn)

        root.add_widget(box)
        return root

    def login(self, instance):
        print(f"Username: {self.username.text}, Password: {self.password.text}")

if __name__ == "__main__":
    LoginApp().run()
