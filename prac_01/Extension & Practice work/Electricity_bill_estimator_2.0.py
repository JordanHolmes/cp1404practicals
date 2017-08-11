TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_used_by_user = (input("Which tariff? 11 or 31: "))
while tariff_used_by_user != "11" and tariff_used_by_user != "31":
    print("Invalid selection!")
    tariff_used_by_user = (input("Which tariff? 11 or 31: "))

if tariff_used_by_user == "11":
    tariff_for_billing_period = TARIFF_11
else:
    tariff_for_billing_period = TARIFF_31

daily_use_in_kWh = float(input("Daily use in kWh: "))
number_of_days_in_the_billing_period = int(input("Number of billing days: "))
daily_use_for_billing_period = daily_use_in_kWh * number_of_days_in_the_billing_period
estimated_bill = tariff_for_billing_period * daily_use_for_billing_period

print("Estimated bill: ${:.2f}".format(estimated_bill))
