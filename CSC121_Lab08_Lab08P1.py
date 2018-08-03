def main():
    kWh_used = get_kWh_used()
    bill_calculator(kWh_used)


def get_kWh_used():
    kWh = int(input("Enter kilowatt hours used: "))
    while kWh < 0:
        print("kWh cannot be negative")
        kWh = int(input("Enter kilowatt hours used: "))
    return kWh



def bill_calculator(kWh_used):
    if kWh_used > 500:
        amount = ((kWh_used - 500) * 0.15) + 60
        print("Please pay this amount: ", amount)
    else:
        amount = kWh_used * 0.12
        print("Please pay this amount: ", amount)


main()
