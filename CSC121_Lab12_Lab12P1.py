def main():
    count, total = scan_prices()
    total = discount(count, total)
    balance = promotion(count, total)
    makePayment(balance)


def scan_prices():

    """Prompts user for price of item until stopped. Will total the prices and number of items"""

    print("Welcome to the self-checkout system of Wake-mart")
    count = 0
    total = 0
    price = 1
    while price != 0:
        is_error = False
        if not is_error:
                try:
                    price = float(input("Enter price of item [or 0 to stop]: "))
                    if price > 0:
                        total = total + price
                        count +=1
                        print("Number of item: ", count, "Total ", total)
                    elif price < 0:
                        print("Price cannot be negative")
                    else:
                        print()
                except ValueError:
                    print('Invalid input. ')
    return count, total

def discount(count, total):

    """Will calculate a 10% discount and apply to total if total number of items is greater than 10"""

    if count >= 10:
        total = float("{0:.2f}".format(total * 0.9))
        print("You've got 10% discount for buying 10 items or more")
        print("Number of items: ", count, "Total: ", total, '\n')
        return total
    else:
        return total

def promotion(count, total):

    """Will prompt user to buy $50 dollar gift card for $40 if they have a total over $50"""

    if total >= 50:
        gift_card = input("Do you want to buy a $50 gift card for $40? [y/n] ")
        if gift_card == 'y':
            print("Thank you for buying a giftcard.")
            count = count + 1
            balance = total + 40
            print("Number of items: ", count, "Total: ", balance)
        else:
            balance = total
    else:
        balance = total
    return balance

def makePayment(balance):

    """Will Determine the method of payment by the user (cash or debit)"""

    payment = 0
    print('\n',"Payment options:")
    while payment not in (1, 2):
        payment = int(input("Enter 1 for cash, 2 for debit: "))
        if payment == 1:
            balance = payCash(balance)
        elif payment == 2:
            balance = payDebit(balance)
        else:
            payment = int(input("Enter 1 for cash, 2 for debit: "))

def payCash(balance):

    """Determines how much the user is paying in cash, only accepts $10, $5, and $1 bills, will calculate change"""

    print("This machine only accepts $10, $5, and $1 bills.")
    total_cash = 0
    while total_cash < balance:
        tens = int(input("How many $10 bills are you going to pay? "))
        fives = int(input("How many $5 bills are you going to pay? "))
        ones = int(input("How many $1 bills are you going to pay? "))
        total_cash = tens*10 + fives*5 + ones
        if total_cash < balance:
            print("Error: Total cash payment less than balance. Please reenter.", '\n')
    change = total_cash - balance
    print('Total cash paid: ', total_cash, '\n', 'Thank you for your payment', '\n', 'Change: ', float("{0:.2f}".format(change)))

def payDebit(balance):

    """Prompts user for Card number, Pin number, and how much they are paying. If payment is greater than amount due they will receive cash back"""

    card_number = input("Please enter a 16-digit card number: ")
    while len(card_number) != 16 or not card_number.isdigit():
        card_number = input("Please enter a 16-digit card number: ")
    pin = input("Please enter a 4-digit pin number: ")
    while len(pin) != 4 or not pin.isdigit():
        pin = input("Please enter a 4-digit pin number: ")
    payment = 0
    while payment < balance:
        payment = float(input("Please enter a payment amount: "))
        if payment < balance:
            print("Error: Payment amount cannot be smaller than balance")
        elif payment > balance:
            cash_back = payment - balance
            print('Thank you for your payment', '\n', 'Cash back', float("{0:.2f}".format(cash_back)))
        else:
            print("Thank you for your payment")


main()
