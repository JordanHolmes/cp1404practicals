from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KILOMETRES = 1.60934


class MilesToKilometresConverter(App):
    def build(self):
        Window.size = 300, 300
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_increment(self, change):
        try:
            input_value = float(self.root.ids.input_name.text)
        except ValueError:
            input_value = 0
        new_miles_text = str(input_value + change)
        self.root.ids.input_name.text = new_miles_text
        self.handle_calculate(new_miles_text)

    def handle_calculate(self, text):
        try:
            input_value = float(text)
        except ValueError:
            input_value = 0
        self.root.ids.label.text = str(input_value * MILES_TO_KILOMETRES)
#TODO: Don't repeat yourself when using the try to check for a float/int value

MilesToKilometresConverter().run()
