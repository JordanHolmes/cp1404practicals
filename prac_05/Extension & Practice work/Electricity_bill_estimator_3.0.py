tariff_dict = {11: 0.244618, 31: 0.136928, 25: 0.216372, 46: 0.163529, 21: 0.097364}

tariff_used_by_user = int(input("Which tariff? {}, {}, {}, {}, or {}: ".format(*tariff_dict.keys())))
while tariff_used_by_user not in tariff_dict:
    print("Invalid selection!")
    tariff_used_by_user = input("Which tariff? {}, {}, {}, {}, or {}: ".format(*tariff_dict.keys()))

tariff_for_billing_period = tariff_dict[tariff_used_by_user]
daily_use_in_kWh = float(input("Daily use in kWh: "))
number_of_days_in_the_billing_period = int(input("Number of billing days: "))
daily_use_for_billing_period = daily_use_in_kWh * number_of_days_in_the_billing_period
estimated_bill = tariff_for_billing_period * daily_use_for_billing_period

print("Estimated bill: ${:.2f}".format(estimated_bill))

# TODO: error checking loop for if a valid tariff is selected