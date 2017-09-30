"""Demonstration of ProgramingLanguage class"""

from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)
    python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    programming_languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are: ")
    for programming_language in programming_languages:
        if programming_language.typing == "Dynamic":
            print(programming_language.name)
main()
