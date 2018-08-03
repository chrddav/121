def main():
    killowatt_hours = int(input("Enter kilowatt hours used: "))
    classification = input("Enter R for residential customer, B for business customer ")
    bill_calculator(y=classification, x=killowatt_hours)


def bill_calculator(y, x):
    if y == 'R':
        if x > 500:
            amount = ((x - 500) * 0.15) + 60
            print("Please pay this amount: ", amount)
        else:
            amount = x * 0.12
            print("Please pay this amount: ", amount)
    else:
        if x > 800:
            amount = ((x - 800) * 0.20) + 128
            print("Please pay this amount: ", amount)
        else:
            amount = x * 0.16
            print("Please pay this amount: ", amount)


main()
