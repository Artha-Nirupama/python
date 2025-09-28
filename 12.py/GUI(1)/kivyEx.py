from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Hello Kivy!")
        button = Button(text="Click")
        button.bind(on_press=self.change_text)

        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def change_text(self, instance):
        self.label.text = "Clicked!"

MyApp().run()
