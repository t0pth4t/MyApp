from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import tweepy


class MainScreen(BoxLayout):
    def on_enter(self, instance):
        self.view.dismiss()
        shit = self.typer.text
        print(shit)
        self.typer.text = ""
    def on_event(self, obj):
        self.view.open()
class MyApp(App):
    def build(self):
        return MainScreen()
if __name__ == "__main__":
    MyApp().run()