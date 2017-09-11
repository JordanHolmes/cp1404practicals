from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934

class Convertmilestokilometres(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_increment(self, change):
        try:
            input_value = float(self.root.ids.input_name.text)
        except ValueError:
            input_value = 0
        self.root.ids.input_name.text = str(input_value + change)
        self.handle_calculate()

    def handle_calculate(self):
        try:
            input_value = float(self.root.ids.input_name.text)
        except ValueError:
            input_value = 0
        self.root.ids.label.text = str(input_value * MILES_TO_KILOMETRES)


Convertmilestokilometres().run()
