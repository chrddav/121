def main():
    x = int(input("Enter kilowatt hours used: "))
    bill_calculator(x)


def bill_calculator(x):
    if x > 500:
        amount = ((x - 500) * 0.15) + 60
        print("Please pay this amount: ", amount)
    else:
        amount = x * 0.12
        print("Please pay this amount: ", amount)


main()
