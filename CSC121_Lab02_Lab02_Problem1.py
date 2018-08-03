hotdogs = float(input('Enter number of hotdogs ordered: '))
potato_chips = float(input('Enter number of potato chips ordered: '))
soda_cans = float(input('Enter number of soda cans ordered: '))
total_amount = (hotdogs * 2.5) + (potato_chips * 1.5) + (soda_cans * 1.25)
print('Total Amount: $', format(total_amount, '.2f'))

