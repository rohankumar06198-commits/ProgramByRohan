from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

class ProgramByRohan(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.layout.add_widget(Label(text="Program by Rohan"))

        self.password = TextInput(
            hint_text="Enter Password",
            password=True
        )
        self.layout.add_widget(self.password)

        btn = Button(text="Unlock")
        btn.bind(on_press=self.unlock)
        self.layout.add_widget(btn)

        self.result = Label(text="")
        self.layout.add_widget(self.result)

        return self.layout

    def unlock(self, instance):
        if self.password.text == "rohank1234":

            now = datetime.now()

            self.result.text = (
                "Welcome Rohan!\n\n"
                f"Date: {now.strftime('%d-%m-%Y')}\n"
                f"Time: {now.strftime('%H:%M:%S')}\n\n"
                "Calculator Ready"
            )
        else:
            self.result.text = "Wrong Password!"

ProgramByRohan().run()[app]
title = ProgramByRohan
package.name = programbyrohan
package.domain = org.rohan
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
