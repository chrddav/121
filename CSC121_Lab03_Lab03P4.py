shipping = (input('Enter S for Standard shipping, E for Express: '))
weight = float(input('Enter weight in pounds (lbs): '))
if shipping == 'S' and weight <= 4:
    charge = weight * 1.05
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'S' and weight < 8:
    charge = weight * 0.95
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'S' and weight < 15:
    charge = weight * 0.85
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'S' and weight > 15:
    charge = weight * 0.8
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'E' and weight <= 2:
    charge = weight * 3.25
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'E' and weight < 5:
    charge = weight * 2.95
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'E' and weight < 10:
    charge = weight * 2.75
    print('Shipping charge: $', format(charge, '.2f'))
elif shipping == 'E' and weight > 10:
    charge = weight * 2.55
    print('Shipping charge: $', format(charge, '.2f'))







