Aquarium_ticket = float(input('Enter the number of tickets for Aquarium only: '))
IMAX_ticket = float(input('Enter the number of tickets for IMAX only: '))
Combo_ticket = float(input('Enter the number of tickets for the IMAX and Aquarium combo: '))
Total_Amount = (Aquarium_ticket * 14) + (IMAX_ticket * 8) + (Combo_ticket * 16.5)
print('Total Amount: $', format (Total_Amount, '.2f'))
