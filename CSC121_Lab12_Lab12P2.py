print('Converting US Dollar to a foreign currency')
def main():
    foreign_currency, dollar_amount = get_user_input()
    currency_calculator(foreign_currency, dollar_amount)


def get_user_input():

    """Prompts user to determine which currency they want to convert to and how much money they are converting"""

    foreign_currency = int(input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: '))
    while foreign_currency not in (1, 2, 3):
        print("Error: Invalid Choice")
        foreign_currency = int(input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: '))
    dollar_amount = int(input('Enter US Dollar: '))
    while dollar_amount < 0:
        print("US Dollar amount cannot be negative")
        dollar_amount = float(input('Enter US Dollar: '))
    return foreign_currency, dollar_amount


def currency_calculator(foreign_currency, dollar_amount):

    """Imports functions from currency module to determine the amount of foreign currency"""

    if foreign_currency == 1:
        from currency import to_euro
        conversion = to_euro(dollar_amount)
        print("It is converted to ", conversion, 'Euros')
    elif foreign_currency == 2:
        from currency import to_yen
        conversion = to_yen(dollar_amount)
        print("It is converted to ", conversion, 'Yen')
    else:
        from currency import to_peso
        conversion = to_peso(dollar_amount)
        print("It is converted to ", conversion, 'Pesos')


main()
