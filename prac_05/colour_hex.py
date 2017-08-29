"""
CP1404/CP5632 Practical
Colour hex in dictionary
"""

COLOUR_HEX = {"white": "#ffffff", "tan": "#d2b48c", "slateblue": "#6a5acd", "powderblue": "#b0e0e6",
              "orangered1": "#ff4500", "maroon": "#b03060", "khaki": "#f0e68c", "hotpink": "#ff69b4",
              "gray41": "#696969", "firebrick2": "#ee2c2c", "aquamarine2": "#76eec6"}

colour = input("Enter the name of your colour: ").lower()
while colour != "":
    if colour in COLOUR_HEX:
        print(colour, "is", COLOUR_HEX[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter the name of your colour: ").lower()
