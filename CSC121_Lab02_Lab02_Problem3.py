Food_Charge = float(input('Enter the food charge: '))
Sales_Tip = Food_Charge * 0.18
Sales_Tax = Food_Charge * 0.07
Total_Amount = Food_Charge + Sales_Tip + Sales_Tax
print('Sales Tip:', format (Sales_Tip, '.2f'))
print('Sales Tax:', format (Sales_Tax, '.2f'))
print('Total Amount Due:', format (Total_Amount, '.2f'))
