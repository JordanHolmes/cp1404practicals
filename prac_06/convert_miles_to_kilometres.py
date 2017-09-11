from kivy.app import App
from kivy.lang import Builder


class Convertmilestokilometres(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_increment(self, value):
        input_value = self.root.ids.input_name.text
        self.root.ids.input_name = int(input_value) + value

Convertmilestokilometres().run()
