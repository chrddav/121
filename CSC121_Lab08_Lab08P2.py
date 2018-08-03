def main():
    customer, kWh_used = get_user_input()
    bill_calculator(customer, kWh_used)


def get_user_input():
    kWh = float(input("Enter kilowatt hours used: "))
    while kWh < 0:
        print("kWh cannot be negative")
        kWh = float(input("Enter kilowatt hours used: "))
    customer = input("Enter R for residential customer, B for business customer: ")
    while is_invalid(customer) == True:
        print("Invalid customer type.")
        customer = input("Enter R for residential customer, B for business customer: ")
    customer = customer.upper()
    return customer, kWh

def is_invalid(cust):
    if cust == 'r':
        invalid = False
    elif cust == 'R':
        invalid = False
    elif cust == 'b':
        invalid = False
    elif cust == 'B':
        invalid = False
    else:
        invalid = True

    return invalid

def bill_calculator(customer, kWh_used):
    if customer == 'R':
        if kWh_used > 500:
            amount = ((kWh_used - 500) * 0.15) + 60
            print("Please pay this amount: ", format(amount, '.2f'))
        else:
            amount = kWh_used * 0.12
            print("Please pay this amount: ", format(amount, '.2f'))
    else:
        if kWh_used > 800:
            amount = ((kWh_used - 800) * 0.20) + 128
            print("Please pay this amount: ", format(amount, '.2f'))
        else:
            amount = kWh_used * 0.16
            print("Please pay this amount: ", format(amount, '.2f'))


main()
