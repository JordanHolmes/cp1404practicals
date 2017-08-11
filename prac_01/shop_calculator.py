total_price = 0  # starting value

number_of_items = int(input("Number of items: "))
while number_of_items < 0:  # input validation loop (for number of items)
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):  # run input loop enough to fill all items required
    price_of_item = float(input("Enter price of item: $"))
    while price_of_item < 0:  # input validation loop (for price)
        print("Invalid price of item!")
        price_of_item = float(input("Enter price of item: $"))
    total_price += price_of_item  # outside input validation loop (sum of prices)

if total_price > 100:
    total_price *= 0.9  # 10% discount, therefore 90% of previous price

print("Your final price is: ${:.2f}".format(total_price))  # formatted to two decimal places
