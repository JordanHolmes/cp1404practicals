from kivy.app import App
from kivy.lang import Builder


class ScoreGrade(App):
    def build(self):
        self.title: 'Score Grade'
        self.root = Builder.load_file("score_grade.kv")
        return self.root

    def calculate(self):
        print('test calculate')
        try:
            score = float(self.root.ids.score_input.text)
        except ValueError:
            score = -1
        # if score < 50 or score > 100:
        #     self.root.ids.result_label.text = "Fail"
        # else:
        #     self.root.ids.result_label.text = "Pass"
        self.root.ids.result_label.text = self.calculate_grade(score)

    def calculate_grade(self, score):
        if score < 0 or score > 100:
            return "Invalid score"
        elif score >= 85:
            return "High Distinction"
        elif score >= 75:
            return "Distinction"
        elif score >= 65:
            return "Credit"
        elif score >= 50:
            return "Pass"
        else:
            return "Fail"

    def clear(self):
        print('test clear')
        self.root.ids.score_input.text = ''
        self.root.ids.result_label.text = ''

ScoreGrade().run()
