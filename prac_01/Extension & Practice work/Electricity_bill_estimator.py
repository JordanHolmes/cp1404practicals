price_per_kWh_in_cents = int(input("Cents per kWh: "))
daily_use_in_kWh = float(input("Daily use in kWh: "))
number_of_days_in_the_billing_period = int(input("Number of billing days: "))

price_per_kWh_in_cents /= 100
daily_use_for_billing_period = daily_use_in_kWh * number_of_days_in_the_billing_period
estimated_bill = price_per_kWh_in_cents * daily_use_for_billing_period

print("Final bill: ${:.2f}".format(estimated_bill))
