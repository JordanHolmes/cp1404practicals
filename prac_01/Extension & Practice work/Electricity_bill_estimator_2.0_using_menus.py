TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

MENU = """11 - Tariff 11
31 - Tariff 31
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "11":
        price_per_kWh_in_cents = TARIFF_11
        daily_use_in_kWh = float(input("Daily use in kWh: "))
        number_of_days_in_the_billing_period = int(input("Number of billing days: "))
        daily_use_for_billing_period = daily_use_in_kWh * number_of_days_in_the_billing_period
        estimated_bill = price_per_kWh_in_cents * daily_use_for_billing_period
        print("Your estimated bill is ${:.2f}".format(estimated_bill))
    elif choice == "31":
        price_per_kWh_in_cents = TARIFF_31
        daily_use_in_kWh = float(input("Daily use in kWh: "))
        number_of_days_in_the_billing_period = int(input("Number of billing days: "))
        daily_use_for_billing_period = daily_use_in_kWh * number_of_days_in_the_billing_period
        estimated_bill = price_per_kWh_in_cents * daily_use_for_billing_period
        print("Your estimated bill is ${:.2f}".format(estimated_bill))
    else:
        print("invalid input error message")
    print(MENU)
    choice = input(">>> ").upper()
print("Goodbye")
