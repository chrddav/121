car = input("Enter C for compact, M for midsize, F for full size: ")
if car in ('C', 'M', 'F', 'c', 'm', 'f'):
    days = int(input("How many days?"))
    if days <= 0:
        print("Invalid number of days. Program ended")
    else:
        if car in ('C', 'c'):
            fee = 90 + (26 * (days - 3))
            if days < 4:
                fee = 30 * days
            print("Rental fee: ", fee)
        elif car in ('M', 'm'):
            fee = 111 + (32 * (days - 3))
            if days < 4:
                fee = 37 * days
            print("Rental fee: ", fee)
        else:
            fee = 135 + (38 * (days - 3))
            if days < 4:
                fee = 45 * days
            print("Rental fee: ", fee)
else:
    print("Invalid car type. Program ended")

