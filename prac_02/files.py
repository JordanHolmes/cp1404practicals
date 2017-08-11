out_file = open("name.txt", "w")
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

in_file = open("numbers.txt", "r")
count = 0
for line in in_file:
    number = int(line)
    count += number
print(count)
in_file.close()
