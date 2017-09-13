from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jordan Holmes", "Bill Worthington", "Max Power", "Chad Steel"]

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file("dynamic_widgets.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.namesBox.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.namesBox.clear_widgets()

DynamicWidgetsApp().run()
