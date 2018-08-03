customer = (input('Enter R for residential customer or B for business customer: '))
water = float(input('How many gallons of water were used?: '))
if customer == 'R' and water <= 6000:
    charge = water * 0.005
    print('Please pay this amount: $', format(charge, '.2f'))
elif customer == 'R' and water > 6000:
    charge = (water - 6000) * 0.007 + 30
    print('Please pay this amount: $', format(charge, '.2f'))
elif customer == 'B' and water <= 8000:
    charge = water * 0.006
    print('Please pay this amount: $', format(charge, '.2f'))
elif customer == 'B' and water > 8000:
    charge = (water - 8000) * 0.008 + 48
    print('Please pay this amount: $', format(charge, '.2f'))
