from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class ProgramByRohan(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text="Program by Rohan"))

        self.password = TextInput(password=True)
        layout.add_widget(self.password)

        btn = Button(text="Unlock")
        btn.bind(on_press=self.unlock)
        layout.add_widget(btn)

        self.result = Label(text="")
        layout.add_widget(self.result)

        return layout

    def unlock(self, instance):
        if self.password.text == "rohank1234":
            self.result.text = "Welcome Rohan"
        else:
            self.result.text = "Wrong Password"

ProgramByRohan().run()
