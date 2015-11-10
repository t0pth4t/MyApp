from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class DemoBox(BoxLayout):
    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.buckets = "0"
        self.garbage = 0
        self.funct = 0
        self.tracker = TextInput(text=self.buckets)
        self.tracker.size_hint = (1, .1)
        self.add_widget(self.tracker)
        buttons = GridLayout(cols=4)
        self.add_widget(buttons)
        bt1 = Button(text="0")
        bt2 = Button(text="1")
        bt3 = Button(text="2")
        bt4 = Button(text="3")
        bt5 = Button(text="4")
        bt6 = Button(text="5")
        bt7 = Button(text="6")
        bt8 = Button(text="7")
        bt9 = Button(text="8")
        bt10 = Button(text="9")
        bt11 = Button(text="+")
        bt12 = Button(text="-")
        bt13 = Button(text="=")
        bt14 = Button(text="*")
        bt15 = Button(text="/")
        bt13.bind(on_press=self.numclear)
        for but in [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt10, bt11, bt12, bt13, bt14, bt15]:
            but.bind(on_press=self.trackerupdate)
        bt1.bind(on_press=self.press0)
        bt2.bind(on_press=self.press1)
        bt3.bind(on_press=self.press2)
        bt4.bind(on_press=self.press3)
        bt5.bind(on_press=self.press4)
        bt6.bind(on_press=self.press5)
        bt7.bind(on_press=self.press6)
        bt8.bind(on_press=self.press7)
        bt9.bind(on_press=self.press8)
        bt10.bind(on_press=self.press9)
        bt11.bind(on_press=self.adder)
        bt12.bind(on_press=self.minuser)
        bt13.bind(on_press=self.equals)
        bt14.bind(on_press=self.multiplyer)
        bt15.bind(on_press=self.divider)
        for but in [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, bt10, bt11, bt12, bt13, bt14, bt15]:
            buttons.add_widget(but)
    def divider(self,obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = "0"
        self.funct = 4
    def multiplyer(self,obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = "0"
        self.funct = 3
    def equals(self,obj):
        if self.funct == 1:
            self.buckets = int(self.buckets)
            self.buckets += self.garbage
            print(self.buckets)
        elif self.funct == 2:
            self.buckets = int(self.buckets)
            self.buckets = self.garbage - self.buckets
            print(self.buckets)
        elif self.funct == 3:
            self.buckets = int(self.buckets)
            self.buckets = self.garbage * self.buckets
            print(self.buckets)
        elif self.funct == 4:
            self.buckets = int(self.buckets)
            self.buckets = self.garbage / self.buckets
            self.buckets = float(self.buckets)
            print(self.buckets)
        
    def adder(self, obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = "0"
        self.funct = 1
    def minuser(self,obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = "0"
        self.funct = 2
    def printer(self, obj):
        print(self.buckets)
    def trackerupdate(self, obj):
        self.tracker.text = str(float(self.buckets))
    def numclear(self, obj):
        self.buckets = "0"
    def press0(self, obj):
        self.buckets += "0"
    def press1(self, obj):
        self.buckets += "1"
    def press2(self, obj):
        self.buckets += "2"
    def press3(self, obj):
        self.buckets += "3"
    def press4(self, obj):
        self.buckets += "4"
    def press5(self, obj):
        self.buckets += "5"
    def press6(self, obj):
        self.buckets += "6"
    def press7(self, obj):
        self.buckets += "7"
    def press8(self, obj):
        self.buckets += "8"
    def press9(self, obj):
        self.buckets += "9"
    def on_property(self, obj, value):
        print("Typical property change from", obj, "to", value)

class DemoApp(App):
    def build(self):
        return DemoBox()

if __name__ == "__main__":
    DemoApp().run()